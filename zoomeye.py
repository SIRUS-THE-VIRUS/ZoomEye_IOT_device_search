import requests
import urllib.parse
from tabulate import tabulate

#make it so that you can get the token automatically(input username password and get token
token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZGVudGl0eSI6ImxvdHNwYWNlNjE5QGdtYWlsLmNvbSIsImlhdCI6MTU4ODkxMDk0NCwibmJmIjoxNTg4OTEwOTQ0LCJleHAiOjE1ODg5NTQxNDR9.dn_02gyeZX9JXyZpifRfu8JbabzfjXuSy7nyO8PDWYU"
query = "country:Jamaica&page=1"
host_filters = ["app", 'app:proftd'], ["ver", 'ver:2.1'], ['ip', 'ip:1.1.1.1'], ['service', 'service:http'], \
               ['cidr', '1.2.3.4/21'], ['hostname', 'google.com'], ['port', 'port:53'], ['city', 'city:beijin'], \
               ['country', 'country:china'], ['asn', 'asn:1234'], ['device', 'device:router'], ['os', 'os:windows']

web_filters = [], [], [], [], [], [], [], []

choice = int(input("what are you searching?\n1)host 2) web\n=======>>>>> "))
if choice == 1:
    print(tabulate(host_filters, headers=['Name', 'Description']))
    print("EXAMPLE: country:jamaica +port:8080 +service:http")
    query = input("Enter search string: ")
    encoded_query = urllib.parse.quote_plus(query)
    url = "https://api.zoomeye.org/host/search?query=" + encoded_query + "&page=1"
elif choice == 2:
    print(tabulate(web_filters, headers=['Name', 'Description']))
    print("EXAMPLE: country:jamaica +port:8080 +service:http")
    query = input("Enter search string: ")
    encoded_query = urllib.parse.quote_plus(query)
    url = "https://api.zoomeye.org/web/search?query=" + encoded_query + "&page=1"

#input must look like this below
#country:Jamaica +port:8080
# query = "country:jamaica +port:8080"
# encoded_query = urllib.parse.quote_plus(query)
# print(encoded_query)
# url = "https://api.zoomeye.org/host/search?query=" + encoded_query + "&page=1"
print(url)
response = requests.get(url, headers={"Authorization": "JWT " + token})
print("\n")
json_data = response.json()
#print(json_data)
length = len(json_data["matches"])
print(length)
for i in range(length):
    print(str(i) + ")")
    print("IP Address: " + json_data["matches"][i]["ip"])
    print("Port: " + str(json_data["matches"][i]["portinfo"]["port"]))
    print("App: " + str(json_data["matches"][i]["portinfo"]["app"]))
    print("\n")
