#!/usr/bin/env python3
import subprocess

def main():
    # Command to run sync.py with the "morrowind" argument
    command = ["python", "sync.py", "morrowind"]

    try:
        # Run the command and capture the output
        result = subprocess.run(command, capture_output=True, text=True)

        # Print the output from sync.py
        print(result.stdout)

        # Print any errors that occurred
        if result.stderr:
            print(f"Error: {result.stderr}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
