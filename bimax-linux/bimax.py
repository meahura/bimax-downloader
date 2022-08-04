import requests
from sys import argv
from tqdm import tqdm
import socket
import os
from notifypy import Notify

# argv to range 1:1000 and --> string
# download argv input and example --> bimax [link download]

argvS = argv[1:700]

if (str(argvS) =="[]"):
   os.system("clear")
   print(r"""
   .______    __  .___  ___.      ___      ___   ___
   |   _  \  |  | |   \/   |     /   \     \  \ /  /
   |  |_)  | |  | |  \  /  |    /  ^  \     \  V  /
   |   _  <  |  | |  |\/|  |   /  /_\  \     >   <
   |  |_)  | |  | |  |  |  |  /  _____  \   /  .  \
   |______/  |__| |__|  |__| /__/     \__\ /__/ \__\

   [1] - Direct Download v1.01
   [2] - Download Anonymous v1.0.1
   """)
   try:
      NumberS = int(input("enter by number Downloader : "))
      if NumberS == 1:
         url = str(input('enter link : '))
         name = url.split('/')[-1]


         notfiy = Notify()
         notfiy.message = f"Downloading please wait..."
         notfiy.title = name
         notfiy.icon = "direct-download.png"
         notfiy.send()


         respons = requests.get(url,stream=True)
         heead = int(respons.headers['Content-Length'])
         with open(name,'wb') as file:
            for data in tqdm(iterable=respons.iter_content(chunk_size=1024), total=heead / 1024, unit='KB'):
               file.write(data)

      elif NumberS == 2:
         url = str(input('enter link : '))
         name2 = url.split('/')[-1]

         notfiy2= Notify()
         notfiy2.message = f"Downloading please wait..."
         notfiy2.title = name2
         notfiy2.icon = "direct-download.png"
         notfiy2.send()

         ip_addr = socket.gethostname()
         hostname = socket.gethostbyname(ip_addr)
         respons = requests.get(url,stream=True,proxies={hostname:9050})
         heead = int(respons.headers['Content-Length'])

         with open(name2,'wb') as file:
            for data in tqdm(iterable=respons.iter_content(chunk_size=1024), total=heead / 1024, unit='KB'):
               file.write(data)

   except:
      print('error to download...')


else:
   try:

      name = argvS
      for i in name:
         pass
      si = str(i)
      print(si)

      notfiy3 = Notify()
      notfiy3.message = f"Downloading please wait..."
      notfiy3.title = si
      notfiy3.icon = "direct-download.png"
      notfiy3.send()

      respons = requests.get(si,stream=True)
      heead = int(respons.headers['Content-Length'])
      name_main = si.split('/')[-1]
      with open(name_main,'wb') as file:
         for data in tqdm(iterable=respons.iter_content(chunk_size=1024), total=heead / 1024, unit='KB'):
            file.write(data)
   except:
      pass
