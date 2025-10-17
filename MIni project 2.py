from  datetime import date

current_percentage = int(input("Enter the current attendance percentage: "))
target_percentage = int(input("Enter the target attendance percentage: "))
class_per_week = 7


if not (0 <= current_percentage <= 100 and 0 < target_percentage <= 100):
    print(" Invalid input. Please enter percentages between 0 and 100.")
    exit()


today=date.today()   
end_sem = date(2026, 1, 2)
days_left = (end_sem - today).days
weeks_left = max(days_left // 7, 1)


total_classes_left = weeks_left * class_per_week
current_total_classes = 100
current_attended = current_percentage
target_total_attendance = target_percentage * (current_total_classes + total_classes_left) / 100
classes_needed = max(int(target_total_attendance - current_attended), 0)
avg_classes_needed_per_week = round(classes_needed / weeks_left, 2)

if avg_classes_needed_per_week>7:
    print("ggs bro issa ova, better luck next time")

if current_percentage < target_percentage:
    print(" You need to attend",classes_needed," more classes to reach your target of",target_percentage,"%.")
    print(" That's about",avg_classes_needed_per_week," classes per week for the next",weeks_left," weeks.")
else:
    print(" You're on track! To maintain ",target_percentage,"  %:")
    print(" Attend at least ",classes_needed," more classes — about ",avg_classes_needed_per_week," per week.")



