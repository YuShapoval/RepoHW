# * Написати сортування для списка по кажному параметру окремо. По імені, по прізвищу, по місту ( за кількістю населення ),
# по номеру ( розбиваючи за операторами ), за віком

def sort_name(opt,revers):
    sort_list=[]
    for i in range(0, len(people)):
        sort_list.append(people[i][opt])
    sort_list.sort(reverse=revers)
    sorted_list=[]
    for i in range(len(sort_list)):
        for j in range(len(people)):
            if sort_list[i]==people[j][opt]:
                sorted_list.append(people[j])
    return sorted_list

def sort_cities(cities,revers):
    if revers==False:
        sort_list=cities
    elif revers==True:
        sort_list=cities[::-1]
    sorted_list=[]
    for i in range(len(sort_list)):
        for j in range(len(people)):
            if sort_list[i]==people[j]["місто проживання"]:
                sorted_list.append(people[j])
    return sorted_list

def sort_phone(operators,revers):
    sort_list=[]
    for i in operators:
        sort_list.append(i)
    sort_list=sorted(sort_list,reverse=revers)
    sorted_list=[]
    for i in range(len(sort_list)):
        for j in range(len(people)):
            if people[j]["номер телефону"][0:6] in operators[sort_list[i]]:
                sorted_list.append(people[j])
    return sorted_list
        #________________________________________________________________________________________________________
people = [
    {
        "ім'я": "Андрій",
        "прізвище": "Коваленко",
        "номер телефону": "+380501234567",
        "місто проживання": "Київ",
        "вік": 28
    },
    {
        "ім'я": "Олена",
        "прізвище": "Шевченко",
        "номер телефону": "+380631112233",
        "місто проживання": "Львів",
        "вік": 34
    },
    {
        "ім'я": "Ігор",
        "прізвище": "Мельник",
        "номер телефону": "+380971234567",
        "місто проживання": "Одеса",
        "вік": 41
    },
    {
        "ім'я": "Наталія",
        "прізвище": "Бондаренко",
        "номер телефону": "+380939998877",
        "місто проживання": "Харків",
        "вік": 25
    },
    {
        "ім'я": "Руслан",
        "прізвище": "Дяченко",
        "номер телефону": "+380661234321",
        "місто проживання": "Дніпро",
        "вік": 37
    }
]       #________________________________________________________________________________________________________
option=""
cities=['Київ','Харків','Одеса','Дніпро','Львів']
operators={'Kyivstar':['+38067', '+38068', '+38096', '+38097', '+38098', '+38077'],
           'Vodafone':['+38050', '+38066', '+38095', '+38099', '+38075'],
           'Lifecell':['+38063', '+38073', '+38093']}

while option!="q":
    result = ''
    option=input('enter a sort option: \n[n+] - to sort by name in ascending order;\n[n-] - to sort by name in descending order;'
                 '\n[sn+] - to to sort by surname in ascending order;\n[sn-] - to to sort by surname in descending order;\n'
                 '[n+] - to sort by age in ascending order;\n[n-] - to sort by age in descending order;\n'
                 '[p+] - to sort by phone operator in ascending order;\n[p-] - to sort by phone operator in descending order;\n'
                 '[c+] - to sort by city population in ascending order;\n[c-] - to sort by city population in descending order;\n'
                 '[q] - to quit: ')
    if option=='n+':
        result=sort_name("ім'я", False)
    elif option=='n-':
        result=sort_name("ім'я", True)
    elif option=='sn+':
        result=sort_name("прізвище", False)
    elif option=='sn-':
        result=sort_name("прізвище", True)
    elif option=='a+':
        result=sort_name("вік", False)
    elif option=='a-':
        result=sort_name("вік", True)
    elif option == 'p+':
        result = sort_phone(operators, False)
    elif option == 'p-':
        result = sort_phone(operators, True)
    elif option == 'c+':
        result = sort_cities(cities, False)
    elif option == 'c-':
        result = sort_cities(cities, True)
    elif option == 'q':
        print('Bue!')
        break
    else:
         print('enter a correct option')
    print(f'\n{result}\n')

