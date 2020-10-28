grade = input('Enter your grade: ')

try:
    grade = float(grade)
except:
    grade = input('Enter a number from 0.0 - 1.0: ')

if float(grade) >= 0.9:
    grade = 'A'
elif float(grade) >=0.8:
    grade = 'B'
elif float(grade) >= 0.7:
    grade = 'C'
elif float(grade) >= 0.6:
    grade = 'D'
elif float(grade) < 0.6:
    grade = 'F'
else:
    grade = input('Enter a number from 0.0 - 1.0: ')

print(grade)

input('Press Enter to Continue...')