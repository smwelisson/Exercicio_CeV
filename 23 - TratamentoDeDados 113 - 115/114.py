import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLError:
    print("Site não acessivel")
else:
    print("Site acessivel")
    print(site.read())