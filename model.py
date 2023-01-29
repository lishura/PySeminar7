import csv
import os


def add_contact():
    with open('last_ID.txt', 'r', encoding='utf-8') as info:
        last_ID = int(info.read())
    with open('contacts.csv', 'a', encoding='utf-8') as file:
        columns = ["ID", "Ф.И.О.", "Должность", "Телефон"]
        file_writer = csv.DictWriter(file, delimiter = ",", lineterminator="\r", fieldnames=columns)
        # file_writer.writeheader()
        # for i in range(10):
        file_writer.writerow({"ID": last_ID+1, "Ф.И.О.": input("Введите Ф.И.О. нового контакта: "), "Должность": input("Введите должность нового контакта: "), "Телефон": input("Введите номер телефона нового контакта: ")})
    with open('last_ID.txt','w', encoding='utf-8') as f:
        f.write(str(last_ID+1))


def print_contacts():
        with open('contacts.csv', 'r', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)  
            line_count = 0   
            for row in csv_reader:
                if line_count == 0:
                    print("                   ".join(row))
                    line_count+=1
                print(f'{row["ID"].center(5)} {row["Ф.И.О."].center(40)} {row["Должность"].center(20)} {row["Телефон"].center(15)}')
                line_count+=1
                

def delete_contact():
    id_del = int(input("Введите ID контакта для удаления: "))
    with open('contacts.csv', 'r', encoding='utf-8') as inp, open('contacts_del.csv', 'w', encoding='utf-8', newline='') as out:
        columns = ["ID", "Ф.И.О.", "Должность", "Телефон"]
        csv_reader = csv.DictReader(inp)
        csv_writer = csv.DictWriter(out, fieldnames=columns)
        csv_writer.writeheader()
        line_count = 0 
        for row in csv_reader:
            if int(row["ID"]) != id_del:
                csv_writer.writerow({"ID": line_count+1, "Ф.И.О.": row["Ф.И.О."], "Должность": row["Должность"], "Телефон": row["Телефон"]})
                line_count+=1
    with open('last_ID.txt','w', encoding='utf-8') as f:
        f.write(str(line_count))
    os.remove('contacts.csv')
    os.rename('contacts_del.csv', 'contacts.csv')

        



    
