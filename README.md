URL Extract
=========
This module extracts tld, domain, subdomains and query from URLs. It also validates the URLs.
Installation
---------
```
pip install url_extract
```
Usage
---------
```
>>> from url_extract import UrlExtract
>>> extract = UrlExtract()
Downloading list...
>>> extracted = extract.extract('http://dir.bg')
>>> extracted.getDomain()
'dir'
>>> extracted.getTld()
'bg'
>>> extracted.valid()
>>> True
>>> extracted = extract.extract('http://police.uk')
>>> extracted.valid()
False
```
Documentation
--------
####*class* **UrlExtract** (datFileMaxAge=86400*31, datFileSaveDir=None, alwaysPuny=None)####
* datFileMaxAge specifies the max age of the [public suffix list](https://publicsuffix.org/list/effective_tld_names.dat)
* datFileSaveDir specifies where will the public suffix list (tlds.dat) will be downloaded
* alwaysPuny if set to True unicoded domains after extract will be punyencoded
* **extract(url)** - Extracts the url and returns Result() object

---------

####*class* Result ()####

* **getDomain()** - Returns domain name without subdomains and tld.
* **getTld()** - Returns the tld of the domain
* **valid()** - Validates domain and returns True or False
* **getFoundSubdomains()** - Returns the extracted subdomains as list
* **getUrlQuery()** - Returns the query after the first / in the url
