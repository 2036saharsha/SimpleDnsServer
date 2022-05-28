import webbrowser
import dns.resolver
import tldextract
DNS_BOOK_ISP={}
DNS_BOOK_DEVICE={}

def BrowserOpen(domainName):
    chrome=webbrowser.Chrome("$path to your browser")
    chrome.open_new_tab(domainName)
def Device():
    domainName = input('Enter the domain name: ')
    domainName=(tldextract.extract(domainName).domain)+"."+(tldextract.extract(domainName).suffix)
    print("FINDING THE IP IN THE DEVICE")
    if DNS_BOOK_DEVICE.get(domainName)==None:
        print("NOT FOUND IN CACHE MEMEORY OF THE DEVICE....FORWARDING TO ISP")
        try:
            Ip=Isp_DNS_Resolver(domainName)
        except:
            print("Domain Name Not registered")
            return
        print("Received ip of domainName from ISP.....User's device")
        DNS_BOOK_DEVICE.update({domainName: Ip})
        BrowserOpen(domainName)
        print("The IP address of",domainName,"is",Ip)
        n=input("Do you want to continue? y or n: ")
        if n =="y":
            Device()
        else:
            exit
    else:
        print("The IP address of",domainName,"is",DNS_BOOK_DEVICE.get(domainName))
        BrowserOpen(domainName)
        n=input("Do you want to continue? y or n: ")
        if n =="y":
            Device()
        else:
            exit
        
def Isp_DNS_Resolver(domainName):
    
    if DNS_BOOK_ISP.get(domainName)==None:
       print("IN.....ISP_resolver")
       Address_TLD=Root_Name_Server(domainName)
       print("Received address of TLD from RNS..... ISP")
       ANS_address= Top_level_Domain(domainName,Address_TLD)
       print("Received address of ANS from TLD..... ISP")
       
       IP=Authoritative_Name_Server(domainName,ANS_address)
       DNS_BOOK_ISP.update({domainName: IP})
       print("Received ip of domainName from ANS.....ISP")
       return(IP)
    else:
        return(DNS_BOOK_ISP.get(domainName))
    
      
def Root_Name_Server(domainName):
    print("IN.....Root_Name_server")
    suffix=tldextract.extract(domainName).suffix
    resolver=dns.resolver.Resolver()
    result = resolver.resolve(suffix, 'NS')

    for val in result:
        if (val.to_text()[:1]) == suffix[:1]:
            Name_server=val.to_text()

    TLD_IPS = resolver.resolve(Name_server, 'A')
    
    for val in TLD_IPS:
        TLD_IP=val.to_text()
    print("Found",TLD_IP,"in RNS")
    print("Address of TLDCOM server",TLD_IP)
    return(TLD_IP)
       
def Top_level_Domain(domainName,Address_TLD):
    print("IN.....Top_level_domain")
    # Get Authoritative Name server of the domain

    res = dns.resolver.Resolver()
    r = res.resolve(domainName, 'ns')

    for val in r:
        nameserver=val.to_text()

    # Get the IP_Address of the ANS
    res = dns.resolver.Resolver()
    r = res.resolve(nameserver, 'A')
    for val in r:
        ANS_address=val.to_text()
    print("Found",ANS_address,"in",Address_TLD)
    return(ANS_address)
    

def Authoritative_Name_Server(domainName,ANS_address):
    print("IN.....Authoritative_Name_Server")
    try:
        res = dns.resolver.Resolver(configure=False)
        res.nameservers = [ANS_address]
        r = res.resolve(domainName, 'a')
        for val in r:
            Get_IP=val.to_text()
        print("Found",Get_IP,"in",ANS_address)
        return(Get_IP)
    except:
        return("No Domain Name registered")

Device()