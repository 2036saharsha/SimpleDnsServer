import dns.resolver
#for RNS

# result = dns.resolver.query('c.gtld-servers.net.', 'A')
# for val in result:
#     print('NS Record : ', val.to_text())


# res = dns.resolver.Resolver(configure=False)
# res.nameservers = ['192.26.92.30']
# r = res.query('ns1.google.com', 'a')
# nameservers = [ns.to_text() for ns in r]
# print(nameservers)


# suffix="com"
# result = dns.resolver.query(suffix, 'NS')

# for val in result:
#     if (val.to_text()[:1]) == suffix[:1]:
#         Name_server=val.to_text()
#         print(Name_server)

# res = dns.resolver.Resolver(configure=False)
# res.nameservers = ["192.26.92.30"]
# r = res.query("google.com", 'ns')
# nameservers = [ns.to_text() for ns in r]
# print(nameservers[0])



try:
    # res = dns.resolver.Resolver(configure=False)
    # res.nameservers = [ANS_address]
    r = dns.resolver.query("youtube.com", 'A')
    Get_IP = [ns.to_text() for ns in r]
    print(Get_IP[0])
except:
    print("No Domain Name registered")