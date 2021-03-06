class bankAccount():
    def __init__(self, holder, balance):
        self.holder = holder
        self.balance = balance
    
    def initialize(self):
        name = input('Please enter a username:')
        self.holder = name
        self.options()

    def options(self):
        option = input('\nWhat transaction would you like to make, ' + self.holder + '? Enter the number corresponding to it below, or type \'exit\' to exit the program: \n1 - Deposit \n2 - Withdraw \n3 - Check balance \n4 - Change name \nexit - Exit this program\n\n')
        if option == '1':
            self.deposit()
        elif option == '2':
            self.withdraw()
        elif option == '3':
            self.checkBal()
        elif option == '4':
            self.changeName()
        elif option == 'exit':
            self.exit()
        else:
            print('That isn\'t a valid transaction number') 
            self.options()  

    def deposit(self):
        try:
            amount = int(input('\nHow much would you like to deposit?: '))
        except ValueError:
            print('Please enter a valid number.')
            self.deposit()
        else:
            if amount > 0:
                self.balance += amount
                print('$' + str(amount) + ' has been deposited')
            else:
                print('Please enter a valid number.')
                self.deposit()
            self.options()
    
    def withdraw(self):
        try:
            amount = int(input('\nHow much would you like to withdraw?: '))
        except ValueError:
            print('Please enter a valid number.')
            self.withdraw()
        else:
            if amount <= self.balance:
                if amount > 0:
                    self.balance -= amount
                    print('$' + str(amount) + ' has been withdrawn')
                    self.options()
                else:
                    print('Please enter a valid number')
                    self.withdraw()
            else:
                print('You don\'t have this much money in your account!')
                self.withdraw()
    
    def checkBal(self):
        print('\nYour current balance is: $' + str(self.balance))
        self.options()

    def changeName(self):
        name = str(input('\nWhat do you want to change your username to?: '))
        self.holder = name
        print('Your username has been changed to: ' + self.holder)
        self.options()
    
    def exit(self):
        print('\nThank you for using this program!')


account = bankAccount(None, 10000)
account.initialize()