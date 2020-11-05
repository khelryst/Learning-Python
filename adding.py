print('Welcome! I will add numbers you give me until you type "done."')

numlist = list()    #create list

while True:
    inp = input('Enter a number: ')
    if inp == 'done': break     #stop loop
    try:
        inp = float(inp)            
    except:
        inp = input('Please enter a number: ')
    numlist.append(inp)         #add number to list

added = sum(numlist)            #sum of list
maximum = max(numlist)
minimum = min(numlist)

print('All of your numbers added: ' + str(added))
print('Maximum: ' + str(maximum))
print('Minimum: ' + str(minimum))