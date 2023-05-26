import view, model

def start():
    view.greetings()
    

    while True:
        
        
        view.menu()
        
    
        choice = input("Введите номер действия: ")

        if choice == "1":
            name = input("Введите имя контакта: ")
            phone_number = input("Введите номер телефона: ")
            model.add_contact(name, phone_number)
        elif choice == "2":
            name = input("Введите имя контакта: ")
            model.remove_contact(name)
        elif choice == "3":
            name = input("Введите имя контакта: ")
            model.find_contact(name)
        elif choice == "4":
            break
