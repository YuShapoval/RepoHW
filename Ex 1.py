'''Напишіть програму «Довідник». Створіть два списки цілих.
Один список зберігає ідентифікаційні коди, другий — телефонні номери. Реалізуйте меню для користувача:
    відсортувати за ідентифікаційними кодами;
    відсортувати за номерами телефонів;
    вивести список користувачів з кодами та телефонами;
    вихід.
'''
def sort_directory(option,users,value_1,value_2,name_1,name_2):
    option.sort()
    result='\n'
    for opt in option:
        for i in range(0,len(value_1)):
            if opt == value_1[i]:
                result+=f'{users[i]} {name_1}{value_1[i]}; {name_2} {value_2[i]}\n'
                break
    return result

users=['User 1', 'User 2', 'User 3', 'User 4', 'User 5', 'User 6', 'User 7', 'User 8', 'User 9']
id_codes=['0766832196', '0101742922', '9541181093', '5226144390', '7200445494', '4493201446', '3211222948', '4192456287', '3062118357']
phone_numbers=['+380950930643', '+380677691359', '+380769672640', '+380968170672', '+380504004553', '+380667766150', '+380977031305',
               '+380963916296', '+380994080139']
option=""
while option!="q":
    result = ''
    option=input('enter a sort option: \n[id] - to sort by id codes;\n[ph] - to sort by phone numbers;\n[pr] - to print not sorted directory;\n[q] - to quit: ')
    if option == 'pr':
        for i in range(0,len(users)):
            result+=f'{users[i]} id code: {id_codes[i]}; phone number:  {phone_numbers[i]}\n'
    elif option == 'id' or option == 'ph':
        if option == 'id':
            option = list(id_codes)
            name_val_1='id code: '
            value_1 = id_codes
            name_val_2='phone number: '
            value_2 = phone_numbers
        elif option == 'ph':
            option = list(phone_numbers)
            name_val_1='phone number: '
            value_1 = phone_numbers
            name_val_2='id code: '
            value_2 = id_codes
        result = sort_directory(option, users, value_1, value_2, name_val_1, name_val_2)
    elif option == 'q':
        print('Bue!')
        break
    else:
         print('enter a correct option')
    print(result)
