import time
print("Countdown Timer")
print("----------------")

while True:
    try:
        seconds = int(input("Enter the number of seconds for the countdown: "))
        if seconds < 1:
            print("Please enter a valid number of seconds.")
            continue
        else:
            print(f"Countdown started for {seconds} seconds.")
            while seconds:
                print(f"Time left: {seconds} seconds", end="\r")
                time.sleep(1)
                seconds -= 1
            print("Time's up! Countdown finished.")
            print("----------------")
            continue
    except ValueError:
        print("Please enter numbers only.")
        
print("----------------")