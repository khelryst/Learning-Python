print('Welcome! I will add numbers you give me until you type "done."')

count = []
x = []

while True:
    count = input('Enter a number: ')
    if count == 'done':
        break
    try:
        float(count)
    except:
        count = input('Please enter a number: ')
    for x in count:
        count = count + x
    

print('All of your numbers added: ' + count)