size = ['small', 'medium', 'large']
base = ['thick','thin']
topping = ['Pepperoni', 'Chicken', 'Extra cheese','Mushrooms','Spinach', 'Olives']
toppingChoice = []
answer = 'no'
orderNum= 1000
countSmall, countMedium, countLarge, countThin, CountThick = 0,0,0,0,0
new = 'yes'

while new == 'yes':
    
    while (answer == 'no' or answer == 'No'):
        print(' \tWelcome to ISS Pizza\n \tPlease choose your pizza size, base and extra toppings')
        
       
        print('Those are the options: ')
        print(' Size: ', size)
        print('Which size would you like: ')
        psize = input('Size: ')
        
        while (psize not in size):
            print('Sorry, invalid option. Please type again: ')
            print('Those are the options: ')
            print(' Size: ', size)
            print('Which size would you like: ')
            psize = input('Size: ')
        if psize == 'small':
            countSmall +=1
        elif psize == 'medium':
            countMedium+=1
        else:
            countLarge+=1
       
       
        print('Now, choose your base')
        print('Those are the options: ')
        print('Base: ', base)
        pbase = input('Base: ')

        while pbase not in base:
            print('Sorry, invalid option. Please type again: ')
            print('Those are the options: ')
            print('Base: ', base)
            pbase = input('Base: ')
        if pbase == 'thin':
            countThin +=1
        else:
            countThick+=1
            
        print(' Now, choose the toppings. A maximum of 3 toppings')

        count = 1
            
        while count <= 3:
                
            print('Those are the option')
            print('Toppings:', topping)
            ptopping = input('Toppings: ')
            if ptopping not in topping:
                print(' Invalid option, please type again')
            else:
                toppingChoice.append(ptopping)
                count+=1
        
        
        print('This is your order')
        print('Size: {}, base: {} , and toppings: {}'.format(psize, pbase, toppingChoice))
        print( '\nConfirm oder? \n\tType no to choose again or press any key to continious')

        answer = input('yes or no: ')
        orderNum+= 1
        
        print('Type yes for new customer order or press any key to show the daily balance')
    new = input('New order or close balance: ')
    if new =='yes':
        answer == 'no'

print('Order number: ', orderNum)
print('Total size of total number of pizzas sold is: ')
print('Small: {}, Medium: {}, Large: {}' .format(countSmall, countMedium, countLarge))
    
