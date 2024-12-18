 # pscrape

`pscrape` is a Python script designed to scrape proxy lists from various sources and save them to files. It supports SOCKS4, SOCKS5, and HTTP(S) proxies. The script uses asynchronous I/O for efficient fetching and includes a progress bar to show the download status.

![Screenshot](https://i.imgur.com/iUkS72j.png)

## Features

- **Asynchronous Fetching**: Uses `aiohttp` for asynchronous HTTP requests to fetch proxy lists efficiently.
- **Progress Bar**: Displays a progress bar with a yellow fill character to indicate the download status.
- **Logging**: Includes logging for error tracking and debugging.
- **Customizable**: Easily add or remove proxy sources by modifying the `proxies_urls` dictionary.

## Requirements

- Python 3.7+
- `aiohttp`
- `tqdm`
- `colorama`

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/herawenn/pscrape.git
    cd pscrape
    ```

2. Install the required dependencies:

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the script:

    ```sh
    python pscrape.py
    ```

2. The script will display a banner, a progress bar for fetching proxies, and the total number of proxies saved for each protocol (SOCKS4, SOCKS5, HTTP(S)).

3. The proxy lists will be saved in the `lists` directory with filenames corresponding to the protocol (e.g., `socks4.txt`, `socks5.txt`, `http.txt`).

## Customization

You can customize the proxy sources by modifying the `proxies_urls` dictionary in the script. Add or remove URLs as needed to include or exclude specific proxy sources.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request if you have any suggestions, bug reports, or feature requests.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or inquiries, please contact alex[at]fear[dot]pw
