import view, model

def start():
    view.greetings()
    while True:
        view.menu()
        answer = input('Введите команду\n')
        if answer == '1':
            view.show()
        
        elif answer == '2':
            name = input('Введите фамилию контакта:\n') # может сделать отдельно ФИО, отельно телефон?
            phone = input('Введите телефон контакта:\n')
            model.add_contact(data)
        
        elif answer == '3':
            data = input('Введите данные контакта через пробел\n')
            model.search(data)       
        
        elif answer == '4':
            view.bye()
            break
        
        else:
            model.error() 
            
if __name__ == '__main__':
    start()  