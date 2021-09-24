import datetime
import json
#------------------------------------------------------------------------------
# reading and extracting data from timedata.json 
with open("timedata.json") as datafile:
  timedata=json.loads(datafile.read())
break_duration = datetime.timedelta(
                                    days=timedata["break_duration"]["days"], 
                                    seconds=timedata["break_duration"]["seconds"]
                                    )
# maximum amount of time the robot can work continuously before taking a break
maximum_working_time = datetime.timedelta(
                                          days=timedata["maximum_working_time"]["days"], 
                                          seconds=timedata["maximum_working_time"]["seconds"]
                                          )
# the unit of time at which the rate is given
timewidth=datetime.timedelta(
                             days=timedata["timewidth"]["days"],
                             seconds=timedata["timewidth"]["seconds"]
                             )
shift_start_time = datetime.datetime.fromisoformat(timedata["shift"]["start"])
shift_end_time = datetime.datetime.fromisoformat(timedata["shift"]["end"])

#------------------------------------------------------------------------------
# setting up empty lists for use 
standard_day_info=[]
extra_day_info=[]
#creating new lists that contains the information of the time slots
for i in timedata["roboRate"]["standard_day"]:
  timedata["roboRate"]["standard_day"][i]["start"]=datetime.datetime.strptime(timedata["roboRate"]["standard_day"][i]["start"], "%H:%M:%S")
  timedata["roboRate"]["standard_day"][i]["end"]=datetime.datetime.strptime(timedata["roboRate"]["standard_day"][i]["end"], "%H:%M:%S")
# it is convenient for calculation if we separate one time slot into if the original crosses the midnight
for i in timedata["roboRate"]["standard_day"]:
  if (timedata["roboRate"]["standard_day"][i]["start"] > timedata["roboRate"]["standard_day"][i]["end"] and 
      datetime.datetime.timestamp(timedata["roboRate"]["standard_day"][i]["end"]) % 86400 != 0):
    standard_day_info.append([
                              datetime.datetime(1900,1,1,0,0,0),
                              timedata["roboRate"]["standard_day"][i]["end"],
                              timedata["roboRate"]["standard_day"][i]["value"]
                              ])
    standard_day_info.append([
                              timedata["roboRate"]["standard_day"][i]["start"],
                              datetime.datetime(1900,1,1,0,0,0),
                              timedata["roboRate"]["standard_day"][i]["value"]
                              ])                        
  else:
    standard_day_info.append([
                              timedata["roboRate"]["standard_day"][i]["start"],
                              timedata["roboRate"]["standard_day"][i]["end"],
                              timedata["roboRate"]["standard_day"][i]["value"]
                              ])
# same procedure for weekends
for i in timedata["roboRate"]["extra_day"]:
  timedata["roboRate"]["extra_day"][i]["start"]=datetime.datetime.strptime(timedata["roboRate"]["extra_day"][i]["start"], "%H:%M:%S")
  timedata["roboRate"]["extra_day"][i]["end"]=datetime.datetime.strptime(timedata["roboRate"]["extra_day"][i]["end"], "%H:%M:%S")
for i in timedata["roboRate"]["extra_day"]:
  if (timedata["roboRate"]["extra_day"][i]["start"] > timedata["roboRate"]["extra_day"][i]["end"] and
      datetime.datetime.timestamp(timedata["roboRate"]["extra_day"][i]["end"]) % 86400 != 0):
    extra_day_info.append([
                           datetime.datetime(1900,1,1,0,0,0),
                           timedata["roboRate"]["extra_day"][i]["end"],
                           timedata["roboRate"]["extra_day"][i]["value"]
                           ])
    extra_day_info.append([
                           timedata["roboRate"]["extra_day"][i]["start"],
                           datetime.datetime(1900,1,1,0,0,0),
                           timedata["roboRate"]["extra_day"][i]["value"]
                           ])                        
  else:
    extra_day_info.append([
                           timedata["roboRate"]["extra_day"][i]["start"],
                           timedata["roboRate"]["extra_day"][i]["end"],
                           timedata["roboRate"]["extra_day"][i]["value"]
                           ])
standard_day_info.sort()
extra_day_info.sort()