import socket
import tldextract
domainName = input('Enter the domain name: ')
print(tldextract.extract(domainName))
domainName=(tldextract.extract(domainName).domain)+"."+(tldextract.extract(domainName).suffix)
print(domainName)
print(socket.gethostbyname('www.youtube.com'))