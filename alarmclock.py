from playsound import playsound
from datetime import datetime

def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return 'Wrong format!'
    else:
        if int(alarm_time[0:2]) > 23:
            return 'Incorrect format of hours!'
        elif int(alarm_time[3:5]) > 59:
            return 'Incorrect format of minutes!'
        elif int(alarm_time[6:8]) > 59:
            return 'Incorrect format of seconds!'
        else:
            return 'GOOD!'

while True:
    alarm_time = input('Enter the time in the following format: \'HH:MM:SS\' \nSet the alarm for: ')
    validate = validate_time(alarm_time)
    if validate != 'GOOD!':
        print(validate)
    else:
        print(f'alarm clock set on {alarm_time}...')
        break

alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[6:8])

while True:
    now = datetime.now()
    current_hour = now.hour
    current_min = now.minute
    current_sec = now.second

    if alarm_hour == current_hour:
        if alarm_min == current_min:
            if alarm_sec == current_sec:
                print('ALARM!')
                playsound('alarm.mp3')
                break
