import view           

def add_contact(name, phone_number):
    with open('phone_book.txt', 'a', encoding='utf-8') as file:
        file.write('{}:{}\n'.format(name,phone_number))
        print(f"Контакт {name} успешно добавлен\n")
        
def find_contact(name):
    with open('phone_book.txt', 'r', encoding='utf-8' ) as file:
        for i in file:
            if name in i:
                print (i)
