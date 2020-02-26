import os
import csv


data_path = ("../../03-Python/Homework03/Instructions/PyBank/Resources/budget_data.csv")

with open(data_path, newline="") as newfile:
    reader = csv.reader(newfile, delimiter=',')
    header = next(newfile)
    #print(f"Header: {csv_header}")
    count = 0
    reader_list1 = []
    
    for row in reader:
      #print(row)
      count += 1
      reader_list1.append(row)
      no_of_months = str(count)
    #print("there are "+ no_of_months + " months in the dataset")
    #print(reader_list1)
    #no_of_months = str(count)
    #print(no_of_months)
    
    net_total = 0
    for x in reader_list1:
      net_total = net_total + int(x[1])
      total = net_total
      total_amount = str(total)
    #print("the net total is " + "$" + total_amount)
    
    mean = total / count
    #average = str(mean)
    average = '{:.2f}'.format(mean)
    #print("the average change is " + "$" + average)
    
    reader_list2 = []
    for y in reader_list1:
      #y[1] = int(y[1])
      reader_list2.append(int(y[1]))
    #print(reader_list2)
    maximum = max(reader_list2)
    #print(maximum)
    str_maximum = str(maximum)
    #print(str_maximum)
    for x in reader_list1:
      if str_maximum == x[1]:
        #print(x)
        #print("the maximum is " + str(x))
        date = str(x[0])
        max_amount = str(x[1])
        #print("the maximum is " + date + " " + "on " + "($" + max_amount + ")")   
    
    reader_list3 = []
    for y in reader_list1:
      #y[1] = int(y[1])
      reader_list3.append(int(y[1]))
    #print(reader_list3)
    minimum = min(reader_list3)
    #print(minimum)
    str_minimum = str(minimum)
    #print(str_minimum)
    for x in reader_list1:
      if str_minimum == x[1]:
        #print(x)
        #print("the minimum is " + str(x))
        date2 = str(x[0])
        min_amount = str(x[1])
        #print("the minimum is " + date2 + " " + "on " + "($" + min_amount + ")")
    
    print("Financial Analysis")
    print("-----------------------------------------------------")
    print(f"Total Months:  {no_of_months}")
    print(f"Total:  {total_amount}")
    print(f"Average Change:  ${average}")
    print(f"Greatest Increase in Profits:  {date}  (${max_amount})")
    print(f"Greatest Decrease in Profits:  {date2}  (${min_amount})")





