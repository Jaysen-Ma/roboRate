# function to calculate the rate for a specific time
def rate_cal(dummy_time,standard_day_info,extra_day_info):
  global rate
  if dummy_time.isoweekday() <= 5: 
    for j in range(0, len(standard_day_info)):
      if standard_day_info[j][0] <= dummy_time < standard_day_info[j][1]:
        rate = float(standard_day_info[j][2])
  else:
    for j in range(0, len(extra_day_info)):
      if extra_day_info[j][0] <= dummy_time < extra_day_info[j][1]:
        rate = float(extra_day_info[j][2])
  return rate