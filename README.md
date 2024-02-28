[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

## About The Project

pScrape is a command line tool that uses the proxyscrape public api to save proxies.

![running the tool](https://i.imgur.com/wjZ3uhs.jpg)
![once complete](https://i.imgur.com/Ww5kxBR.jpg)

## Features

- Fetch proxies asynchronously using the ProxyScrape API.
- Check the status of each proxy.
- Save all proxies to a text file.
- Print out the status of each proxy.

## Installation

1. Ensure that you have Python (3.6 or later) installed on your machine.
2. Install the required Python libraries using pip:
  `pip install aiohttp ping3 colorama`
3. Download the `pscrape.py` file from this repository.
4. Run the script from the command line:
  `python pscrape.py`
5. When prompted, enter the type of proxies you'd like to fetch (HTTP, SOCKS4, SOCKS5, or ALL).

The script will then fetch the proxies, check their status, and save them into a text file. The status of each proxy will be printed out.

## Requirements

- Python 3.6 or later
- aiohttp library
- ping3 library
- colorama library

## Note

The `ping` function from the `ping3` library is blocking and might affect performance when checking the status of a large number of proxies.

## Future Improvements

Future updates to this script can include options for concurrent proxy status checking and options for saving only 'online' proxies.

Feel free to contribute to this project by submitting a pull request.

## Contact

[Telegram](https://t.me/mulicious) - [Discord](https://discord.gg/portlords) - [Cracked](https://cracked.io/herawen)
<p align="left">(<a href="#readme-top">back to top</a>)</p>
