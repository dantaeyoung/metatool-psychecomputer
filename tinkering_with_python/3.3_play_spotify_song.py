import subprocess

def play_random_spotify_song():
    # AppleScript to play a random track
    script = """
    tell application "Spotify"
        play track "spotify:track:2rcuUQp2wFLqNWXCiS1k1Y"
    end tell
    """

    # Execute the AppleScript
    try:
        subprocess.run(['osascript', '-e', script], check=True, text=True)
    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage
play_spotify_song()

