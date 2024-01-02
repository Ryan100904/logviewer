import os
import sys
import time

def restart_program():
    python = sys.executable
    os.execl(python, python, *sys.argv)

def main():
    print("Self-restart script started...")
    
    while True:
        # Wait for a certain period of time (e.g., 1 hour)
        time.sleep(86400)  # 3600 seconds = 1 hour
        
        # Restart the main script
        print("Restarting the main script...")
        restart_program()

if __name__ == "__main__":
    main()
