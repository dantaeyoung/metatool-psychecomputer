import psutil
import subprocess

def kill_safari_if_instagram_open():
    # Iterate through running processes
    for process in psutil.process_iter(attrs=['pid', 'name']):
        try:
            process_name = process.info['name']
            if process_name == 'Safari':
                # Check if Instagram is open in Safari
                result = subprocess.check_output(["osascript", "-e", 'tell application "Safari" to get URL of document 1'])
                result_str = result.decode("utf-8")
                if "instagram.com" in result_str:
                    # Force quit Safari
                    subprocess.call(["osascript", "-e", 'tell application "Safari" to quit'])
                    print("Safari has been quit because Instagram was open.")
                    return
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    print("Instagram is not open in Safari.")

# Call the function
kill_safari_if_instagram_open()
