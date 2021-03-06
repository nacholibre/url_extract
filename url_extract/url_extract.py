#!/usr/bin/env python
import sys
import codecs
import re
import os
import time
import urllib2


class Result(object):
    '''Results are returned as objects, this is the return object of the
    ExtractUrl.extract() method'''
    domValid = True
    tld = None
    domain = None
    query = None
    subdomains = []

    def setFoundSubdomains(self, subdomains):
        self.subdomains = subdomains

    def getFoundSubdomains(self):
        return self.subdomains

    def setTld(self, tld):
        self.tld = tld

    def getTld(self):
        return self.tld

    def setDomain(self, domain):
        self.domain = domain

    def getDomain(self):
        return self.domain

    def setValid(self, valid):
        self.domValid = valid

    def setUrlQuery(self, query):
        self.query = query

    def getUrlQuery(self):
        return self.query

    def getHostname(self):
        hostname = []
        subdomains = self.getFoundSubdomains()
        if subdomains:
            [hostname.append(x) for x in subdomains]
        hostname.append(self.getDomain())
        hostname.append(self.getTld())
        return '.'.join(hostname)

    def valid(self):
        return self.domValid


class SuffixList(object):
    suffixList = set()
    punyTranslator = None
    maxAge = None

    def __init__(self, maxAge, saveDir, punyTranslator):
        self.punyTranslator = punyTranslator
        self.maxAge = maxAge
        self.saveDir = saveDir
        self.fileLocation = self.generateLocation(saveDir, 'tlds.dat')

    def loadList(self):
        file = self.getFileLocation()
        if not self.fileExists(file) or not self.fresh(file, self.maxAge):
            self.downloadList(file)

        with open(self.getFileLocation(), 'r') as listHandler:
            for line in listHandler:
                line = line.strip()
                if line and line[0] != '/':
                    if self.punyTranslator.hasUtf(line):
                        line = self.punyTranslator.encode(line)
                        self.suffixList.add(line)
                    else:
                        self.suffixList.add(line)

    def generateLocation(self, saveDir, listName):
        if saveDir:
            fileLocation = '%s/%s' % (saveDir, listName)
        else:
            fileLocation = '%s/%s' % (os.getcwd(), listName)
        return fileLocation

    def getFileLocation(self):
        return self.fileLocation

    def fresh(self, file, maxAge):
        fresh = True
        if os.path.getmtime(file) + maxAge < time.time():
            fresh = False
        return fresh

    def fileExists(self, file):
        exists = True

        try:
            with open(file, 'r'):
                pass
        except Exception:
            exists = False

        return exists

    def downloadList(self, to):
        print 'Downloading list...'
        location = 'https://publicsuffix.org/list/effective_tld_names.dat'
        get = urllib2.urlopen(location)
        with open(to, 'w') as handler:
            handler.write(get.read())

    def getList(self):
        return self.suffixList

    def generateSufixesList(self, hostname):
        suffixes = []
        splitted = hostname.split('.')

        for i in xrange(0, len(splitted)):
            levels = splitted[i:]

            searchFor = '.'.join(levels)

            suffixes.append('!' + searchFor)
            suffixes.append('*.' + searchFor)
            suffixes.append(searchFor)
        return suffixes

    def searchSuffix(self, hostname):
        generatedDomainSuffixes = self.generateSufixesList(hostname)
        splittedHostname = hostname.split('.')

        foundSuffix = None

        for suffix in generatedDomainSuffixes:
            if suffix in self.getList():
                if suffix.startswith('!'):
                    splitted = suffix.split('.')
                    foundSuffix = '.'.join(splitted[1:])
                    break
                elif suffix.startswith('*'):
                    suffixLen = len(suffix.split('.'))
                    splittedHostname = list(reversed(splittedHostname))
                    index = suffixLen-1
                    if index >= len(splittedHostname):
                        break
                    host = splittedHostname[index]
                    suffix = suffix.replace('*', host)
                    foundSuffix = suffix
                    break
                else:
                    foundSuffix = suffix
                    break

        return foundSuffix


