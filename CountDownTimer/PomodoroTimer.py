import time

print("POMODORO STARTS NOW")
# t = int(input("How many seconds do you want to set the timer for? "))
for i in range(4):
    t = 25*60 # value of t is 25minutes
    while t:
        mins = t//60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(" "+ timer, end = "\r") #overwrite previous line
        time.sleep(1)
        t -=1
    print("BREAK TIME!!!")

    t = 5 * 60 # value of t is 5minutes
    while t:
        mins = t // 60
        secs = t % 60
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(" " + timer, end="\r")  # overwrite previous line
        time.sleep(1)
        t -= 1
    print("WORK TIME!!!")
    break