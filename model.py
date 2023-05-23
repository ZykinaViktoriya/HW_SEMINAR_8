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