import os
import aiohttp
import asyncio
import logging
from tqdm.asyncio import tqdm
from colorama import init, Fore

init()
Y = Fore.YELLOW
X = Fore.RESET

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')

# List of proxy URLs
proxies_urls = {
    "socks4": [
        "https://www.proxy-list.download/api/v1/get?type=socks4",
        "https://www.proxyscan.io/download?type=socks4",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks4.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt",
        "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks4.txt"
    ],
    "socks5": [
        "https://www.proxy-list.download/api/v1/get?type=socks5",
        "https://www.proxyscan.io/download?type=socks5",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks5.txt",
        "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks5.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-socks5.txt",
        "https://api.openproxylist.xyz/socks5.txt",
        "https://raw.githubusercontent.com/manuGMG/proxy-365/main/SOCKS5.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/SOCKS5_RAW.txt",
        "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/socks5.txt"
    ],
    "http": [
        "https://www.proxy-list.download/api/v1/get?type=http",
        "https://www.proxyscan.io/download?type=http",
        "https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/http.txt",
        "https://api.openproxylist.xyz/http.txt",
        "https://raw.githubusercontent.com/shiftytr/proxy-list/master/proxy.txt",
        "http://alexa.lr2b.com/proxylist.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
        "https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
        "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt",
        "https://raw.githubusercontent.com/opsxcq/proxy-list/master/list.txt",
        "https://proxy-spider.com/api/proxies.example.txt",
        "https://multiproxy.org/txt_all/proxy.txt",
        "https://raw.githubusercontent.com/roosterkid/openproxylist/main/HTTPS_RAW.txt",
        "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/http.txt",
        "https://raw.githubusercontent.com/UserR3X/proxy-list/main/online/https.txt",
        "https://raw.githubusercontent.com/almroot/proxylist/master/list.txt",
        "https://raw.githubusercontent.com/aslisk/proxyhttps/main/https.txt",
        "https://raw.githubusercontent.com/B4RC0DE-TM/proxy-list/main/HTTP.txt",
        "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt",
        "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
        "https://raw.githubusercontent.com/mertguvencli/http-proxy-list/main/proxy-list/data.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt",
        "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt",
        "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt",
        "https://raw.githubusercontent.com/RX4096/proxy-list/main/online/http.txt",
        "https://raw.githubusercontent.com/RX4096/proxy-list/main/online/https.txt",
        "https://raw.githubusercontent.com/saisuiu/uiu/main/free.txt",
        "https://raw.githubusercontent.com/saschazesiger/Free-Proxies/master/proxies/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
        "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
        "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
        "https://rootjazz.com/proxies/proxies.txt",
        "https://www.proxy-list.download/api/v1/get?type=https"
    ]
}

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    print("")
    print(f"       ___                        ")
    print(f"  _ __/ __| __ _ _ __ _ _ __  ___ ")
    print(f" | '{Y}_{X} \\__ \\/ _| '_/ {Y}_{X}` | '{Y}_{X} \\/ {Y}-{X}_)")
    print(f" | .__/___/\\__|_| \\__._| .__/\\___|")
    print(f" |_|                   |_|        ")
    print("")

async def scrape_proxies(session, urls):
    proxies = []
    for url in tqdm(urls, desc="Fetching proxies", leave=False, bar_format=f"{Y}{{bar}}{X}"):
        try:
            logging.info(f"Fetching proxies from {url}")
            async with session.get(url, timeout=10) as response:
                if response.status == 200:
                    data = await response.text()
                    proxies.extend(data.split('\r\n'))
        except Exception as e:
            logging.error(f"Error fetching proxies from {url}: {e}")
    return list(filter(lambda proxy: len(proxy) > 0, proxies))

async def save_proxies_to_files(proxies_list, protocol):
    file_name = f'lists/{protocol}.txt'
    with open(file_name, 'w') as file:
        for proxy in proxies_list:
            file.write(f'{proxy}\n')
    logging.info(f"{len(proxies_list)} proxies saved to {file_name}")

async def download_and_save_proxies():
    live_proxies = {'socks4': 0, 'socks5': 0, 'http': 0}

    async with aiohttp.ClientSession() as session:
        for protocol, urls in proxies_urls.items():
            proxies_list = await scrape_proxies(session, urls)
            if proxies_list:
                await save_proxies_to_files(proxies_list, protocol)
                live_proxies[protocol] += len(proxies_list)

    return live_proxies

async def main():
    if not os.path.exists('lists'):
        os.makedirs('lists')
    print_banner()
    live_proxies = await download_and_save_proxies()
    print(f"Socks4 [{Y}{live_proxies['socks4']}{X}] Socks5 [{Y}{live_proxies['socks5']}{X}] Http [{Y}{live_proxies['http']}{X}]")
    input(f"\n\t\t\t  {Y}Continue{X}...\n")

if __name__ == "__main__":
    asyncio.run(main())
