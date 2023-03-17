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
import urllib.request
import requests
import re
import json
#from imports
from hashlib import md5
from urllib.request import urlopen, hashlib
from scapy.all import ARP, Ether, srp
from datetime import date
from colorama import Fore
from time import sleep
from datetime import datetime
from phonenumbers import geocoder, carrier, timezone

#pre variable setting
help = """
phonecheck: does OSINT on phonenumber
help: shows help screen
websitecheck: checks response to a url
exit: exits
networkscan: scans network for devices
clear: clears the screen
ping: pings IP address
iptrack: geolocates IP address
drillbit: does OSINT on person based on their name and city
proxyscrape: provides list or usable proxies
wordlistcheck: checks to see if string is in wordlist
portscan: scans IP address for ports
library: Opens library to take notes
default: prints default gateway
hashcracker: a hashcracker for low hanging fruit
"""
light_blue = Fore.LIGHTCYAN_EX
blue = Fore.LIGHTBLUE_EX
magenta = Fore.LIGHTMAGENTA_EX
white = Fore.LIGHTWHITE_EX
green = Fore.LIGHTGREEN_EX
red = Fore.LIGHTRED_EX

hashcracker_title = """
    __  __           __    ______                __            
   / / / /___ ______/ /_  / ____/________ ______/ /_____  _____
  / /_/ / __ `/ ___/ __ \/ /   / ___/ __ `/ ___/ //_/ _ \/ ___/
 / __  / /_/ (__  ) / / / /___/ /  / /_/ / /__/ ,< /  __/ /    
/_/ /_/\__,_/____/_/ /_/\____/_/   \__,_/\___/_/|_|\___/_/     
No password is safe...   
"""

