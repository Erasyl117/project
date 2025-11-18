


class bank():
    def __init__(self,clients):
        self.clients=clients
    def add_user(self,user):
        self.clients.append(user)
        
        
    def create_user(self,id,balance,name):
        name=input('Введите ваше имя: ')
        id=int(input('Введите ваш айди: '))
        balance=int(input('Введите ваш баланс: '))
        self.clients.append(client(name,id,balance))
        
        
    def delete_user(self,user):
        self.clients.remove(user)
    def deposit(self,id,amount):
        for client in self.clients:
            if client.id==id:
                client.balance += amount
    def cash(self,id,amount):
        for client in self.clients:
            if client.id==id:
                client.balance -= amount

        
class client():
    def __init__(self,id,name,balance=0):
        self.id=id
        self.name=name
        self.balance=balance
        
        def check_pin(self):
            user_pin = int(input("Введите пин код: "))
            return user_pin == self.pin
        
    def change_info(self):
        if self.check_pin():
            new_name = input('Введите новое имя: ')
            self.balance = new_name
            print(f"имя успешно изменено на {self.name}")
        else:
            print("пин код неверен, действие отменено")
  
        
        
    def deposit(self,amount):
        if self.check_pin():
            if amount > 0:
                self.balance += amount
                print(f'Баланс пополнен на {amount}. Текущий баланс {self.balance}')
            else:
                print('Сумма пополнения не должна быть меньше 0')
            
    def withdraw(self,amount):
        if self.check_pin():
            if amount > self.balance:
                print(f'Недостаточно средств на балансе. Текущий баланс: {self.balance}')
            elif amount > 500:
                print("нельзя снять больше 500 едениц со счета")
            else:
                self.balance -= amount 
                print(f'Снято {amount} средств. Текущий баланс: {self.balance}')
            
    def show_balance(self):
        print(f'Ваш текущий баланс: {self.balance}')
        
    def client_info(self,name,id):
        print(id,name)
        
def bank_menu():
    bank=bank()
    while True:
        print('1-добавить клиента\n2-пополнить счет\n3-снять со счета\n4-посмотреть баланс\n5-выйти')
        choise=int(input("Выберите что хотите сделать: "))
        
        if choise == 1:
            bank.create_user()
        elif choise == 2:
            client.deposit()
        elif choise == 3:
            client.withdraw()
        elif choise == 4:
            client.show_balance()
        elif choise == 5:
            break
        else:
            print('Неверный выбор. Попробуйте снова')