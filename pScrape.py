import os
import aiohttp
import asyncio
from ping3 import ping
from colorama import init, Fore

# Initialize colorama for colored output
init()
R = Fore.LIGHTRED_EX
G = Fore.LIGHTGREEN_EX
Y = Fore.YELLOW
B = Fore.LIGHTBLUE_EX
P = Fore.LIGHTMAGENTA_EX
C = Fore.LIGHTCYAN_EX
X = Fore.RESET

# Asynchronous function to scrape proxies
async def scrape_proxies(session, api_key, protocol='socks5'):
    # Define the API URL
    api_url = f'https://api.proxyscrape.com/v2/?request=getproxies&protocol={protocol}&timeout=10000&country=all&ssl=all&anonymity=all&simplified=true'
    headers = {'Authorization': f'Bearer {api_key}'}
    # Make an asynchronous GET request
    async with session.get(api_url, headers=headers) as response:
        if response.status == 200:
            # Read the response text
            proxies = await response.text()
            # Split the proxies and filter out any empty ones
            proxies = proxies.split('\r\n')
            proxies = list(filter(lambda proxy: len(proxy) > 0, proxies))
            return proxies
        else:
            print(f" {R}Error{X}: Unable to fetch proxies. Status Code: {Y}{response.status}{X}")
            return []

# Asynchronous function to check the status of a proxy
async def check_proxy_status(proxy):
    try:
        # Note: ping function from ping3 library is blocking, it'll affect performance
        result = ping(proxy, timeout=1, unit='ms')
        if result is not None:
            return G + 'Online' + X
        else:
            return R + 'Offline' + X
    except TimeoutError:
        return Y + 'Timeout' + X

# Print a banner
print(f"{Y}       {G}___ {X}                                    ")
print(f"{Y} _ __ {G}/ __|{R} __ {P}_ _{B} __ _{C} _ __ {G} ___  ")
print(f"{Y}| '_ \{G}\\__ \{R}/ _|{P} '_{B}/ _` {C}| '_ \{G}/ -_)")
print(f"{Y}| .__/{G}|___/{R}\__|{P}_| {B}\__,_{C}| .__/{G}\___| ")
print(f"{Y}|_|                    {C}|_|{G}H{Y}e{R}r{P}a{B}w{C}e{G}n{X}")
print("")

# Asynchronous main function
async def main():
    # Take user input for protocol
    protocol = input(f'HTTP {Y}/{X} SOCKS4 {Y}/{X} SOCKS5 {Y}/{X} ALL{Y}:{X} ')
    # Initialize an aiohttp session
    async with aiohttp.ClientSession() as session:
        your_api_key = 'api_key'
        # Call scrape_proxies to fetch proxies
        proxies_list = await scrape_proxies(session, api_key=your_api_key, protocol=protocol)
        if proxies_list:
            total_proxies = len(proxies_list)
            live_proxies = 0
            print(f"\nProxies: ")
            # Iterate over proxies and check their status
            for proxy in proxies_list:
                status = await check_proxy_status(proxy)
                print(f" {G}{proxy}{X} - {Y}{status}{X}")
                if 'Online' in status:
                    live_proxies += 1
            # Save proxies to a file
            file_name = f'{protocol}.txt'
            with open(file_name, 'w') as file:
                for proxy in proxies_list:
                    # Note: You can't call async function here
                    file.write(f'{proxy}\n')
            print(f"\nScraping Complete{Y}!{X}\n Saved {Y}{total_proxies}{X} proxies to {Y}{file_name}{X}")
        else:
            print(f"\n{R}Error!{X} Please try again.")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())
    # Pause before exiting
    input("Press Enter to exit...")
