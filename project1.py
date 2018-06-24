#!/usr/bin/python
import commands,time,webbrowser,platform
n=raw_input("enter name")
print n
print type(n)



option='''
no 1 if cable is connected
no 2 if internet is connected
no 3 if there is google access
'''

print option


choice=raw_input()

if choice== "1" :

	print "please wait checking if cable is connected" 
	time.sleep(2)
	
	plat_sys=platform.system() #gives the os version
	
	if 'linux' in plat_sys:
		cable_check=commands.getoutput('mii-tool p8p1')
	
	else:
		cable_check=commands.getoutput('sudo mii-tool p8p1')
			
	if 'link ok' in cable_check:
		print"lan is connected "
	else:
		print "lan is not connected"
		time.sleep(3)
		print "checking if wifi is connected"
		wifi_check=commands.getoutput('iw dev wlp2s0 link')#gives the wifi name and details
		print wifi_check
	
	
				
elif choice== "2" :
		print "plz wait checking if internet is connected"
		time.sleep(3)
		commands.getoutput('ping 8.8.8.8 -c 4')#checks connection with google.com
		
		
elif choice== "3" :
		print "loading google web page"
		time.sleep(2)
		brow_access=webbrowser.open_new_tab("http://www.google.com")
	
		
else :
	print "wrong choice"
		
	print "wrong option"

