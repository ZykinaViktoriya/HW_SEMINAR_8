def add_contact(name, phone: str):
    with open('file.txt', 'a', encoding='utf-8') as file:
        file.write(f'{name} - {phone}\n') 
        
        
# if __name__ == '__main__':
#     add_contact('Hello world')
    
    
def read_file():
    with open('file.txt', 'a', encoding='utf-8') as file:
        return file.read().split('\n')[: -1]