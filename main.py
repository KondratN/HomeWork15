class User:
    __login = 0
    __password = 0

    def __init__(self, name, last_name):
        self.__name = name
        self.__last_name = last_name

    def get_name(self):
        return self.__name

    def get_last_name(self):
        return self.__last_name

    def set_name(self, name):
        self.__name = name

    def set_last_name(self, last_name):
        self.__last_name = last_name

    def set_login(self, login):
        if len(login) < 5:
            print('Логин должен быть не менее 5 символов')
        else:
            self.__login = login

    def set_password(self, password):
        _countLetters = 0
        if len(password) < 8:
            print('Пароль должен быть не менее 8 символов')
        else:
            for i in password:
                if i.alpha():
                    _countLetters += 1
            if _countLetters > 2:
                self.__password = password
            else:
                print('Пароль должен содержать хотя бы три буквы')

    def get_login(self):
        return self.__login

    def get_password(self):
        return self.__password

    def user_info(self):
        print(f'Имя: {self.__name}')
        print(f'Фамилия: {self.__last_name}')


user1 = User('Иван', 'Иванов')
user1.user_info()
user1.set_login('12345')
user1.set_password('qwerty')
