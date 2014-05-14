#!/usr/bin/env python
# -*- coding: utf8 -*-
from url_extract.url_extract import UrlExtract


class testCase(object):
    urlInput = None
    returnedDomain = None
    returnedTld = None
    returnedSubdomains = []
    returnedUrlQuery = None
    returnedHostname = None
    valid = True

    def __init__(self):
        self.returnedSubdomains = []

    def setInput(self, inputUrl):
        self.urlInput = inputUrl

    def getInput(self):
        return self.urlInput

    def shouldReturnDomain(self, shouldReturn):
        self.returnedDomain = shouldReturn

    def shouldReturnUrlQuery(self, urlQuery):
        self.returnedUrlQuery = urlQuery

    def shouldReturnHostname(self, hostname):
        self.returnedHostname = hostname

    def getExpectedHostname(self):
        return self.returnedHostname

    def getExpectedUrlQuery(self):
        return self.returnedUrlQuery

    def getExptectedDomain(self):
        return self.returnedDomain

    def shouldReturnTld(self, shouldReturn):
        self.returnedTld = shouldReturn

    def getExpectedTld(self):
        return self.returnedTld

    def shouldBeValid(self, valid):
        self.valid = valid

    def getExpectedValid(self):
        return self.valid

    def shouldHaveSubdomain(self, subdomain):
        self.returnedSubdomains.append(subdomain)

    def getExpectedSubdomains(self):
        return self.returnedSubdomains


def generateTestCases():
    cases = []

    case = testCase()
    case.setInput('http://dir.bg')
    case.shouldReturnDomain('dir')
    case.shouldReturnTld('bg')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('http://dnes.dir.bg/news/volen-siderov-Сergey-Нarishkin-16638984?nt=4')
    case.shouldReturnDomain('dir')
    case.shouldReturnTld('bg')
    case.shouldHaveSubdomain('dnes')
    case.shouldBeValid(True)
    case.shouldReturnUrlQuery('news/volen-siderov-Сergey-Нarishkin-16638984?nt=4')
    cases.append(case)

    case = testCase()
    case.setInput('xn--h3cken9adhbc8a7ahfc3ad6deq0cf4vpad6pze.net')
    case.shouldReturnDomain('xn--h3cken9adhbc8a7ahfc3ad6deq0cf4vpad6pze')
    case.shouldReturnTld('net')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('xn--1000-y73c3e2qiaj0aap13b4cqa7f9ri047bwba340a13r6gmmv3dcm1i.net')
    case.shouldReturnDomain('xn--1000-y73c3e2qiaj0aap13b4cqa7f9ri047bwba340a13r6gmmv3dcm1i')
    case.shouldReturnTld('net')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('kobe.jp')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('http://blah.dir.bg')
    case.shouldReturnDomain('dir')
    case.shouldHaveSubdomain('blah')
    case.shouldReturnTld('bg')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('http://blah.dir.bg/sometest.php')
    case.shouldReturnDomain('dir')
    case.shouldHaveSubdomain('blah')
    case.shouldReturnTld('bg')
    case.shouldReturnUrlQuery('sometest.php')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('xn--b28h.to')
    case.shouldReturnDomain('xn--b28h')
    case.shouldReturnTld('to')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('http://www.dir.bg')
    case.shouldReturnDomain('dir')
    case.shouldReturnTld('bg')
    case.shouldHaveSubdomain('www')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('test.ide.kyoto.jp')
    case.shouldReturnDomain('test')
    case.shouldReturnTld('ide.kyoto.jp')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('www.test.ide.kyoto.jp')
    case.shouldReturnDomain('test')
    case.shouldReturnTld('ide.kyoto.jp')
    case.shouldHaveSubdomain('www')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('www.test.k12.ak.us')
    case.shouldReturnDomain('test')
    case.shouldReturnTld('k12.ak.us')
    case.shouldHaveSubdomain('www')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('www.食狮.公司.cn')
    case.shouldReturnDomain('食狮')
    case.shouldReturnTld('公司.cn')
    case.shouldHaveSubdomain('www')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('食狮.食狮.公司.cn')
    case.shouldReturnDomain('食狮')
    case.shouldReturnTld('公司.cn')
    case.shouldHaveSubdomain('食狮')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('www.xn--85x722f.xn--55qx5d.cn')
    case.shouldReturnDomain('xn--85x722f')
    case.shouldReturnTld('xn--55qx5d.cn')
    case.shouldHaveSubdomain('www')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('xn--12caaalsccaj7zg3ae5iba9ered8gyjsb1kvb3f.net')
    case.shouldReturnDomain('xn--12caaalsccaj7zg3ae5iba9ered8gyjsb1kvb3f')
    case.shouldReturnTld('net')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('blah.xn--12caaalsccaj7zg3ae5iba9ered8gyjsb1kvb3f.net')
    case.shouldReturnDomain('xn--12caaalsccaj7zg3ae5iba9ered8gyjsb1kvb3f')
    case.shouldReturnTld('net')
    case.shouldHaveSubdomain('blah')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('xn--85x722f.xn--85x722f.xn--55qx5d.cn')
    case.shouldReturnDomain('xn--85x722f')
    case.shouldReturnTld('xn--55qx5d.cn')
    case.shouldHaveSubdomain('xn--85x722f')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('test.xn--85x722f.xn--55qx5d.cn')
    case.shouldReturnDomain('xn--85x722f')
    case.shouldReturnTld('xn--55qx5d.cn')
    case.shouldHaveSubdomain('test')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('xn--85x722f.xn--85x722f.xn--55qx5d.cn')
    case.shouldReturnDomain('xn--85x722f')
    case.shouldReturnTld('xn--55qx5d.cn')
    case.shouldHaveSubdomain('xn--85x722f')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('公司.cn')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('k12.ak.us')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('https://www.dir.bg')
    case.shouldReturnDomain('dir')
    case.shouldReturnTld('bg')
    case.shouldHaveSubdomain('www')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('https://dir.dir.bg')
    case.shouldReturnDomain('dir')
    case.shouldReturnTld('bg')
    case.shouldHaveSubdomain('dir')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('https://ww w.dir.bg')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('https://www.d ir.bg')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('dir.b g')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('www.dir.b g')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('https://test.data.bg/blah/hah.html')
    case.shouldReturnDomain('data')
    case.shouldReturnTld('bg')
    case.shouldHaveSubdomain('test')
    case.shouldReturnUrlQuery('blah/hah.html')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput(' https://test.data.bg ')
    case.shouldReturnDomain('data')
    case.shouldReturnTld('bg')
    case.shouldHaveSubdomain('test')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('blah.parliament.uk')
    case.shouldReturnDomain('parliament')
    case.shouldReturnTld('uk')
    case.shouldHaveSubdomain('blah')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('parliament.uk')
    case.shouldReturnDomain('parliament')
    case.shouldReturnTld('uk')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('www.parliament.uk')
    case.shouldReturnDomain('parliament')
    case.shouldReturnTld('uk')
    case.shouldHaveSubdomain('www')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('ham-radio-op.net')
    case.shouldReturnDomain(None)
    case.shouldReturnTld(None)
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('test.ham-radio-op.net')
    case.shouldReturnDomain('test')
    case.shouldReturnTld('ham-radio-op.net')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('blah.uk')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('mda.co.uk')
    case.shouldReturnDomain('mda')
    case.shouldReturnTld('co.uk')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('www.mda.co.uk')
    case.shouldReturnDomain('mda')
    case.shouldReturnTld('co.uk')
    case.shouldHaveSubdomain('www')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('www.niki.national.museum')
    case.shouldReturnDomain('niki')
    case.shouldReturnTld('national.museum')
    case.shouldHaveSubdomain('www')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('www.президент.рф')
    case.shouldReturnDomain('президент')
    case.shouldReturnTld('рф')
    case.shouldHaveSubdomain('www')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('niki.pr')
    case.shouldReturnDomain('niki')
    case.shouldReturnTld('pr')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('niki'*20 + '.pr')
    case.shouldReturnDomain(None)
    case.shouldReturnTld(None)
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('www.niki.uk')
    case.shouldReturnDomain('www')
    case.shouldReturnTld('niki.uk')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('www.-mda.co.uk/test.com')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('https://-my.test.dir.bg')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('my-.test.dir.bg')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('http://www.notexistent.hello')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('notexistent.hello')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('com')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('co.uk')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('/site/xn----7sbe4aieideh6blm.blogspot.com')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('net')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('i.net')
    case.shouldReturnDomain('i')
    case.shouldReturnTld('net')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('www.i.net')
    case.shouldReturnDomain('i')
    case.shouldReturnTld('net')
    case.shouldHaveSubdomain('www')
    case.shouldBeValid(True)
    cases.append(case)

    case = testCase()
    case.setInput('')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput(' ')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('www.')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('www')
    case.shouldBeValid(False)
    cases.append(case)

    case = testCase()
    case.setInput('.bg')
    case.shouldBeValid(False)
    cases.append(case)
    return cases


