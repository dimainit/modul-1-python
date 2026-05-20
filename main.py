# Mixins for function 

def get_name(text):
    name = input(text)
    while name == "":
        print("❌ Имя не может быть пустым.")
        name = input(text)
    return name
def get_tel(text):
    tel = input(text) 
    while not tel.isdigit() or len(tel) != 12:
        print("❌ Телефон должен содержать ровно 12 цифр.")
        tel = input(text)
    return tel
def get_email(text):
    email = input(text)
    while not "@" in email or not "." in email:
        print("❌ Email должен содержать @ и .")
        email = input(text)
    return email

def append_contacts(contact):
    file = open("contacts.txt", "a", encoding="UTF-8")
    file.write(contact + "\n")
    file.close()
def read_contacts():
    file = open("contacts.txt", "r", encoding="UTF-8")
    new_file = file.readlines()
    file.close()
    return new_file
def write_contacts(list):
    end_file = open("contacts.txt", "w", encoding="UTF-8")
    end_file.writelines(list)
    end_file.close()


# Funcions and logics

def add_contact ():
    name = get_name("Введите имя: ")
    tel = get_tel("Введите номер телефона: ")
    email = get_email("Введите почту: ")
    contact = f"{name} | {tel} | {email}"
    append_contacts(contact)
    print("✅ Контакт успешно добавлен!") 

def find_contact ():
    search = input("Введите имя или номер телефона: ")
    file = read_contacts()
    found = False
    for text in file:
        if search in text:
            print(text.strip())
            found = True
    if found == True:
        print("✅ Контакт найден.")
    if found == False:
        print("❌ Контакт не найден.")

def delete_contact ():
    new_list_name = []
    search = input("Введите имя или номер телефона: ")
    file = read_contacts()
    found = False
    for text in file:
        if search not in text:
            new_list_name.append(text)
        else:
            found = True
    write_contacts(new_list_name)
    if found == True:
        print("✅ Контакт удалён.")
    if found == False:
        print("❌ Контакт не найден.")

def update_contact():
    new_list_name = []
    search = input("Введите имя или номер телефона: ")
    file = read_contacts()
    uptade = False
    for text in file:
        if search in text:
            uptade = True
            name = get_name("Введите новое имя: ")
            tel = get_tel("Введите новый номер телефона: ")
            email = get_email("Введите новую почту: ")
            contact = f"{name} | {tel} | {email} \n" 
            new_list_name.append(contact)
        else:
            new_list_name.append(text)
    write_contacts(new_list_name)
    if uptade == True:
        print("✅ Контакт обновлён!")
    else:
        print("❌ Контакт не найден.")

def view_contact ():
    file = read_contacts()
    file.sort()
    for text in file:
        result = text.strip()
        print(result)
    

while True:
    print("1. Добавить контакт")
    print("2. Найти контакт")
    print("3. Удалить контакт")
    print("4. Обновить контакт")
    print("5. Просмотреть контакты")
    print("6. Выйти")
    start = input("Выбери пункт: ")
    if start == "1":
        add_contact()
    elif start == "2":
        find_contact()
    elif start == "3":
        delete_contact ()
    elif start == "4":
        update_contact()
    elif start == "5":
        view_contact ()
    elif start == "6":
        print("👋 Программа завершена. До свидания!")
        break
    else:
        print("❌ Неверный выбор. Попробуйте снова.")