import shodan, os

API_KEY = "YOUR API HERE"

api=shodan.Shodan(API_KEY)
fl=open('ips.txt','w+')
try:
	results = api.search('apache')
	print("Total results found: \t" + str(results["total"]))
	for result in results['matches']:
		print("IP:==========\t" + result["ip_str"])
		fl.write(result["ip_str"]+"\n")
		print("")
except shodan.APIError as e:
	print("Error is "+e)

fl.close()

del fl

fl=open('ips.txt','r+')

lins=fl.readlines()

print(type(lins))
for i in lins:
	hostname = i
	response = os.system("ping -c 1 " + hostname)
	if response == 0:
		print(hostname + " is DOWN!!!")
	else:
		print(hostname + " is UP...")


fl.close()
