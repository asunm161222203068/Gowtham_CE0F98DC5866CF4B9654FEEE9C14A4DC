def isLeapyear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
    return True
  else:
    return false 


year = 2012
if isLeapyear(year):
  print ("{}is not a leap year.". format (year))
else:
  print("{}is not a leap year.".format(year))
