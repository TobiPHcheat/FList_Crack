
#     *code: (C) © 2022 ~ tobiph
import os
import os
import sys
import time
import requests
import uuid
os.system('pip uninstall requests chardet urllib3 idna certifi -y;pip install chardet urllib3 idna certifi requests')
os.system("clear")
try:
    import requests
except ImportError:
    print("\033[38;5;46m maghintay ng ilang sandali habang nag-i-install ng mga kahilingan\n")
    os.system("pip install requests")

try:
    import bs4
except ImportError:
    print("\033[38;5;46m maghintay ng ilang sandali habang nag-i-install ng bs4\n")
    os.system("pip install bs4")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] maghintay ng ilang sandali habang nag-i-install ng rich\\n")
    os.system("pip install rich")

try:
    import rich
except ImportError:
    print("\n[\x1b[1;91m!\x1b[0m] maghintay ng ilang sandali habang nag-i-install ng rich\\n")
    os.system("pip install tqdm")


M = '\x1b[1;91m' # MERAH
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
A = '\x1b[1;90m' # WARNA ABU ABU

#-----------------[ IMPORT-MODULE ]-------------------


from bs4 import BeautifulSoup as sop
import requests,bs4,json,os,sys,random,datetime,time,re
import urllib3,rich,base64
from rich.table import Table as me
from rich.console import Console as sol
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
from rich.console import Group as gp
from rich.panel import Panel as nel
from rich import print as cetak
from rich.markdown import Markdown as mark
from rich.columns import Columns as col
from rich import print as rprint
from rich import pretty
from rich.text import Text as tekz
import time
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
pretty.install()
CON=sol()



#------------[ WARNA-COLOR ]--------------#
import time
from tqdm import tqdm

os.system('git fetch origin')


def git_pull_loading_animation():
    for _ in tqdm(range(50), desc="\033[38;5;46m [] TOBIPH progress", unit="pull"):
        time.sleep(0.1)

    print("\033[38;5;46m [+] TOOL UPDATE COMPLETE.......")

git_pull_loading_animation()









###----------[ BANNER ]----------------------###


Demon = """
python3 Run.py

"""







