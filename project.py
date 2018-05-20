#!usr/bin/python2

import datetime
import webbrowser
import urllib2
from BeautifulSoup import BeautifulSoup
import re
import requests
from bs4 import BeautifulSoup


opt='''
press 1 :Search every keyword in browser
press 2 :Search images for every keyword in browser
press 3 :Search URl for Websites
press 4 :Print current Date and time of system
press 5 :Check and Open default WEB BROWSER
press 6 :Print Network IPs of all machines
press 7 :Check name and Info of Domain owner
''' 
print (opt)
ch=raw_input()



if ch=='1':
   search_data=raw_input("Enter Data: ")
   final_data=search_data.strip()
   #removing leading and trailing spaces
   done_data=final_data.split()
   for i in done_data:
         webbrowser.open_new_tab('https://www.google.com/search?q='+i)  #to open web browser search results

if ch=='2':
      search_data=raw_input("Enter Data: ")
      final_data=search_data.strip()
      #removing leading and trailing spaces
      done_data=final_data.split()
      for i in done_data:
           webbrowser.open_new_tab('https://www.google.co.in/search?tbm=isch&source=hp&biw=1301&bih=670&ei=4E38WtahBNee9QP-74moAg&q='+i)  
      #to open web browser image search results
         
if ch=='3':
      search_data=raw_input("Enter Data: ")
      final_data=search_data.strip()
      #removing leading and trailing spaces
      page = requests.get("https://www.google.dz/search?q="+final_data)
      soup = BeautifulSoup(page.content)
      links = soup.findAll("a")
      for link in  soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
           print re.split(":(?=http)",link["href"].replace("/url?q=",""))
           print ("")
if ch=='4':
    date_time=datetime.datetime.now()
    print ("Current Date and Time:"+date_time)  #to print system current date and time


