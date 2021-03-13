birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}
while True :
    print('Enter a name (Blam to quite) ')
    name = input()
    if name == '':
        break
    elif name in birthdays :  
        print(name,'thier birthday is : ',birthdays[name])
    else :
        print('the name is not in our database ')
        print('enter to add it ')
        bday = input('Enter a birthday')
        birthdays[name]= bday
        print('database is updated')