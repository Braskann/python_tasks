import random

# генерация хорошего пароля
def good_password_generation(length):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alphabet += '0123456789'
    alphabet += '!@#$%^&*()[]<>/№%?'
    password = ''
    for i in range(length):
        password += random.choice(alphabet)
    return password

def check_your_password(password):
    f = open('10_million_password_list_top_1000000.txt', 'r')
    nums = f.read().splitlines()
    for elem in nums:
        if password == elem:
            print('Ваш пароль ненадежен, рекомендуем сменить его!')
            break

# меню
def main():
    print('\nЗдравствуйте! Что вы хотите сделать?\n')
    print('0 - выйти\n1 - сгенерировать хороший пароль\n2 - Сгенерировать плохой пароль\n3 - Проверить свой пароль\n')
    choice = None
    while choice != "0":
        choice = str(input('Ваш выбор - '))
        if choice == "0":
            print('Всего хорошего!')
        elif choice == "1":
            length = int(input('Введите длину пароля - '))
            good_password_generation(length)
            print(f'Ваш пароль готов! {password}')
        elif choice == "2":
            print(3434)
        elif choice == "3":
            password = str(input('Введите ваш пароль - '))
            check_your_password(password)

main()