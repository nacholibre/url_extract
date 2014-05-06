#!/usr/bin/python-whoisrequest
from url_extract.url_extract import UrlExtract


if __name__ == '__main__':
    extract = UrlExtract()
    with open('/home/nacholibre/whoisrequest/data/com.01.50k.txt', 'r') as f:
        for line in f:
            line = line.strip()
            try:
                domain, ns = line.split(' NS ')
            except Exception:
                pass
            else:
                domain = domain.lower()+'.com'
                result = extract.extract(domain)