class DomainPunyTranslator(object):
    def hasUtf(self, string):
        return not all(ord(c) < 128 for c in string)

    def encode(self, string):
        result = []
        for chunk in string.split('.'):
            if self.hasUtf(chunk):
                chunk = 'xn--' + codecs.encode(chunk.decode('utf8'),
                                               'punycode')
            result.append(chunk)

        return '.'.join(result)

    def decode(self, url):
        decodedChunks = []

        for chunk in url.split('.'):
            if self.isPunyEncoded(chunk):
                punycode = '--'.join(chunk.split('--')[1:])
                chunk = codecs.decode(punycode, 'punycode')

            decodedChunks.append(chunk)

        url = '.'.join(decodedChunks).encode('utf8')

        return url

    def isPunyEncoded(self, url):
        puny = False

        if url.find('xn--') != -1:
            puny = True

        return puny


class UrlExtract(object):
    alwaysPuny = False

    suffixList = None
    punyTranslator = None

    def __init__(self, datFileMaxAge=86400*31,
                 datFileSaveDir=None, alwaysPuny=False):
        self.alwaysPuny = alwaysPuny

        self.punyTranslator = DomainPunyTranslator()

        self.suffixList = SuffixList(datFileMaxAge,
                                     datFileSaveDir, self.punyTranslator)
        self.suffixList.loadList()

    def trimUrl(self, url):
        url = url.lower().strip()
        url = url.replace('http://', '')
        url = url.replace('https://', '')
        return url

    def validDomain(self, domain):
        valid = True

        for hostname in domain.split('.'):
            #encode to puny, because if domain is in utf8 and the len is wrong
            hostname = self.punyTranslator.encode(hostname)

            if len(hostname) > 63:
                valid = False
            elif hostname.startswith('-'):
                valid = False
            elif hostname.endswith('-'):
                valid = False
            elif hostname.find(' ') != -1:
                valid = False

        return valid

    def normalizeEncoding(result, utfInput, punyInput):
        pass

    def extract(self, url):
        url = self.trimUrl(url)

        punyInput = self.punyTranslator.isPunyEncoded(url)
        utfInput = self.punyTranslator.hasUtf(url)

        urlChunks = url.split('/')
        hostname = urlChunks[0]

        if utfInput:
            hostname = self.punyTranslator.encode(hostname)

        foundSuffix = self.suffixList.searchSuffix(hostname)

        urlQuery = None
        valid = True
        foundSubdomains = []
        withoutTld = None

        if len(urlChunks) > 1:
            urlQuery = '/'.join(urlChunks[1:])

        if foundSuffix is None:
            valid = False
        else:
            withoutTld = re.sub(re.escape(foundSuffix)+'$', '', hostname)
            withoutTld = withoutTld[:-1]

            if withoutTld == '' or not self.validDomain(hostname):
                valid = False

            withoutTldSplitted = withoutTld.split('.')
            if len(withoutTldSplitted) > 1:
                subdomains = withoutTldSplitted
                withoutTld = withoutTldSplitted[-1]
                subdomains.remove(withoutTld)
                foundSubdomains = subdomains

        if utfInput:
            withoutTld = self.punyTranslator.decode(withoutTld)
            foundSuffix = self.punyTranslator.decode(foundSuffix)
            foundSubdomains = map(self.punyTranslator.decode, foundSubdomains)

        if punyInput or self.alwaysPuny:
            withoutTld = self.punyTranslator.encode(withoutTld)
            foundSuffix = self.punyTranslator.encode(foundSuffix)
            foundSubdomains = map(self.punyTranslator.encode, foundSubdomains)

        result = Result()

        if valid:
            result.setValid(True)
            result.setDomain(withoutTld)
            result.setTld(foundSuffix)
            result.setFoundSubdomains(foundSubdomains)
            result.setUrlQuery(urlQuery)
        else:
            result.setValid(False)

        return result

if __name__ == '__main__':
    url = sys.argv[1]

    extract = UrlExtract()
    extracted = extract.extract(url)
    print extracted.getDomain()
    print extracted.getTld()
    print extracted.getFoundSubdomains()
    print 'hostname', extracted.getHostname()