if __name__ == '__main__':
    urlExtract = UrlExtract()

    testCases = generateTestCases()

    i = 0
    for case in testCases:
        errors = []

        extracted = urlExtract.extract(case.getInput())

        expectedSubdomains = sorted(case.getExpectedSubdomains())
        foundSubdomains = sorted(extracted.getFoundSubdomains())

        urlQuery = extracted.getUrlQuery()
        expectedUrlQuery = case.getExpectedUrlQuery()

        if extracted.valid() != case.getExpectedValid():
            errors.append('expected to be valid: %s' % case.getExpectedValid())
            errors.append('but got valid %s insted' % extracted.valid())

        if extracted.getDomain() != case.getExptectedDomain():
            errors.append('expected domain: %s' % case.getExptectedDomain())
            errors.append('but got %s insted' % extracted.getDomain())

        if extracted.getTld() != case.getExpectedTld():
            errors.append('expected tld: %s' % case.getExpectedTld())
            errors.append('but got %s insted' % extracted.getTld())

        if expectedUrlQuery != urlQuery:
            errors.append('expected url query: %s' % expectedUrlQuery)
            errors.append('but got %s insted' % urlQuery)

        if expectedSubdomains != foundSubdomains:
            errors.append('exptected subdomains: %s' % expectedSubdomains)
            errors.append('found subdomains: %s' % foundSubdomains)

        if errors:
            print '=' * 50
            print 'ERRORS FOUND FOR %s' % case.getInput()
            print '=' * 50
            for error in errors:
                print error
            break

        i = i+1
        if i == len(testCases):
            print 'All tests passed'
