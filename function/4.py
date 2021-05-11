def hour_to_sec(hour, min, sec):
    return hour *60 * 60 + min*60 + sec

res = hour_to_sec( 1, 0, 0)
print(res)