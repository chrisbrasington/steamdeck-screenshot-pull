#!/usr/bin/env python3
import os
import json
import requests
import subprocess

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

def copy_screenshots(game_name, app_id, user_id, ssh_user, hostname):
    # Destination directory for screenshots
    destination_dir = f"/home/chris/Pictures/Screenshots/\"{game_name}\""

    # SCP command to copy screenshots from Steam Deck to local machine
    scp_command = f"scp -r {ssh_user}@{hostname}:/home/{ssh_user}/.steam/steam/userdata/{user_id}/760/remote/{app_id}/screenshots/ {destination_dir}"

    # Execute the SCP command
    try:
        subprocess.run(scp_command, shell=True, check=True)
        print("Screenshots copied successfully!")
    except subprocess.CalledProcessError as e:
        print("Error copying screenshots:", e)

def read_config():
    # Read configuration from JSON file
    try:
        with open('config.json') as f:
            config = json.load(f)
        return config
    except FileNotFoundError:
        print("Config file not found.")
        return None

# Example usage
if __name__ == "__main__":
    game_name = input("Enter the name of the game: ")
    app_id = search_game_id(game_name)

    if app_id:
        print(f"App ID for '{game_name}': {app_id}")
        config = read_config()
        copy_screenshots(game_name, app_id, config['user_id'], config['ssh_user'], config['hostname'])
    else:
        print(f"Game '{game_name}' not found.")
