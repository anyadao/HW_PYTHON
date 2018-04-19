# В программе phone_book (https://github.com/dbradul/python/blob/master/phone_book.py) реализовать следующие функции:
## ●find_entry_age_phonebook 		# найти все записи с указанным возрастом
# #●print_phonebook_by_age		# распечатать все записи отсортированные по возрасту
# ●	delete_entry_name_phonebook	# удалить все записи с указанным именем
# ●	print_avr_age				# распечатать средний возраст всех абонентов
# ●	increase_age				# увеличить возраст всем абонентам на заданное пользователем кол-во лет
# ●	<ваша_функция>				# добавить любую функцию, манипулирующую записями (печать, добавление, удаление)
#  в телефонной книге на ваше усмотрение.
# ●	добавить поддержку еще одного поля (например, скайп, адрес, день рождения) и сделайте по нему поиск и печать.
# Т.е. добавить функцию для поиска и обновить существующую функцию печати.
#
# 	При выполнении обратите внимание на обработку ошибок. Например, если при удалении записи с заданным именем нет,
# то вывести сообщение “Not found!”.
import pickle

running = True

#------------------------------------------------------------------------------
phone_book = [
              {"name": "Petr", "surname": "Petrov", "age": 50, "phone_number":"+380501234567", "address": "Odessa"},
              {"name": "Ivan", "surname": "Ivanov", "age": 15, "phone_number":"+380507654321", "address": "Kyiv"},
              {"name": "Olga", "surname": "Verdii", "age": 22, "phone_number":"+380735690121", "address": "Kharkov"},
              {"name": "Timur", "surname": "Lazeb", "age": 13, "phone_number":"+380734937849", "address": "Bangkok"},
              {"name": "Anya", "surname": "Daaooa", "age": 21, "phone_number":"+380960738888", "address": "Hawai"},
              {"name": "Serezha", "surname": "Unt", "age": 69, "phone_number":"+380522454124", "address": "New-York"}
             ]


#------------------------------------------------------------------------------
def print_entry(number, entry):
    print ("--[ %s ]--------------------------" % number)
    print ("| Surname: %20s |" % entry["surname"])
    print ("| Name:    %20s |" % entry["name"])
    print ("| Age:     %20s |" % entry["age"])
    print ("| Phone:   %20s |" % entry["phone_number"])
    print ("| Address:   %20s |" % entry["address"])
    print ()


#------------------------------------------------------------------------------
def print_phonebook():
    print ()
    print ()
    print ("#########  Phone book  ##########")
    print ()

    number = 1
    for entry in phone_book:
        print_entry(number, entry)
        number += 1


#------------------------------------------------------------------------------
def add_entry_phonebook():
    surname = input("    Enter surname: ")
    name    = input("    Enter name: ")
    age     = int(input("    Enter age: "))
    phone_number   = input("    Enter phone num.: ")
    adress = input("    Enter address: ")

    entry = {}
    entry["surname"] = surname
    entry["name"] = name
    entry["age"] = age
    entry["phone_number"] = phone_number
    entry["address"] = adress
    phone_book.append(entry)


#------------------------------------------------------------------------------
def printError(message):
    print ("ERROR: %s" % message)


#------------------------------------------------------------------------------
def printInfo(message):
    print ("INFO: %s" % message)

#------------------------------------------------------------------------------
def change_number_by_name():
    name = str(input("    Enter name: "))
    number = int(input("    Please write a new number: "))
    for entry in phone_book:
        if entry["name"] == name:
            entry["phone_number"] = number
    print_phonebook()


    print_phonebook()

#-------------------------------------------------------------------------------
def find_entry_address_phonebook():
    address = str(input("    Enter address: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["address"] == address:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found!!")

#------------------------------------------------------------------------------
def find_entry_name_phonebook():
    name = str(input("    Enter name: "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["name"] == name:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found such name!!!")


#------------------------------------------------------------------------------
def find_entry_age_phonebook():
    age = int(input("   Enter age, please   "))
    idx = 1
    found = False
    for entry in phone_book:
        if entry["age"] == age:
            print_entry(idx, entry)
            idx += 1
            found = True
    if not found:
        printError("Not found this age!!!")

#------------------------------------------------------------------------------
def delete_entry_name_phonebook():
    name = str(input("  Enter name to delete info   "))
    condition = lambda entry: entry["name"] == name
    found = False
    for i in range(len(phone_book)-1, -1, -1):
        if condition(phone_book[i]):
            found = True
            del phone_book[i]
    print_phonebook()
    if not found:
        printError("Not found such name!!!")
#------------------------------------------------------------------------------
def count_all_entries_in_phonebook():
    print ("Total number of entries: ", len(phone_book))


#------------------------------------------------------------------------------
def sorting_by_age(elem):
    return elem['age']

def print_phonebook_by_age():
    phone_book.sort(key=sorting_by_age)
    print_phonebook()
#------------------------------------------------------------------------------
def increase_age():
    shift = int(input("Write number to shift the age of persons: "))
    for entry in phone_book:
        entry["age"] += shift
    print_phonebook()
#------------------------------------------------------------------------------
def avr_age_of_all_persons():
    avr_age = (sum([entry["age"] for entry in phone_book]))/len(phone_book)
    printInfo("Average age of persons is: %d " %(avr_age))

#------------------------------------------------------------------------------
def save_to_file():
    pickle.dump(phone_book, open("phone_book.save", "wb"))
    printInfo("Phonebook is saved into 'phone_book.save'")


#------------------------------------------------------------------------------
def load_from_file():
    global phone_book
    phone_book = pickle.load(open("phone_book.save", "rb"))
    printInfo("Phonebook is loaded from 'phone_book.save'")


#------------------------------------------------------------------------------
def exit():
      global running
      running = False


#------------------------------------------------------------------------------
def print_prompt():
      print()
      print()
      print()
      print("~ Welcome to phonebook ~")
      print("Select one of actions below:")
      print("     1 - Print phonebook entries")
      print("     2 - Print phonebook entries (by age)")
      print("     3 - Add new entry")
      print("     4 - Find entry by name")
      print("     5 - Find entry by age")
      print("     6 - Delete entry by name")
      print("     7 - The number of entries in the phonebook")
      print("     8 - Avr. age of all persons")
      print("     9 - Increase age by num. of years")
      print("     10 - Find entry by address")
      print("     11 - Change number")
      print("-----------------------------")
      print("     s - Save to file")
      print("     l - Load from file")
      print("     0 - Exit")
      print()


#------------------------------------------------------------------------------
def main():

    while running:
        try:

            menu = {
                  '1':  print_phonebook,
                  '2':  print_phonebook_by_age,
                  '3':  add_entry_phonebook,
                  '4':  find_entry_name_phonebook,
                  '5':  find_entry_age_phonebook,
                  '6':  delete_entry_name_phonebook,
                  '7':  count_all_entries_in_phonebook,
                  '8':  avr_age_of_all_persons,
                  '9':  increase_age,
                  '10': find_entry_address_phonebook,
                  '11': change_number_by_name,

                  '0':  exit,
                  's':  save_to_file,
                  'l':  load_from_file,
            }

            print_prompt()
            user_input = input("phonebook> ")
            menu[user_input]()

        except Exception as ex:
            printError("Something went wrong. Try again...")


#------------------------------------------------------------------------------
if __name__ == '__main__':
    main()