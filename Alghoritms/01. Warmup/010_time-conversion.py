# Problem: https://www.hackerrank.com/challenges/time-conversion/problem
# Points: 15.00


def timeConversion(s):
    hours = s[0:2]
    result_time = s[2:-2]
    t_format = s[-2:]
    
    print('Format:', t_format, '\nHours:', hours, '\nRest of the input:', result_time)
    if int(hours) > 12:
        return
    if t_format == 'PM':
        hours_alt = '12' if hours == '12' else str(int(hours) + 12)
        return hours_alt + result_time
    if t_format == 'AM':
        hours_alt = '00' if hours == '12' else hours
        return hours_alt + result_time