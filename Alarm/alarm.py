import datetime
import time
import os  # For playing a sound (works on Windows)

def alarm_clock(alarm_time):
    print(f"Alarm set for {alarm_time}...")
    while True:
        now = datetime.datetime.now().strftime("%H:%M")
        if now == alarm_time:
            print("⏰ Alarm ringing! Wake up!")
            try:
                # This will try to play the default Windows alarm sound
                os.system("echo '\a'")
            except:
                print("Beep!")
            break
        time.sleep(10)  # Check every 10 seconds

# Set your desired alarm time here in HH:MM (24-hour) format
alarm_time = input("Set alarm time (HH:MM, 24-hour format): ")
alarm_clock(alarm_time)
