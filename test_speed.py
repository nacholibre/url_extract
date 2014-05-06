#!/usr/bin/python-whoisrequest
from extract_url.extract_url import ExtractUrl


if __name__ == '__main__':
    extract = ExtractUrl()
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
