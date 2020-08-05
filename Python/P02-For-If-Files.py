Router_List=["RA","RB","RC"]

#print (Router_List)

for item in Router_List:
    if item == "RA":
        print (item)

#####################

with open("IP_List.txt","r+") as File:
    print (File.read())

#####################


with open("IP_List.txt","r+") as File:
    File=(File.readlines())
    print (File)

#####################

IP_List=[]
with open("IP_List.txt","r+") as File:
    for line in File:
        line = line.strip()
        if line:
            IP_List.append(line)
print(IP_List)

#####################

Config_Set1=[]
with open("Config_F1.txt","r+") as File:
    for line in File:
        line = line.strip()
        if line:
            print (line)
            Config_Set1.append(line)
print(Config_Set1)

#####################


Hosts=[]
for i in range(1,10):
    Hosts.append("192.168.1." + str(i))
print (Hosts)

#####################

Hosts =  ["192.168.1." + str(i) for i in range (1, 10)]
print (Hosts)

#####################

with open("Config_F2.txt","r+") as File:
    for i in range(1,10):
        File.write("192.168.1." + str(i) + "\n")

#####################


with open("Config_F3.txt","w+") as File:
    Hosts =  ["192.168.1." + str(i) for i in range (1, 10)]
    File.writelines("\n".join(Hosts))


