# Back end the acutal code for the calc ( simple stuff just look at the variable names)
def calculate_gpa(subject, isa1, isa2, assignment, esa, lab):
    isa1 = min(isa1, 40) / 2
    isa2 = min(isa2, 40) / 2
    assignment = min(assignment, 10)
    esa = min(esa, 100) / 2

    lab_score = 0
    max_score = 100

    if subject in ["chem", "python", "cs", "chemistry", "computer", "phy", "physics"]:
        lab_score = min(lab, 20)
        max_score = 120

    total = isa1 + isa2 + assignment + esa + lab_score
    scaled_total = (total / max_score) * 100

    if scaled_total >= 90:
        grade = "S"
    elif scaled_total >= 80:
        grade = "A"
    elif scaled_total >= 70:
        grade = "B"
    elif scaled_total >= 60:
        grade = "C"
    elif scaled_total >= 50:
        grade = "D"
    else:
        grade = "F"

    return total, max_score, scaled_total, grade
