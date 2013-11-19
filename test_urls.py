import urllib2
from urllib2 import URLError
from datetime import datetime as time


def main():
    begin = time.now()
    urls = []
    failed_urls = []
    total_count = 0
    failed_count = 0
    passed_count = 0
    try:
        log = open('logging.txt', 'a')
    except IOError:
        log = open('logging.txt', 'w')
    print "Reading the URLS from the wsdls.txt file..."
    try:
        for line in open('wsdls.txt', 'r').readlines():
            li = line.strip()
            if not li.startswith("#"):
                urls.append(line.strip())
        print "Done."
        print "Hitting the WSDL URLs now:"
        log.writelines('------------------------------------------------------'
                       '-------------------------------------------------\r\n')

        for url in urls:
            try:
                r = urllib2.urlopen(url)
                passed_count += 1
            except URLError, e:
                failed_count += 1
                failed_urls.append(url)
                log.writelines("%s - FAILED: %s.\r\n" % (str(time.now()), url))
                log.writelines("Error code: %s \r\n" % e.code)
                print ""
                print "Failed:"
                print "-------"
                print ""
                print "URL: %s" % url
                print "URL returned %s." % e.code  # urllib
                print ""

        end = time.now()
        total_count = failed_count + passed_count

        log.writelines('                  ------------- Summary ---------\r\n')
        log.writelines('Total URLs tested: %s -- ' % total_count)
        log.writelines('Passed URLs: %s -- ' % passed_count)
        log.writelines('Failed URLs: %s -- ' % failed_count)
        log.writelines('-----------------------------------------------------'
                       '-------------------------------------------------\r\n')

        print ""
        print "---------------------------------------"
        print "Total URLs tested: %s." % total_count
        print "Passed URLs: %s." % passed_count
        print "Failed URLs: %s." % failed_count
        print ""
        print "Failed URLs:"
        print "============="
        for url in failed_urls:
            print url
        print "---------------------------------------"
        print ""
        print "Test time: %s." % (end - begin)

    except IOError:
        print "IOError: Could not locate 'wsdls.txt' file."
        log.writelines("\r\n%s - IOError: Could not locate 'wsdls.txt' file."
                       % (str(time.now())))

if __name__ == "__main__":
    main()
