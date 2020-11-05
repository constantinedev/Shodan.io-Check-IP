import os, sys, socket, arrow, shodan, requests
import shodan.helpers as helpers

API_KEY = '<<INPUT YOUR API KEY HERE>>'
domain = input("target domain:")

checkip = socket.gethostbyname(domain)

print (f'The "{domain}" IP Addr is {socket.gethostbyname(domain)}')

site1 = "https://exploits.shodan.io/shodan/host/" + checkip + "?key=" + API_KEY
site2 = "https://exploits.shodan.io/api/count?query=" + domain + "&key=" + API_KEY

resut1 = requests.get(site1).text
resut2 = requests.get(site2).text

print (resut1)
print (resut2)