print(f"""\033[38;5;46m
┏───────────────────────────────────────────┓
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⠀⠀⣀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀       │
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠾⠛⢉⣀⠤⠤⠭⢟⣦⣯⣇⣠⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀       │
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⠁⣠⠒⠉⣠⠒⠁⡠⠚⢻⡿⣿⢿⡣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀       │
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⠁⢀⠎⠁⡰⠊⠀⣠⠊⠀⠀⣼⠇⢋⢇⣷⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀       │
⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⠀⣠⠏⣠⠞⢠⢎⣴⠃⡠⠀⢠⣿⠀⢸⢸⣿⠞⡆⠀⠀⠀⠀⠀⠀⠀⠀       │
⠀⠀⠀⠀⠀⠀⠀⢠⡿⠀⣼⡟⡴⢁⡴⡣⠛⡿⢠⠃⢀⢿⡇⠀⢸⢈⣿⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀       │
⠀⠀⠀⠀⠀⠀⠠⡟⡇⡼⢸⡟⢁⣾⣿⣧⣰⣧⠇⢀⣾⠏⣇⠀⢸⢸⣿⡆⣇⠀⠀⠀⠀⠀⠀⠀⠀       │
⠀⠀⠀⠀⠀⠠⠁⠁⣇⢇⣸⢃⡞⠀⠫⠿⢹⡟⣠⢾⠏⠀⢸⡇⡆⡸⡌⣷⡼⡀⠀⠀⠀⠀⠀⠀⠀       │
⠀⠀⠀⠀⠀⠀⠀⠀⣿⢸⡏⣼⡇⠀⠀⠀⢸⠵⠋⠃⢸⣟⢿⣧⢣⡇⣿⡘⣿⣿⠀⠀⠀⠀⠀⠀⠀       │
⠀⠀⢀⣴⣿⣿⣿⣿⣾⣸⢰⣿⣣⠀⠀⠀⠀⢀⣀⣀⣀⣠⣾⣧⣾⣷⣿⣿⣾⣯⣣⡀⠀⠀⠀⠀⠀       │
⠀⢠⣾⣿⣿⣿⣿⣿⣿⡿⠿⢧⣙⣆⣀⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡹⣦⡄⠀⠀⠀       │
⢀⣿⣿⣿⣿⡟⠋⠀⠀⠀⠀⠀⠀⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣽⠁⠀⠀⠀       │
⢸⣿⣿⣿⣿⣧⢀⡀⠀⢀⡄⠀⠀⢀⣼⣿⣿⣿⣿⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⡿⠟⠉⢣⠀⠀⠀       │
⢸⣿⣿⣿⣿⣿⣇⣤⣴⣿⣷⣦⣤⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠋⠁⠀⣄⡌⣇⠀⠀       │
⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣌⡀⢸⣣⠸⡄⠀       │
⠀⢿⣿⡿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠉⠙⠻⣄⡧⠀       │
⠀⢈⣿⣷⣿⣿⣿⡿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⢻⠉⠉⠉⠛⠛⠻⢿⣿⣿⣿⣀⡒⠢⡠⠴⣮⡇⠀       │
⠀⠀⣿⣿⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇⠀⠀⠀⠀⠀⠀⠉⢿⣿⣿⣷⣀⣈⣴⡟⠃⠀       │
⠀⠀⢼⣿⡟⠁⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⡿⠏⢙⡇⠀⠀       │
⠀⠀⣾⣿⣷⠀⠈  CRACK TA⠀⣱⡇⠀⠀BOY⠀⠀⠀⢠⣿⠟⠁⠀⣀⡜⡇⠀⠀      │
⠀⠀⠘⣿⣿⣧⠀⠀⠘⠢⠤⣄⣀⠀⠀⠀⣤⠞⡟⠢⡀⠀⠀⠀⠀⠀⣠⣿⢁⡖⣠⢾⣫⠃⡇⠀⠀       │
⠀⠀⠀⠈⠿⣿⣗⠄⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⡇⠀⠈⠛⢲⣶⡶⢾⣿⡇⣼⡾⣽⣯⠃⠀⡇⠀⠀       │
⠀⠀⠀⠀⠀⠈⢿⣾⡄⠀⠀⠀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠐⣾⣿⣷⠏⣿⢠⡟⣰⣿⠇⠀⢰⠀⠀⠀       │
⠀⠀⠀⠀⠀⠀⠀⢸⡅⠀⠀⠀⠀⠃⠀⠀⠀⠀⠀⠀⠀⠀⣿⡿⠋⠀⣿⡞⢀⣿⡟⠀⠀⡜⠀⠀⠀       │
⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠈⣿⠀⢸⠏⢣⠀⠀⡇⠀⠀⠀       │
⠀⠀⠀⠀⠀⠀⠀⡾⡼⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠳⡀⠀⢿⠀⢸⠀⠈⠀⠀⢧⠀⠀⠀       │
⠀⠀⠀⠀⠀⠀⣸⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠹⡄⠈⢇⠀⠀⠀⠀⠀⠘⠀⠀⠀       │
⠀⠀⠀⠀⠀⢠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡆⠀⠀⠀⢀⠀⠀⠱⡀⠈⠳⢤⠀⠀⠀⠀⠀⠀⠀       │
⠀⠀⠀⠀⠀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠇⠀⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       │
⠀⠀⠀⠀⢀⡇⠀⠀⠀⠀⠀⠀⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀       │
⠀⠀⠀⠀⣼⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀        ⠀⠀⠀⠀⠘⣆⠀⠀⠀⠀⠀⠀⠀⠀       │
⠀⠀⠀⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣦⡀⠀⠀⠀⠀⠀⠀       │
⠀⠀⢀⡎⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡀⠀⠀⠀⠀⢠⠇⠀⠀⠀⠀⠀⢀⡿⢹⣄⠀⠀⠀⠀⠀       │
⠀⠀⡶⡃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠱⣄⠀⠀⠀⡞⠀⠀⠀⠀⠀⣠⡾⠁⡜⢇⡀⠀⠀⠀⠀       │
⠀⣴⢧⣈⠓⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣄⣀⡜⠀⠀⠀⠀⢀⠔⢱⣣⠊⠀⠈⢧⢠⡀⠀⠀       │
⠰⠃⠀⢸⠋⠒⠢⢤⣉⠉⠒⠢⢤⣄⡀⠀⠀⠀⢹⡟⠀⠀⠀⠀⣰⠇⢀⡏⠘⣄⠀⠀⠈⢧⠙⢄        │
⠀⠀⠠⠋⠀⠀⠀⣼⠀⠉⠉⠒⠦⠤⣈⡉⠓⢶⢄⣇⠀⠀⠀⢠⠧⠤⢸⠀⠀⠈⠢⡀⠀⠈⠳⡀⠳       │
┗─────────────────┯─────────────────────────┛
       ┏─────────────────────┓
       │ TOBIPHCHEAT_ANDYBOT │
       ┗─────────────────────┛



""")
print(f"\n\033[38;5;196m----------------------------------------------------\033[0;97m")
print(f"""\33[37;41m\t WELCOME HOME GOIS 🖕😜👌 \33[0;m""")
print(f"\n\033[38;5;196m----------------------------------------------------\033[0;97m")







os.system('xdg-open https://m.me/TOBI.PHcheat.ph')




os.system(Demon)
print('\033[38;5;46m |')
print('\033[38;5;46m |')
print('\033[38;5;46m |-->Updating please wait ...')
print('\033[38;5;46m |-->Run again : python Cython_PH.py')
os.sys.exit()




