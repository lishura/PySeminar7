from faker import Faker
import model
import csv

fake = Faker(locale = "ru_RU")


def fill_contacts():   
    with open('contacts.csv', 'w', encoding='utf-8') as file:
        columns = ["ID", "Ф.И.О.", "Должность", "Телефон"]
        file_writer = csv.DictWriter(file, delimiter = ",", lineterminator="\r", fieldnames=columns)
        file_writer.writeheader()
        for i in range(10):
            file_writer.writerow({"ID": i+1, "Ф.И.О.": fake.name(), "Должность": fake.job(), "Телефон": fake.phone_number()})
        with open('last_ID.txt','w', encoding='utf-8') as f:
            f.write(str(i+1))


def greeting():
    print("Добро пожаловать в телефонный справочник!")


def choice_todo():
    print("Доступные операции с телефонной книгой:\n\
    1 - печать телефонной книги;\n\
    2 - добавление контакта;\n\
    3 - удаление контакта;\n")
    ch = input("Введите номер операции: ")
    if ch == '1':
        model.print_contacts()
    elif ch == '2':
        model.add_contact()
    elif ch == '3':
        model.delete_contact()










