'''Напишіть програму «Книги». Створіть два списки з даними.
Один список зберігає назви книг, другий — роки випуску. Реалізуйте меню для користувача:
    відсортувати за назвою книг;
    відсортувати за рокам випуску;
    вивести список книг з назвами та роками випуску;
    вихід.
'''
def sort_books(option,book_names,book_yaers):
    result = '\n'
    if option=='n':
        option_list=list(sorted(book_names))
        for opt in option_list:
            for i in range(0,len(book_names)):
                if opt == book_names[i]:
                  result+=f'{book_names[i]} - {book_yaers[i]} year\n'
                  break
    elif option=='y':
        option_list = list(sorted(book_yaers))
        for opt in option_list:
            for i in range(0, len(book_years)):
                if opt == book_years[i]:
                    result += f'{book_names[i]} - {book_yaers[i]} year\n'
                    break
    return result

book_names=['If Cats Disappeared from the World','Belladonna','Assistant to the Villain','Sharp Objects','Magnolia Parks']
book_years=[2018, 2023, 2022, 2007, 2014]



option=""
while option!="q":
    result = ''
    option=input('enter a sort option: \n[n] - to sort by book\'s name;\n[y] - to sort by year;\n[pr] - to print not sorted directory;\n[q] - to quit: ')
    if option == 'pr':
        for i in range(0,len(book_names)):
            result+=f'{book_names[i]}- {book_years[i]} year\n'
    elif option == 'n' or option == 'y':
        result = sort_books(option, book_names, book_years)
    elif option == 'q':
        print('Bue!')
        break
    else:
         print('enter a correct option')
    print(result)
