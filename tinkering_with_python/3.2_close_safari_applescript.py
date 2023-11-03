import subprocess
import os

def kill_safari_if_twitter_is_open():
    # AppleScript to check for Twitter in Safari and quit if found
    script = """
    tell application "Safari"
        set twitterIsOpen to false
        repeat with t in tabs of windows
            set tabURL to URL of t
            if tabURL contains "twitter.com" then
                set twitterIsOpen to true
                exit repeat
            end if
        end repeat
        
        if twitterIsOpen then
            quit
        end if
    end tell
    """

    # Run the AppleScript from Python
    try:
        subprocess.run(['osascript', '-e', script], check=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

kill_safari_if_twitter_is_open()
