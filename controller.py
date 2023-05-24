import view, model

def start():
    view.greetings()
    while True:
        view.menu()
        answer = input('Введите команду\n')
        if answer == '1':
            name = input('Введите фамилию контакта:\n') 
            phone = input('Введите телефон контакта:\n')
            model.add_contact(name, phone: str)
        
        elif answer == '2':
            data = input('Введите данные контакта через пробел\n')
            model.find_contact(data: str, query)       
        
        elif answer == '3':
            name = input('Введите имя или фамилию контакта, который хотите удалить:  ')
            view.delete_contact(data: str, query)
            
if __name__ == '__main__':
    start()  
