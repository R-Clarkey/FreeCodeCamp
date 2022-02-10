def add_time(start, duration, day=None):
  
  days_later = 0
  day_str_as_int = 0

  output_of_day = 0
  output_of_hour = 0
  output_of_minute = 0
  final_output = ""
  
  str_to_int = {
    "monday" : 1,
    "tuesday" : 2,
    "wednesday" : 3,
    "thursday" : 4,
    "friday" : 5,
    "saturday" : 6,
    "sunday" : 7,
  }

  int_to_str = {
      1 : "Monday",
      2 : "Tuesday",
      3 : "Wednesday",
      4 : "Thursday",
      5 : "Friday",
      6 : "Saturday",
      7 : "Sunday"
  }

  days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]



  start = start.split(" ")
  starting_time = start[0]
  period = start[1]

  starting_time_hour = int(starting_time.split(":")[0])
  starting_time_minute = int(starting_time.split(":")[1])

  duration = duration.split(":")
  duration_hour = int(duration[0])
  duration_minute = int(duration[1])
  print("\n",("*"*50))
  print("\nFull argument:", start, duration, day)
  # print("Hour:", starting_time_hour)
  # print("Minute:", starting_time_minute)
  # print("AM/PM",period)
  # print("Hour increasement:", duration_hour)
  # print("Minute increasement:", duration_minute,"\n")

  if (duration_minute + starting_time_minute >=60):
    output_of_minute = (duration_minute + starting_time_minute)% 60
    duration_hour +=1
    duration_minute = 0
    # print("Output of minute:",output_of_minute)
  else:
    output_of_minute = (duration_minute + starting_time_minute)
    duration_minute = 0
    # print("Output of minute:",output_of_minute)


  while duration_hour >= 24:
    duration_hour -= 24
    days_later += 1

  if period == "AM":
    if duration_hour + starting_time_hour > 12:
      duration_hour -= (12 - starting_time_hour)
      output_of_hour = duration_hour
      period = "PM"
    elif duration_hour + starting_time_hour == 12:
      output_of_hour = 12
      period = "PM"
    else:
      output_of_hour = starting_time_hour + duration_hour
  elif period == "PM":
    if duration_hour + starting_time_hour > 12:
      days_later +=1
      duration_hour -= (12 - starting_time_hour)
      output_of_hour = duration_hour
      period = "AM"
    elif duration_hour + starting_time_hour == 12:
      days_later +=1
      output_of_hour = 12
      period = "AM"
    else:
      output_of_hour = starting_time_hour + duration_hour

  if output_of_minute < 10:
    output_of_minute = str(0) + str(output_of_minute)

  if day != None:
    for index in days:
      if day.lower() == index:
        day_str_as_int = str_to_int[index]
    
    # print("Current day as value [1-7]:",day_str_as_int, "\nAmount of days changed:", days_later)
    output_of_days = days_later
    while days_later > 6:
      days_later -=7
    # print("Amount of days to shift after taking off weeks:",days_later)
    if day_str_as_int + days_later > 7:
      output_of_day = (days_later - (7-day_str_as_int))
      # print("Day Value:",output_of_day)
      # print("Day:",int_to_str[output_of_day])
    else:
      output_of_day = days_later + day_str_as_int
      # print("Day value:", output_of_day)
      # print("Day:", int_to_str[output_of_day])
    
    final_output += str(output_of_hour)
    final_output += ":"
    final_output += str(output_of_minute)
    final_output += " "
    final_output += str(period) 
    final_output += ", "
    final_output += str(int_to_str[output_of_day])
    # print(final_output)
    # print("Days later:",days_later)
    if days_later == 0:
      print(final_output)
      return final_output
    elif days_later == 1:
      final_output += " (next day)"
      print(final_output)
      return final_output
    elif days_later > 1:
      final_output += " ("+str(output_of_days)+" days later)"
      print(final_output)
      return final_output


  final_output += str(output_of_hour)
  final_output += ":"
  final_output += str(output_of_minute)
  final_output += " "
  final_output += str(period) 

  if days_later == 0:
    print(final_output)
    return final_output
  elif days_later == 1:
    final_output += " (next day)"
    print(final_output)
    return final_output
  elif days_later > 1:
    final_output += " ("+str(days_later)+" days later)"
    print(final_output)
    return final_output


