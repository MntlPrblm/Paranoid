#imports
import os
import time
import sys
import socket
import netifaces
import platform
import phonenumbers
import webbrowser
import threading
import requests
#from imports
from scapy.all import ARP, Ether, srp
from datetime import date
from colorama import Fore
from phonenumbers import geocoder, carrier, timezone
from ip2geotools.databases.noncommercial import DbIpCity

#pre variable setting
help = """
phonecheck: does OSINT on phonenumber
help: shows help screen
websitecheck: checks response to a url
exit: exits
networkscan: scans network for devices
clear: clears the screen
"""
light_blue = Fore.LIGHTCYAN_EX
blue = Fore.LIGHTBLUE_EX
magenta = Fore.LIGHTMAGENTA_EX
white = Fore.LIGHTWHITE_EX
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX

networktitle = """
 _      _     ____  ____    ____  _        _     ___  _   _      _____ _____  _      ____  ____  _  __
/ \  /|/ \ /|/  _ \/ ___\  /  _ \/ \  /|  / \__/|\  \//  / \  /|/  __//__ __\/ \  /|/  _ \/  __\/ |/ /
| |  ||| |_||| / \||    \  | / \|| |\ ||  | |\/|| \  /   | |\ |||  \    / \  | |  ||| / \||  \/||   / 
| |/\||| | ||| \_/|\___ |  | \_/|| | \||  | |  || / /    | | \|||  /_   | |  | |/\||| \_/||    /|   \ 
\_/  \|\_/ \|\____/\____/  \____/\_/  \|  \_/  \|/_/     \_/  \|\____\  \_/  \_/  \|\____/\_/\_\\_|\_\
"""

titlescreen = """
 (                                           
 )\ )                                  (     
(()/(    )  (       )             (    )\ )  
 /(_))( /(  )(   ( /(   (      (  )\  (()/(  
(_))  )(_))(()\  )(_))  )\ )   )\((_)  ((_)) 
| _ \((_)_  ((_)((_)_  _(_/(  ((_)(_)  _| |  
|  _// _` || '_|/ _` || ' \))/ _ \| |/ _` |  
|_|  \__,_||_|  \__,_||_||_| \___/|_|\__,_|  
This shit might scare someone, github.com/MntlPrblm
"""

phonechecktitle = """
   ___ _                        ___ _               _    
  / _ \ |__   ___  _ __   ___  / __\ |__   ___  ___| | __
 / /_)/ '_ \ / _ \| '_ \ / _ \/ /  | '_ \ / _ \/ __| |/ /
/ ___/| | | | (_) | | | |  __/ /___| | | |  __/ (__|   < 
\/    |_| |_|\___/|_| |_|\___\____/|_| |_|\___|\___|_|\_|
          Who the hell keeps texting me?????
"""

#functions---------------------------------------------------
def clear():
    if os.name == "posix":
        _ = os.system('clear')
    else:
        _ = os.system('cls')

#scans network for devices
def network_scan():
    print(magenta+networktitle)
    gateways = netifaces.gateways()
    local_ip = gateways['default'][netifaces.AF_INET][0]
    print(white+"scanning "+local_ip)
    #create ARP packet
    arp = ARP(pdst=local_ip+"/24")
    #create Ether destination
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    #creates packet
    packet = ether/arp
    result = srp(packet, timeout=3)[0]
    #client list
    clients = []
    for sent, received in result:
        clients.append({'ip': received.psrc, 'mac': received.hwsrc})
    # print clients
    print("Available devices in the network:")
    print("IP" + " "*18+"MAC")
    for client in clients:
        print("{:16}    {}".format(client['ip'], client['mac']))
    start()

#check https: website
def websitecheck():
    website = input("Website: ")
    print("checking website")
    try:
        response = requests.get(website)
        print(response)
        print("website is up")
    except:
        print("website is down")
    start()

#does OSINT on phonenumber
def phonecheck():
    clear()
    print(magenta+phonechecktitle)
    pn = input("Phone number with country code, ex: +1: ")
    clear()
    print(Fore.LIGHTGREEN_EX+"checking phone number...")
    time.sleep(1)
    clear()
    try:
        z = phonenumbers.parse(pn, None)
    except:
        print("Please add country code, ex: +1")
        time.sleep(2)
        start()
    print(z)
    real_number = phonenumbers.is_possible_number(z)
    if real_number == True:
        print(Fore.LIGHTWHITE_EX+"Number has NPA 200, aka Real number")
    else:
        print("NPA not found, not real number")
    location = geocoder.description_for_number(z, "en")
    print("Location: "+location)
    ro_number = phonenumbers.parse(pn, "RO")
    OGcarrier = carrier.name_for_number(ro_number, "en")
    print("Original carrier: "+OGcarrier)
    gb_number = phonenumbers.parse(pn, "GB")
    time_zone = timezone.time_zones_for_number(gb_number)
    print("Timezone: "+str(time_zone))
    print("===========================")
    print("Open OSINT websites? Y OR N")
    print("===========================")
    phone_osint = input("Y or N: ")
    if phone_osint == "y":
        webbrowser.open("https://thatsthem.com/")
        webbrowser.open("https://www.usphonebook.com/")
        webbrowser.open("https://freecarrierlookup.com/")
        webbrowser.open("https://www.truepeoplesearch.com/")
    start()

def library():
    clear()
    try:
        os.chdir("./library")
    except FileNotFoundError:
        print("Welcome to the library, keep your notes here!")
    print(magenta+"Creating a file requires a restart of script")
    print(light_blue+"================")
    print(white+"[1] show entries")
    print("[2] make entry")
    print("[3] read entry")
    print("[0] exit")
    print(light_blue+"================")
    print("")
    library_in = input(Fore.WHITE+"Library input: ")
    if library_in == "0":
        os.chdir("../")
        start()
    if library_in == "1":
        path = os.getcwd()
        dir_list = os.listdir(path)
        # prints all files
        print("------------------")
        print(dir_list)
        print("------------------")
        input("Press enter to continue")
        library()
    if library_in == "2":
        today = date.today()
        filename = input("Filename with .txt: ")
        content = input("Content in file: ")
        f = open(filename, "w")
        f.write(content)
        f.close
        library()
    if library_in == "3":
        path = os.getcwd()
        dir_list = os.listdir(path)
        # prints all files
        print("------------------")
        print(dir_list)
        print("------------------")
        file_to_read = input("File to read: ")
        if os.path.exists(file_to_read) == True:
            with open(file_to_read, 'r') as f:
                print(f.read())
        print("=======================")
        input("press enter to continue")
        library()
        
#pre script commands--------------------------------------------------------------
clear()
print(magenta+titlescreen)
time.sleep(2)
if os.path.exists("./library"):
    print("Found library directory")
else:
    os.makedirs("library")

#start screen---------------------------------------------------------------------
def start():
    print(white+"==============================================")
    print(light_blue+"I think im Paranoid! And complicated...")
    print(white+"==============================================")
    user_in = input("Input: ")
    if user_in == "help":
        print(light_blue+help)
        start()
    if user_in == "phonecheck":
        phonecheck()
    if user_in == "websitecheck":
        websitecheck()
    if user_in == "exit":
        sys.exit()
    if user_in == "networkscan":
        if os.name == "posix":
            print("This scan only works for windows")
            time.sleep(2)
            start()
        else:
            network_scan()
    if user_in == "clear":
        clear()
        start()
    if user_in == "library":
        library()

if __name__=="__main__":
    start()
