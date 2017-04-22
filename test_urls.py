"""Simple module to hit a list of URLs."""
import requests
from datetime import datetime


def main():
    """The main function that does all the work."""
    begin = datetime.now()
    urls = []
    failed_urls = []
    total_count = 0
    failed_count = 0
    passed_count = 0
    try:
        log = open('logging.txt', 'a')
    except IOError:
        log = open('logging.txt', 'w')
    print("Reading the URLS from the urls.txt file...")
    try:
        for line in open('urls.txt', 'r').readlines():
            li = line.strip()
            if not li.startswith("#"):
                urls.append(line.strip())
        print("Done.")
        print("Hitting the URLs now:")
        log.writelines('------------------------------------------------------'
                       '-------------------------------------------------\r\n')
        for url in urls:
            r = requests.head(url=url)
            if r.status_code == 200:
                passed_count += 1
            else:
                failed_count += 1
                failed_urls.append(url)
                log.writelines("%s - FAILED: %s.\r\n" % (
                    str(datetime.now()), url))
                log.writelines("Error code: %s \r\n" % r.status_code)
                print("Failed:")
                print("-------")
                print("URL: {}".format(url))
                print("URL returned {}".format(r.status_code))

        end = datetime.now()
        total_count = failed_count + passed_count

        log.writelines('                  ------------- Summary ---------\r\n')
        log.writelines('Total URLs tested: %s -- ' % total_count)
        log.writelines('Passed URLs: %s -- ' % passed_count)
        log.writelines('Failed URLs: %s -- ' % failed_count)
        log.writelines('-----------------------------------------------------'
                       '-------------------------------------------------\r\n')

        print("---------------------------------------")
        print("Total URLs tested: {}.".format(total_count))
        print("Passed URLs: {}.".format(passed_count))
        print("Failed URLs: {}.".format(failed_count))
        print("Failed URLs:")
        print("=============")
        for url in failed_urls:
            print(url)
        print("---------------------------------------")
        print("Test time: {}.".format(end - begin))

    except IOError:
        print("IOError: Could not locate 'urls.txt' file.")
        log.writelines("\r\n{} - IOError: Could not locate 'urls.txt'"
                       " file.".format(str(datetime.now())))

if __name__ == "__main__":
    main()
