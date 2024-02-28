# Submitted
import datetime

num_cases = int(input())

def pad_start(string, char, length):
    while len(string) < length:
        string = char + string
    return string

for _ in range(num_cases):
    time1, time2 = input().split("|")

    t1_date, t1_time = time1.split()
    t2_date, t2_time = time2.split()

    t1_m, t1_d, t1_y = map(int, t1_date.split("."))
    t2_m, t2_d, t2_y = map(int, t2_date.split("."))
    t1_h, t1_mi, t1_s = map(int, t1_time.split(":"))
    t2_h, t2_mi, t2_s = map(int, t2_time.split(":"))

    t1 = datetime.datetime(t1_y, t1_m, t1_d, hour=t1_h, minute=t1_mi, second=t1_s)
    t2 = datetime.datetime(t2_y, t2_m, t2_d, hour=t2_h, minute=t2_mi, second=t2_s)

    t_new = t2 - t1

    days = t_new.days
    hours, seconds = divmod(t_new.seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    days_isp = days != 1
    hours_isp = hours != 1
    minutes_isp = minutes != 1
    seconds_isp = seconds != 1

    output = pad_start(str(days), "0", 2) + " Day" + ("s" if days_isp else "") + " " + pad_start(str(hours), "0", 2) + " Hour" + ("s" if hours_isp else "") + " " + pad_start(str(minutes), "0", 2) + " Minute" + ("s" if minutes_isp else "") + " " + pad_start(str(seconds), "0", 2) + " Second" + ("s" if seconds_isp else "")
    print(output)