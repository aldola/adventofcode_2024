file = open("day2.txt", "r")
safe_reports = 0
for line in file:
   safe = True
   last_value = int(line.split()[0])
   second_value = int(line.split()[1])
   dampener = True
   if last_value > second_value:
      decreasing = True
   else:
      decreasing = False
   for i in line.split()[1:]:
      i = int(i)
      if -3 <= last_value - i <= 3:
         if last_value == i:
            if dampener:
               dampener = False
            else:
               safe = False
               break
         if decreasing:
            if last_value < i:
               if dampener:
                  dampener = False
               else:
                  safe = False
                  break
         else:
            if last_value > i:
               if dampener:
                  dampener = False
               else:               
                  safe = False
                  break
         last_value = i
      else:
         if dampener:
            dampener = False
         else:
            safe = False
            break
   if safe:
      safe_reports += 1

print (safe_reports)