networktitle = """
 _      _     ____  ____    ____  _        _     ___  _   _      _____ _____  _      ____  ____  _  __
/ \  /|/ \ /|/  _ \/ ___\  /  _ \/ \  /|  / \__/|\  \//  / \  /|/  __//__ __\/ \  /|/  _ \/  __\/ |/ /
| |  ||| |_||| / \||    \  | / \|| |\ ||  | |\/|| \  /   | |\ |||  \    / \  | |  ||| / \||  \/||   / 
| |/\||| | ||| \_/|\___ |  | \_/|| | \||  | |  || / /    | | \|||  /_   | |  | |/\||| \_/||    /|   \ 
\_/  \|\_/ \|\____/\____/  \____/\_/  \|  \_/  \|/_/     \_/  \|\____\  \_/  \_/  \|\____/\_/\_\\_|\_\
We will find everyone!
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

#HASH CRACKING===============================================
def hashcracker():
    print(magenta+hashcracker_title)
    hash_input = input(white+"Please input hash\n>")
    hash_input = hash_input.lower()
    hash_type = input("Please enter hash type\n>")
    hash_type = hash_type.lower()
    if hash_type == "md5":
        md5crack(hash_input)
    if hash_type == "sha1":
        sha1crack(hash_input)
    if hash_type == "sha224":
        sha224crack(hash_input)
    if hash_type == "sha256":
        sha256crack(hash_input)
    if hash_type == "sha384":
        sha384crack(hash_input)
    if hash_type == "sha512":
        sha512crack(hash_input)
    if hash_type == "blake2b":
        blake2bcrack(hash_input)
    if hash_type == "blake2s":
        blake2scrack(hash_input)
    if hash_type == "sha3_224":
        sha3_224crack(hash_input)
    if hash_type == "sha3_256":
        sha3_256crack(hash_input)
    if hash_type == "sha3_384":
        sha3_384crack(hash_input)
    if hash_type == "sha3_512":
        sha3_512crack(hash_input)
    if hash_type == "shake_128":
        shake_128crack(hash_input)
    if hash_type == "shake_256":
        shake_256crack(hash_input)
    else:
        screen_clear()
        print("Please only enter hashes that are: sha1, sha224, sha256, sha384, sha512, blake2b, blake2s, md5, sha3_224, sha3_256, sha3_384, sha3_512, shake_128, or shake_256")
        time.sleep(3)
        hashcracker()


#url containing wordlist
url_wordlist = 'https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Common-Credentials/10-million-password-list-top-10000.txt'

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')

def md5crack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.md5(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
           print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#sha224 crack
def sha224crack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha224(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
           print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#sha1 crack
def sha1crack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha1(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
            print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#sha256 crack
def sha256crack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha256(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
            print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#sha384 crack
def sha384crack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha384(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
            print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#sha512 crack
def sha512crack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha512(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
            print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#blake2b crack
def blake2bcrack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.blake2b(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
            print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#blake2s crack
def blake2scrack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.blake2s(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
            print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#sha3_224 crack
def sha3_224crack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha3_224(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
            print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#sha3_256 crack
def sha3_256crack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha3_256(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
            print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#sha3_384 crack
def sha3_384crack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha3_384(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
            print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#sha3_512 crack
def sha3_512crack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.sha3_512(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
            print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#shake_128 crack
def shake_128crack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.shake_128(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
            print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#shake_256 crack
def shake_256crack(hash):
    LIST_OF_COMMON_PASSWORDS = str(urlopen(url_wordlist).read(), 'utf-8')
    for guess in LIST_OF_COMMON_PASSWORDS.split('\n'):
        hashedGuess = hashlib.shake_256(bytes(guess, 'utf-8')).hexdigest()
        if hashedGuess == hash:
            screen_clear()
            print("The password is:", str(guess))
            start()
        elif hashedGuess != hash:
            print("Password guess ",str(guess)," does not match, trying next...")
    screen_clear()
    print("Password not in database, we'll get them next time.")
    start()

#=============================================================

#default gateway finder
def default_gateway():
    gateways = netifaces.gateways()
    default_gateway = gateways['default'][netifaces.AF_INET][0]
    print(default_gateway)
    start()

#port scanner made by david bombal
def portscan():
    print("==============================================")
    print(light_blue+"All credits to David Bombal! Hell of a hacker!")
    print(green+"https://github.com/davidbombal/red-python-scripts/blob/main/port_scanner_regex.py")
    print(white+"==============================================")
    ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    port_range_pattern = re.compile("([0-9]+)-([0-9]+)")
    port_min = 0
    port_max = 65535
    open_ports = []
    while True:
        ip_add_entered = input(white+"\nTarget IP address: ")
        if ip_add_pattern.search(ip_add_entered):
            print(f"{ip_add_entered} IP address Valid")
            break
    while True:
        print("Please enter port range, ex: 22-80")
        port_range = input("Enter port range: ")
        print("Scanning...")
        port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
        if port_range_valid:
            port_min = int(port_range_valid.group(1))
            port_max = int(port_range_valid.group(2))
            break
    for port in range(port_min, port_max + 1):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                s.connect((ip_add_entered, port))
                open_ports.append(port)
        except:
            pass
    for port in open_ports:
        print(green+f"Port {port} is open on {ip_add_entered}.")
    start()

#checks to see if string is in wordlist
def wordlistcheck():
    users_password = input("Please enter password to check: ")
    wordlist = input("Enter path to wordlist: ")
    if os.path.exists(wordlist) == False:
        clear()
        print("Wordlist not found")
        time.sleep(3)
        wordlistcheck()
    f = open(wordlist, "r", encoding="ISO-8859-1")
    wordlist = f.read().splitlines()
    f.close()
    print("Checking...")
    for password in wordlist:
        if password == users_password:
            print("Password in wordlist")
            input("Press enter to continue")
            start()
    print("Password not in wordlist")
    start()


#proxy scraping
def proxy_scrape():
    print("Scraping https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt")
    time.sleep(2)
    website = "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt"
    response = requests.get(website)
    data = response.text
    print(data)
    start()

#name to location
def drillbit():
    first_name = input("First name: ")
    last_name = input("last name: ")
    state = input("State abbreviated: ")
    city = input("City: ")
    city = city.replace(' ','-')
    webbrowser.open("https://www.beenverified.com/people/"+first_name+"-"+last_name+"/"+state+"/"+city)
    start()

#ip geolocator
def get_location():
    ip_address = input("Victim IP address: ")
    response = requests.get(f'https://ipapi.co/{ip_address}/json/').json()
    location_data = {
        "ip": ip_address,
        "city": response.get("city"),
        "region": response.get("region"),
        "country": response.get("country_name")
    }
    print(location_data)
    start()

#pings ip address, fully cross platform
def ping(host):
    """
    Returns True if host responds to a ping request
    """
    import subprocess, platform

    # Ping parameters as function of OS
    ping_str = "-n 1" if  platform.system().lower()=="windows" else "-c 1"
    args = "ping " + " " + ping_str + " " + host
    need_sh = False if  platform.system().lower()=="windows" else True

    # Ping
    return subprocess.call(args, shell=need_sh) == 0
    
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
    if user_in == "ping":
        ip = input("IP address: ")
        print(ping(ip))
        start()
    if user_in == "iptrack":
        get_location()
    if user_in == "drillbit":
        drillbit()
    if user_in == "proxyscrape":
        proxy_scrape()
    if user_in == "wordlistcheck":
        wordlistcheck()
    if user_in == "portscan":
        portscan()
    if user_in == "default":
        default_gateway()
    if user_in == "hashcracker":
        hashcracker()
    if user_in == "instadata":
        instadata()
    

    print("Invalid command")
    time.sleep(2)
    start()



if __name__=="__main__":
    start()
