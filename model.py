phone_book = {}

def get_data():
    with open('phone_book.txt','r') as file:
        for key,val in phone_book.items():
            phone_book = file.write('{}:{}\n'.format(key,val))
    return phone_book                

def add_contact(name, phone_number):
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        phone_book[name] = phone_number
        print(f"Контакт {name} успешно добавлен")
        
def remove_contact(name):
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        if name in phone_book:
            del phone_book[name]
            print(f"Контакт {name} успешно удален")
        else:
            print(f"Контакт {name} не найден")

def find_contact(name):
    with open('phone_book.txt', 'r', encoding='utf-8') as file:
        if name in phone_book:
            print(f"Номер телефона {name}: {phone_book[name]}")
        else:
            print(f"Контакт {name} не найден")
