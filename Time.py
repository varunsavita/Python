import time

while True:
    # get current
    current_time = time.localtime()
    # format the time in 12-hour clock with AM/PM
    formatted_time = time.strftime("%I:%M:%S %p", current_time)

    print(formatted_time)
    time.sleep(1)