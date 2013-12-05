<b>Automate URL Test</b><br />
A simple python script that hits a list of URLs for testing

Opens the urls.txt file to read in URLs. Iterates over each request and displays information to the screen as well as writes output to a log file.

If a request returns something other than a 200 response code, the script with wait 10 seconds and try it again.

To run: <pre>python test_urls.py</pre>