phone_list = [
    ["Robb", "0680929258"],
    ["Stark", "380912146146"],
    ["Jonn", "+380636690103"],
    ["Snow", "+380638690261"],
    ["Tirion", "+958758767"]
]

phone_dict = dict(phone_list)

print(
    'Список команд які можна використати в даній телефонній книзі:',
    "Формат: команда, номер, ім'я",
    '- stats: кількість записів',
    '- add: додати запис',
    '- del: видалити запис за іменем (ключем)',
    '- list: список всіх імен в книзі',
    '- show: детальна інформація по імені',
    sep='\n'
)

while True:
    command = input('Enter a command: ')
# Переглянути кількість записів
    if command == 'stats':
        print(len(phone_dict))
# Додати нового користувача

    elif command == 'add':
        while True:
            '''
            цикл завершиться в разі спроби додати існуючий контакт
            '''
            user = input('Enter a name user: ')
            if user in phone_dict:
                print(f'{user} is already in the phonebook\nChange request')
                break
            number = input(f'Enter a number {user}: ')
            add_dict = {user: number}
            phone_dict.update(add_dict)
            break
# Видалити користувача
    elif command == 'del':
        remove = input('Enter a name user: ')
        del phone_dict[remove]
        print(f'{remove} has been deleted from the phonebook')
# Показати весь список контактів
    elif command == 'list':
        for key, value in phone_dict.items():
            print(key, value)
# Показати деталі по 1 користувачі за іменем
    elif command == 'show':
        key = input('View detailed information on the user: ')
        if key in phone_dict:
            contact = phone_dict[key]
            print(f'User: {key}',
                  f'Number: {contact}',
                  sep='\n'
                  )