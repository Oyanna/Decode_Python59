def hour_to_sec(hour, min, sec):
    return hour *60 * 60 + min*60 + sec

res = hour_to_sec(sec=50, hour=0, min=1)
print(res)