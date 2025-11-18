        
class Client():
    def __init__(self,id,name,balance=0,pin=[]):
        self.id=id
        self.name=name
        self.balance=balance
        self.pin= pin
        
    def check_pin(self):
        user_pin = int(input("Введите пин код: "))
        return user_pin == self.pin
        
    def change_info(self):
        if self.check_pin():
            new_name = input('Введите новое имя: ')
            self.name = new_name
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
        
    def Client_info(self,):
        print(f'Id: {self.id} \nname: {self.name} \nbalance {self.balance}')
        
class Bank():
    def __init__(self,):
        self.Clients=[]
        
    def add_user(self,Client):
        self.Clients.append(Client)
        
        
    def create_user(self,id,balance,name):
        name=input('Введите ваше имя: ')
        id=int(input('Введите ваш айди: '))
        balance=int(input('Введите ваш баланс: '))
        pin= int(input('Создайте свой пин код: '))
        new_Client= Client(id =id, name = name,balance= balance,pin=pin)
        self.add_user(new_Client)
        print('Клиент добавлен')
         
    def get_clientid(self,id):
        client = self.get_clientid(id)
        if client.id == id:
            return client
        return None
            
        
    def cash(self,id,amount):
        client =self.get_clientid(id)
        if client.id==id:
            client.balance -= amount
        
def Atm_menu():
    global bank
    bank=Bank()
    
    while True:
        print('1-добавить клиента\n2-пополнить счет\n3-снять со счета\n4-посмотреть баланс\n5-выйти')
        choise=int(input("Выберите что хотите сделать: "))
        
        if choise == 1:
            bank.create_user()
        elif choise in [2,3,4]:
            id= int(input('Введите ваш id: '))    
            client = bank.get_clientid(id)
            if client is None:
                print("Клиент не найден")
                continue
            
        elif choise == 2:
            
            amount= int(input('Введите сумму пополнения: '))
            client.deposit(amount)
        elif choise == 3:
            amount= int(input('Введите сумму для снятия: '))
            client.withdraw(amount)
        elif choise == 4:
            client.show_balance()
        elif choise == 5:
            break
        else:
            print('Неверный выбор. Попробуйте снова')
            
Atm_menu()