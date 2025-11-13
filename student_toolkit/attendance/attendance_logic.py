from datetime import date

# All the variable names and predefined info needed for the code to run ( update the end sem when new data is found )
def calculate_attendance(current_percentage, target_percentage):
    class_per_week = 7

    #Invalid entries 
    if not (0 <= current_percentage <= 100 and 0 < target_percentage <= 100):
        return {"error": "Invalid input. Enter percentages between 0 and 100."}

    today = date.today()
    end_sem = date(2026, 1, 2)
    days_left = (end_sem - today).days
    weeks_left = max(days_left // 7, 1)
    total_classes_left = weeks_left * class_per_week

    current_total_classes = 100
    current_attended = (current_percentage / 100) * current_total_classes
    target_total_attendance = (target_percentage / 100) * (
        current_total_classes + total_classes_left
    )

    classes_needed = max(int(target_total_attendance - current_attended), 0)
    avg_classes_needed_per_week = round(classes_needed / weeks_left, 2)
    bunkable_classes = max(round(class_per_week - avg_classes_needed_per_week, 2), 0)
    total_bunkable_classes = int(bunkable_classes * weeks_left)  # remove bunkable classes if needed for professional submission 

    if avg_classes_needed_per_week > class_per_week:
        return {"warning": "ggs bro issa ova, better luck next time"}  # change the code when to submit and make it professional

    return {
        "classes_needed": classes_needed,
        "total_left": total_classes_left,
        "avg_week": avg_classes_needed_per_week,
        "bunk_week": bunkable_classes,
        "bunk_total": total_bunkable_classes,
    }
