def add_contact(name, phone: str):
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} - {phone}\n') 
        
def find_contact(data: str, query):
        with open('file.txt') as file:
            for line in file:
                if (data.last_name, data.name) == query:
                    return data
    
def delete_contact(data: str, query):
    with open('file.txt', 'r', encoding='UTF-8') as file:
        for i in range(0, len(data)):
            if name == data[i]['Name'] or name == data[i]['Surname']:
                del data[i]
