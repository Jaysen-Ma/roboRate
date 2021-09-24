from timedata import *
import sys
#------------------------------------------------------------------------------
# function to do initial checks
def int_check(
              standard_day_info,
              extra_day_info,
              shift_start_time,
              shift_end_time
              ):
  for j in standard_day_info:
    if j[2] < 0:
      sys.exit(
              "Standard day time rates cannot be negative"
              )
  for k in extra_day_info:
    if k[2] < 0:
      sys.exit(
              "Extra day time rates cannot be negative"
              )
  if len(standard_day_info) > 1:
    for j in range(0, len(standard_day_info)-1):
      if (standard_day_info[j+1][0] != standard_day_info[j][1]):
        sys.exit(
                "Please check all standard day times have been specified a unique non-empty rate."
                )
      elif standard_day_info[-1][1] != standard_day_info[0][0]:
        sys.exit(
                "Please check all standard day times have been specified a unique non-empty rate."
                )
      elif standard_day_info[j][0] == standard_day_info[j][1]:
        sys.exit(
                "At least one standard day time slot have zero time duration."
                )
  else:
    if standard_day_info[0] != standard_day_info[1]:
      sys.exit(
              "Start time of time slot has to equal to the end time if there is only one time slot on a standard day."
              )
  if len(extra_day_info) > 1:
    for k in range(0, len(extra_day_info)-1):
      if (extra_day_info[j+1][0] != extra_day_info[j][1]):
        sys.exit(
                "Please check all extra day times have been specified a unique non-empty rate."
                )
      elif extra_day_info[-1][1] != extra_day_info[0][0]:
        sys.exit(
                "Please check all extra day times have been specified a unique non-empty rate."
                )
      elif extra_day_info[j][0] == extra_day_info[j][1]:
        sys.exit(
                "At least one extra day time slot have zero time duration."
                )
  else:
    if extra_day_info[0] != extra_day_info[1]:
      sys.exit(
              "Start time of time slot has to equal to the end time if there is only one time slot on an extra day."
              )
  if shift_start_time > shift_end_time:
    sys.exit(
            "I have not grasped the essence of backward time travelling yet. The shift has ended before it has started."
            )
  if (maximum_working_time == datetime.timedelta(0) or
      break_duration == datetime.timedelta(0) or
      timewidth == datetime.timedelta(0)):
      sys.exit(
              "Time duration cannot be zero(s)"
              )