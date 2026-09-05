name = input ("Enter students name: ")
maths_score = float(input("Enter Mathematics score: "))
englis_score = float(input("Enter English Score: "))
science_score = float(input("Enter Science Score: "))
total = maths_score + englis_score + science_score
average = total / 3
if average >= 90:
    grade ="A"
elif average >= 80:
    grade ="B"
elif average >= 70:
    grade ="c"
elif average >= 60:
    grade ="D"
else:
    grade ="F"

print (f"name: {name}")
print (f"maths_score: {85}")
print (f"english_score: {72}")
print (f"science_score: {90}")
print (total)
print (average)
print (grade)