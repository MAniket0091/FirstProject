class employees:

    def __init__(self,name,surname,pay):

        self.name = name
        self.surname = surname
        self.pay = pay
    
    def full_name(self):

        print(f'Hey {self.name} {self.surname} we are happy to have you here. We know you get paid {self.pay} dollars a year.')
    
    def dept(self) :
        print('Hey your department is Human Resources.')


class developers(employees):

    def __init__(self,name,surname,pay,prog_lang):
        super().__init__(name,surname,pay)
        self.prog_lang = prog_lang
    
    def dept(self):
        print('Hey your department is Programming and Research.')

class accountant(employees):

    def __init__(self,name,surname,pay,balance):
        super().__init__(name,surname,pay)
        self.balance = balance
    
    def dept(self):
        print('Hey your department is Accounts.')
    

dev_1 = developers('Joe','Rogan',50000,'Python')
dev_2 = developers('Justin','Smith',70000,'SQL')

acc_1 = accountant('Ross','Geller',40000,12000)
acc_2 = accountant('Martha','Stewart',60000,20000)

print(dev_1.full_name())
print(acc_2.full_name())

print(dev_2.dept())
print('I just updated this file')
