#!/usr/bin/env python3
import requests

def search_game_id(game_name):
    # Steam API endpoint for searching games
    url = "https://api.steampowered.com/ISteamApps/GetAppList/v2/"

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise exception for non-200 status codes
        data = response.json()

        # Search for the game name in the response data
        for app in data['applist']['apps']:
            if app['name'].lower() == game_name.lower():
                return app['appid']

        # If the game name is not found, return None
        return None

    except requests.exceptions.RequestException as e:
        print("Error making request:", e)
        return None

# Example usage
if __name__ == "__main__":
    game_name = input("Enter the name of the game: ")
    app_id = search_game_id(game_name)

    if app_id:
        print(f"App ID for '{game_name}': {app_id}")
    else:
        print(f"Game '{game_name}' not found.")
