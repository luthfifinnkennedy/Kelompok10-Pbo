class logincustomer:


    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    @property
    def username(self):
        pass
    @username.getter
    def username(self):
        return self.__username
    @username.setter
    def username(self, username):
        self.__username = username

    @property
    def password(self):
        pass
    @password.getter
    def password(self):
        return self.__password
    @password.setter
    def password(self, password):
        self.__password = password

    def loginAutentikator(self):
        pass

customer = logincustomer("isne yeyen", "sepatu12")
print("username : ", customer.username ,"password :", customer.password)