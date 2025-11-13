grade_points = {"S": 10, "A": 9, "B": 8, "C": 7, "D": 6, "E": 5, "F": 0}

# sgpa formula maybe changed
def calculate_sgpa_letter(entries):
    total_points = 0
    total_credits = 0
    for grade, credit in entries:
        total_points += grade_points[grade.upper()] * credit
        total_credits += credit
    sgpa = round(total_points / total_credits, 2)
    return sgpa

#Actual math for the calc if its wrong pls change idk what the actual formula is bruh
def ms_calc_total(isa1, isa2, assignment, esa, credit, lab=0):
    if credit == 2:
        return ((isa1 / 2) + (isa2 / 2) + ((esa * 7) / 10))
    elif credit in [3, 4]:
        return ((isa1 / 2) + (isa2 / 2) + assignment + (esa / 2))
    elif credit == 5:
        return ((((isa1 / 2) + (isa2 / 2) + assignment + (esa / 2) + lab) * 120) / 100)
    else:
        raise ValueError("Credit must be 2-5")

def ms_grade_point(total):
    if total >= 90: return 10
    elif total >= 80: return 9
    elif total >= 70: return 8
    elif total >= 60: return 7
    elif total >= 50: return 6
    elif total >= 40: return 5
    else: return 0

def calculate_sgpa_marks(rows):
    total_points = 0
    total_credits = 0
    for isa1, isa2, assignment, esa, lab, credit in rows:
        total = ms_calc_total(isa1, isa2, assignment, esa, credit, lab)
        gp = ms_grade_point(total)
        total_points += gp * credit
        total_credits += credit
    sgpa = round(total_points / total_credits, 2)
    return sgpa

# Formula
def calculate_cgpa(values):
    total = 0
    count = 0
    for sg in values:
        total += sg
        count += 1
    return round(total / count, 2)
