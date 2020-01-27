# Napisać funkcję główną 'Generate', pozwalającą na wybór rodzaju generowanych danych
# Napisać podfunkcje generujące randomowe dane na podstawie bazy danych z pliku:
#     Funkcję generującą imię męskie/żeńskie
#     Funkcję generującą nazwisko
#     Funkcję generującą nick
#     Funkcję generującą email
#     Funkcję generującą adres
#     Funkcję generującą pełen zestaw danych (połączone wyniki poprzednich funkcji z podziałem na płeć)

welcome_message = """
Press F, to generate first name,
Press L, to generate last name,
Press N, to generate nick,
Press M, to generate e-mail,
Press A, to generate adress,
Press P, to generate full person data,
Press Z, to shutdown
Choice: """


def generate():
    print("* * * Random data generator * * *")
    choice = input(welcome_message)

    while choice not in ('z', 'Z'):
        if choice in ('f', 'F'):
            gender = input("Choice gender of generated name (M/F):")
            if gender in ('m', 'M'):
                generate_male_first_name()
            elif gender in ('f', 'F'):
                generate_female_first_name()
        elif choice in ('l', 'L'):
            generate_last_name()
        elif choice in ('n', 'N'):
            generate_nick()
        elif choice in ('m', 'M'):
            generate_email()
        elif choice in ('a', 'A'):
            generate_adress()
        elif choice in ('p', 'P'):
            gen = input("Choice gender of generated person (M/F):")
            if gen in ('m', 'M'):
                generate_person("Male")
            elif gen in ('f', 'F'):
                generate_person("Female")
        else:
            print("Wrong choice - try again")

        choice = input(welcome_message)
    print("* * * Generator is shutdown * * *")




def generate_male_first_name():
    pass


def generate_female_first_name():
    pass


def generate_last_name():
    pass


def generate_nick():
    pass


def generate_email():
    pass


def generate_adress():
    pass


def generate_person(gen):
    pass


generate()
