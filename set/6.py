months_winter = {"dec", "jan", "feb"}
months_summer = {"june", "july", "aug"}
all_months = months_summer.union(months_winter)
print(all_months)
print(months_winter | months_summer)

