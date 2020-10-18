import time
from pprint import pprint
import nmap
import sys
nm_scan = nmap.PortScanner()
print("\nRunning...\n")
nm_scanner = nm_scan.scan(sys.argv[1],'80',arguments = '-O') #O is for OS fingerprinting , 80 is the port we are going to scan, argv[1] is the IP add we take from user
#pprint(nm_scanner)		#we want state of host, port, method of scanning
host_is_up = "The state of the host is: " + nm_scanner['scan'][sys.argv[1]]['status']['state']+".\n"
port_open = "The state of the port is: " + nm_scanner['scan'][sys.argv[1]]['tcp'][80]['state']+".\n"
method_scan = "The scan type is: " + nm_scanner['scan'][sys.argv[1]]['tcp'][80]['reason']+".\n"
guessed_os = "There is %s chance that the host is running %s "%(nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['accuracy'],nm_scanner['scan'][sys.argv[1]]['osmatch'][0]['name'])+".\n"
with open("%s.txt"%sys.argv[1],'w') as f:
	f.write(host_is_up+port_open+method_scan+guessed_os)
	f.write("\nReport generated at: "+time.strftime("%Y-%m-%d_%H:%M:%S IST"))
print("\nFinished...")