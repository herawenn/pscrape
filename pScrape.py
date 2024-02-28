import os,requests
from ping3 import ping
from colorama import init, Fore

def set_window():
    os.system('mode con cols=75 lines=23')

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

init()
R = Fore.LIGHTRED_EX
G = Fore.LIGHTGREEN_EX
Y = Fore.YELLOW
B = Fore.LIGHTBLUE_EX
P = Fore.LIGHTMAGENTA_EX
C = Fore.LIGHTCYAN_EX
X = Fore.RESET

def scrape_proxies(api_key, protocol='socks5'):

    api_url = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol={protocol}&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true'

    headers = {'Authorization': f'Bearer {api_key}'}

    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        proxies = response.text.split('\r\n')

        # Remove empty lines
        proxies = list(filter(lambda proxy: len(proxy) > 0, proxies))

        # Return list of proxies
        return proxies
    else:
        print(f" {R}Error{X}: Unable to fetch proxies. Status Code: {Y}{response.status_code}{X}")
        return None

# Function to check the status of a proxy using ping
def check_proxy_status(proxy):
    try:
        result = ping(proxy, timeout=1, unit='ms')
        if result is not None:
            return G + 'Online' + X
        else:
            return R + 'Offline' + X
    except TimeoutError:
        return Y + 'Timeout' + X

print(f"{Y}       {G}___ {X}                                    ")
print(f"{Y} _ __ {G}/ __|{R} __ {P}_ _{B} __ _{C} _ __ {G} ___  ")
print(f"{Y}| '_ \{G}\\__ \{R}/ _|{P} '_{B}/ _` {C}| '_ \{G}/ -_)")
print(f"{Y}| .__/{G}|___/{R}\__|{P}_| {B}\__,_{C}| .__/{G}\___| ")
print(f"{Y}|_|                    {C}|_|{G}H{Y}e{R}r{P}a{B}w{C}e{G}n{X}")
print("")
protocol = input(f'HTTP {Y}/{X} SOCKS4 {Y}/{X} SOCKS5 {Y}/{X} ALL{Y}:{X} ')

your_api_key = 'api_key'
proxies_list = scrape_proxies(api_key=your_api_key, protocol=protocol)

if proxies_list:
    total_proxies = len(proxies_list)
    live_proxies = 0

if proxies_list:
    print(f"\nProxies: ")
    for proxy in proxies_list:
        status = check_proxy_status(proxy)
        print(f" {G}{proxy}{X} - {Y}{status}{X}")

        if 'Online' in status:
            live_proxies += 1

    file_name = f'{protocol}.txt'
    with open(file_name, 'w') as file:
        for proxy in proxies_list:
            status = check_proxy_status(proxy)
            file.write(f'{proxy}\n')

    clear_console()
    print(f"\nScraping Complete{Y}!{X}\n Saved {Y}{total_proxies}{X} proxies to {Y}{file_name}{X}")
else:
    print(f"\n{R}Error!{X} Please try again.")