print('Welcome to the payrate calculator!\n')

hours = input('Enter hours: ')

try:
    hours = int(hours)
except:
    hours = input('Error, please enter a number: ')

rate = input('Enter pay rate: ')

try:
    rate = int(rate)
except:
    rate = input('Error, please enter a number: ')

payrate = int(hours) * int(rate)

if int(hours) > 40:
    print(payrate * 1.5)
else:
    print(payrate)

input('Press Enter to Continue...')