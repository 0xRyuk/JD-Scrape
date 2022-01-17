import sys
import os
import platform

# fancy stuff is here

colors = True  # Output should be colored
machine = sys.platform  # Detecting the os of current system
checkplatform = platform.platform()  # Get current version of OS
if machine.lower().startswith(('os', 'win', 'darwin', 'ios')):
    colors = False  # Colors shouldn't be displayed in mac & windows
if checkplatform.startswith("Windows-10") and int(platform.version().split(".")[2]) >= 10586:
    colors = True
    os.system('')   # Enables the ANSI
if not colors:
    N = R = W = G = Y = run = bad = good = info = que = ''
else:
    N = '\033[0m'
    W = '\033[1;37m'
    B = '\033[1;34m'
    M = '\033[1;35m'
    R = '\033[1;31m'
    G = '\033[1;32m'
    Y = '\033[1;33m'
    C = '\033[1;36m'
    underline = "\033[4m"


banner = Y+"""
     ____.________      _________                                  
    |    |\______ \    /   _____/ ________________  ______   ____  
    |    | |    |  \   \_____  \_/ ___\_  __ \__  \ \____ \_/ __ \ 
/\__|    | |    `   \  /        \  \___|  | \// __ \|  |_> >  ___/ 
\________|/_______  / /_______  /\___  >__|  (____  /   __/ \___  >
                  \/          \/     \/           \/|__|        \/ 
                  %s
                  %s
""" % (R+"{v1.0}"+G, underline+C+"[https://github.com/0xRyuk/JDScrape]"+N+G)+N


epilog = f"""
{Y}Github: {underline}{C}https://www.github.com/0xRyuk{N}
{Y}Version: {R}1.0{N}
"""

about = M+f"""
+───────────────────────+
| {C}Project{N}   : {G}JDScrape{N} {M} |
| {C}License{N}   : {B}MIT{N}       {M}|
| {C}Author{N}    : {R}0xRyuk{N}    {M}|
| {C}Twitter{N}   : {R}0xRyuk{N}    {M}|
+───────────────────────+
"""+N+epilog
