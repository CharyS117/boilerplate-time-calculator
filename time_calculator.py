def add_time(start, duration, weekday=''):
    weekdays_list = [
        'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
        'sunday'
    ]
    start_hour = int(start.split(':')[0])
    start_min = start.split(':')[1]
    am_or_pm = start_min.split(' ')[1]
    start_min = int(start_min.split(' ')[0])
    d_hour = int(duration.split(':')[0])
    d_min = int(duration.split(':')[1])
    if am_or_pm.lower() == 'pm':
        start_hour = start_hour + 12
    end_min = start_min + d_min
    in_hour = end_min // 60
    end_min = end_min % 60
    end_hour = start_hour + d_hour + in_hour
    days = end_hour // 24
    end_hour = end_hour % 24
    if end_hour >= 12:
        end_hour = end_hour - 12
        end_aop = 'PM'
    else:
        end_aop = 'AM'
    if days == 0:
        output_days = ''
    elif days == 1:
        output_days = ' (next day)'
    else:
        output_days = ' (' + str(days) + ' days later)'
    if end_hour == 0:
        end_hour = 12
    if weekday != '':
        index = weekdays_list.index(weekday.lower()) + days
        index = index % 7
        weekday = ', ' + weekdays_list[index][0].upper() + weekdays_list[index][1:]
    new_time = str(end_hour) + ':' + str(end_min).zfill(
        2) + ' ' + end_aop + weekday + output_days

    return new_time