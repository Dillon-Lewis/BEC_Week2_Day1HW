# Task 1

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

print("Days of the week that fall on even numbers:")

for index in range(len(days_of_week)):
    if index % 2 == 0:
        print(days_of_week[index])

