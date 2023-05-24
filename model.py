def add_contact(data: str):
    # with open('file.txt', 'a', encoding='utf-8') as file:
    #     file.write(f'{data}\n')
    
    with open('file.txt', 'w', encoding='utf-8') as file:
        file.write(f'{data}\n')
        
        
if __name__ == '__main__':
    add_contact('Hello world')
    
    
def read_file():
    with open('file.txt', 'a', encoding='utf-8') as file:
        return file.read().split('\n')[: -1]
    

def delete_contact(data: str, query):
    name = input('Введите имя или фамилию контакта, который хотите удалить:  ')

    with open('file.txt', 'r', encoding='UTF-8') as file:
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                del data[i]

def find_contact(data: str, query):
        with open('file.txt') as file:
            for line in file:
                if (data.last_name, data.name) == query:
                    return data