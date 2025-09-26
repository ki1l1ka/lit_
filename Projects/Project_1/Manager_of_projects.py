def create():
    pass
def delete():
    pass
def search():
    pass
def close():
    pass
def show():
    pass
def interface():
    print('''Привет, пользователь, это программа Manager of projects. Здесь можно писать заметки''')
    while True:
        print('''Что ты хочешь сделать? 
        1. Создать заметку 
        2. Удалить заметку. 
        3. Найти заметку 
        4. Закрыть заметки 
        5. Показать заметки
        Для выбора команды, напишите номер команды.''')
        answer = input()
        match answer:
            case "1":
                create()
            case "2":
                delete()
            case "3":
                search()
            case "4":
                close()
            case "5":
                show()
            case _:
                print('''Выбери команды от 1 до 5''')
                continue