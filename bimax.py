import requests
from sys import argv
from tqdm import tqdm
from platform import system ; import socket
import os

# Request permission


# platfrom -> install tor
list_dir_home = os.listdir()
if "safarey.session" not in list_dir_home :
   if system() == "Linux":
      # print("We need to download the tools needed for this tool, we need your access 👇🏻")
      # os.system("sudo apt-get install tor")
      # os.system("tor")
      # os.system("pip install -r requirement.txt")
      # os.system("clear")
      with open("safarey.session" , mode='w') as files:
         files.write(str(requests.get("https://github.com").status_code))
else:
   pass

# argv to range 1:1000 and --> string
# download argv input and example --> bimax [link download]

argvS = argv[1:700]

if (str(argvS) =="[]"):
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
         respons = requests.get(url,stream=True)
         heead = int(respons.headers['Content-Length'])
         with open(name,'wb') as file:
            for data in tqdm(iterable=respons.iter_content(chunk_size=1024), total=heead / 1024, unit='KB'):
               file.write(data)

      elif NumberS == 2:
         url = str(input('enter link : '))
         name = url.split('/')[-1]
         ip_addr = socket.gethostname()
         hostname = socket.gethostbyname(ip_addr)
         respons = requests.get(url,stream=True,proxies={hostname:9050})
         heead = int(respons.headers['Content-Length'])
         with open(name,'wb') as file:
            for data in tqdm(iterable=respons.iter_content(chunk_size=1024), total=heead / 1024, unit='KB'):
               file.write(data)

   except:
      print('error to download...')


else:
   name = argvS
   for i in name:
      pass
   si = str(i)
   print(si)

   respons = requests.get(si,stream=True)
   heead = int(respons.headers['Content-Length'])
   name_main = si.split('/')[-1]
   with open(name_main,'wb') as file:
      for data in tqdm(iterable=respons.iter_content(chunk_size=1024), total=heead / 1024, unit='KB'):
         file.write(data)
