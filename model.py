def add_contact(name, phone: str):
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} - {phone}\n') 
        
        
# if __name__ == '__main__':
#     add_contact('Hello world')
    
    
def read_file():
    with open('file.txt', 'a', encoding='utf-8') as file:
        return file.read().split('\n')[: -1]
    

def delete_contact(data: str, query):
    query = input('Введите имя или фамилию контакта, который хотите удалить:  ')

    with open('file.txt', 'r', encoding='UTF-8') as file:
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                del data[i]

def find_contact(data: str, query):
    query = input('Введите имя контакта для поиска: ')
        with open('file.txt') as file:
            for line in file:
                if (data.last_name, data.name) == query:
                    return data
