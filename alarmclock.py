from playsound import playsound
from datetime import datetime

def validate_time(alarm_time):
    if len(alarm_time) != 8:
        return 'Невірний формат!'
    else:
        if int(alarm_time[0:2]) > 23:
            return 'Невірний формат годин!'
        elif int(alarm_time[3:5]) > 59:
            return 'Невірний формат годин хвилин!'
        elif int(alarm_time[6:8]) > 59:
            return 'Невірний формат годин секунд!'
        else:
            return 'Добре!'

while True:
    alarm_time = input('Потрібно ввести час у наступному форматі: \'HH:MM:SS\' \nВведіть час спрацювання будильника: ')
    validate = validate_time(alarm_time)
    if validate != 'Добре!':
        print(validate)
    else:
        print(f'Будильник спрацює в {alarm_time}...')
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
                print('ALAAAARM!!!')
                playsound('alarm.mp3')
                break
