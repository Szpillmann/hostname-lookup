import os
import re

with open("ip_list.txt") as file:
    park = file.read()
    park = park.splitlines()
    print(" {park}  \n")
    # ping for each ip in the file
for ip in park:
    response = os.popen(f"ping -n 1 {ip} ").read()
    #saving some ping output details to output file
    if("Ping request could not find host" or "Request timed out." or "unreachable") in response:
        print(response)
        f = open("ip_output.txt","a")
        f.write(response)
        f.close() 
    else:
        print(response)
        x = re.search(r'(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', response)
        f = open("ip_output.txt","a") 
        f.write(ip+' is up '+x.group()+'\n')
        f.close() 
    # print output file to screen
with open("ip_output.txt") as file:
    output = file.read()
    f.close()
    print(output)
#with open("ip_output.txt","w") as file:
#    pass
#te va a borrar todo despues de guardarlo