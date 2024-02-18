# Steam Screenshots Downloader

This Python script allows you to search for a game on Steam using the Steam API and download screenshots of the game from your Steam Deck to your local machine.

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)
- Access to the Steam API (free)
- Steam deck has ssh enabled

## Getting Started

1. Clone this repository to your local machine.
2. Make sure you have Python installed on your system.
3. Install the required dependencies by running `pip install -r requirements.txt`.
4. Obtain your Steam ID from [SteamIDFinder](https://www.steamidfinder.com/).
5. Create a configuration file named `config.json` with the following structure:

```json
{
    "user_id": "YourSteamID",
    "ssh_user": "deck",
    "hostname": "cb-steamdeck"
}
```

Replace `"YourSteamID"` with your actual Steam ID.

## Usage

Run the script `sync.py` and follow the on-screen instructions:

```bash
python sync.py
```

Enter the name of the game you want to search for when prompted. If the game is found, the script will attempt to copy the screenshots from your Steam Deck to your local machine.

## Notes

- Make sure your Steam Deck is accessible via SSH and the specified user and hostname are correct in the configuration file.
- The Steam API key is not required as this script only uses the public GetAppList API endpoint.
- You can obtain your Steam ID from [SteamIDFinder](https://www.steamidfinder.com/).

## Sample Run

```bash
Enter the name of the game: ultros demo
App ID for 'ultros demo': 2709040
deck@cb-steamdeck's password: 
20240218005056_1.jpg                                                 100%  250KB   2.7MB/s   00:00    
20240218004334_1.jpg                                                 100%  370KB   4.6MB/s   00:00    
Screenshots copied successfully!
```