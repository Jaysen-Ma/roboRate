#Author: Chun Hin Ma
#Last edited: 19/09/2021
#This script is an attempt to the 2021 Credit Suisse Online Coding challenge (Entry Challenge)
import check
import rate
from timedata import *
#------------------------------------------------------------------------------
# initial check of inputs
check.int_check(standard_day_info,extra_day_info,shift_start_time,shift_end_time)

# set up initial values
earn = 0
earn1 = 0
alpha = 0
gamma = 0
dummy_time = shift_start_time
# first breaking time
breaktime = shift_start_time + maximum_working_time
# argued in section 4.4 in README.pdf
if maximum_working_time < timewidth:
  timewidth = maximum_working_time

# useful constants
zero = datetime.timedelta(0)
one_day = datetime.timedelta(days= 1)
one_week = datetime.timedelta(days= 7)
time_interval = break_duration + maximum_working_time

#calculating the least commom multiple (section 5 in README.pdf)
larger= max(time_interval, timewidth, one_week)
period=larger
while (period % time_interval != zero or 
       period % timewidth != zero or
       period % one_week != zero):
  period += larger
# number of periods
n = (shift_end_time - shift_start_time) // period
# set as small as possible so the condition will not be met easily unless we want it to be met 
eff_end_time2 = datetime.datetime(1,1,1,0,0,0)
if n == 0:
  eff_end_time1 = shift_end_time
else:
  eff_end_time1 = shift_start_time + period
  eff_end_time2 = shift_end_time - n*period

# beta condition (section 4.4)
while eff_end_time1 - dummy_time > zero:  
  # the info has to be updated regularly otherwise they get outdated
  for j in range(0, len(standard_day_info)):
    standard_day_info[j][0] = standard_day_info[j][0].replace(
                                                              year = dummy_time.year,
                                                              month = dummy_time.month,
                                                              day = dummy_time.day
                                                              )  
  for j in range(0, len(standard_day_info)):  
    standard_day_info[j][1] = standard_day_info[j][1].replace(
                                                              year = dummy_time.year,       
                                                              month = dummy_time.month,
                                                              day = dummy_time.day
                                                              )
  # the date of the midnight is by default one day earlier and need to be adjusted
  standard_day_info[-1][1] = standard_day_info[-1][1] + one_day 
  for k in range(0, len(extra_day_info)):
    extra_day_info[k][0] = extra_day_info[k][0].replace(  
                                                        year = dummy_time.year,
                                                        month = dummy_time.month,
                                                        day = dummy_time.day
                                                        )
  for k in range(0, len(extra_day_info)):
    extra_day_info[k][1] = extra_day_info[k][1].replace(
                                                        year = dummy_time.year,
                                                        month = dummy_time.month,
                                                        day = dummy_time.day
                                                        )
  extra_day_info[-1][1] = extra_day_info[-1][1] + one_day
  # decide whter to break or not
  if (breaktime > dummy_time or 
    dummy_time >= breaktime + break_duration):
    #gamma condition
    if dummy_time > breaktime + break_duration - timewidth:
      earn += rate.rate_cal(dummy_time, standard_day_info, extra_day_info)
      dummy_time = breaktime + break_duration
      gamma = 1   
    if (dummy_time.isoweekday() <= 5 and gamma == 0):                    
      #alpha condition
      for j in standard_day_info:
        if zero < j[1] - dummy_time < timewidth:
          earn += rate.rate_cal(dummy_time, standard_day_info, extra_day_info)
          dummy_time = j[1]
          alpha = 1
      # ordinary condition
      if alpha == 0 and gamma == 0:
        earn += rate.rate_cal(dummy_time, standard_day_info, extra_day_info)
        dummy_time += timewidth 
    elif (dummy_time.isoweekday() > 5 and gamma == 0):            
      #alpha condition
      for k in extra_day_info:  
        if zero < k[1] - dummy_time < timewidth:
          earn += rate.rate_cal(dummy_time, extra_day_info, extra_day_info)
          dummy_time = k[1]
          alpha = 1
      # ordinary condition
      if alpha == 0 and gamma == 0:
        earn += rate.rate_cal(dummy_time, standard_day_info, extra_day_info)
        dummy_time += timewidth
  else:
    dummy_time += timewidth
  # reset alpha and gamma values
  alpha = 0
  gamma = 0
  # memorize the result of the summation of the second sub-shift
  if timewidth + eff_end_time2 > dummy_time :
    earn1 = earn
  # updating the next breaking time
  if dummy_time >= breaktime + break_duration:
    breaktime += time_interval
if n == 0:
  total_earn = earn
else:
  total_earn = n*earn + earn1
print("The robots will earn a total of {} in this shift".format(total_earn))
print("Please read README.pdf in FILES to review the details of the discussion, assumptions and comment on the problem statement and solution which is not explicitly stated in this script")