#1.Create a class hierarchy for shapes, starting with a base class Shape. Then,
#create subclasses like Circle, Rectangle, and Triangle. Implement methods to
#calculate area and perimeter for each shape.
class Shape:
    def __init__(self, shape):
        self.shape = shape
    def area(self):
        pass
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, shape, radius):
        super().__init__(shape)
        self.radius = radius
    def area(self):
        return 3.14*self.radius*self.radius
    def perimeter(self):
        return 2*3.14*self.radius
class Rectangle(Shape):
    def __init__(self, shape, length, breadth):
        super().__init__(shape)
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
class Triangle(Shape):
    def __init__(self, shape, side1, side2, side3):
        super().__init__(shape)
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
    def area(self):
        s = (self.side1+self.side2+self.side3)/2
        return (s*(s-self.side1)*(s-self.side2)*(s-self.side3))**0.5
    def perimeter(self):
        return self.side1+self.side2+self.side3
circle = Circle('Circle', 7)
print('Area of Circle:', circle.area())
print('Perimeter of Circle:', circle.perimeter())
rectangle = Rectangle('Rectangle', 5, 6)
print('Area of Rectangle:', rectangle.area())
print('Perimeter of Rectangle:', rectangle.perimeter())
triangle = Triangle('Triangle', 3, 4, 5)
print('Area of Triangle:', triangle.area())
print('Perimeter of Triangle:', triangle.perimeter())

#2.Design a bank account system with a base class Account and subclasses 
#SavingsAccount and CheckingAccount. Implement methods for deposit, withdrawal,
#and interest calculation.
class Account:
    def __init__(self):
        self.balance = 0
    def deposit(self, amount):  
        self.balance += amount
        return self.balance
    def withdraw(self, amount):
        if amount > self.balance:
            return 'Insufficient Balance'
        self.balance -= amount
        return self.balance
    def interest(self, rate):
        return self.balance*rate/100

class SavingsAccount(Account):
    def __init__(self):
        super().__init__()
    def interest(self, rate):
        return self.balance*rate/100
    
class CheckingAccount(Account):
    def __init__(self):
        super().__init__()
    def interest(self, rate):
        return self.balance*rate/100
print(' ')  
account = Account()
print('Account Balance:', account.deposit(1000))
print('Account Balance:', account.withdraw(500))
print('Interest:', account.interest(5))
savings_account = SavingsAccount()
print('Savings account balance is', savings_account.deposit(1000))
print('Savings account balance is', savings_account.withdraw(500))
print('Interest:', savings_account.interest(5))
checking_account = CheckingAccount()
print('Checking account balance is', checking_account.deposit(1000))
print('Checking account balance is', checking_account.withdraw(500))
print('Interest:', checking_account.interest(5))

#3.Create a base class Vehicle with attributes like make, model, and year, and
#then create subclasses for specific types of vehicles like Car, Motorcycle, 
#and Truck. Add methods to calculate mileage or towing capacity based on the 
#vehicle type.
class Vehicle:
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year    
    def mileage(self):
        pass
    def towing_capacity(self):
        pass
    
class Car(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    def mileage(self, mileage):
        if mileage < 10:
            return 'Good Mileage'
        return 'Bad Mileage'
    def towing_capacity(self, towing_capacity):
        if towing_capacity < 750:
            return 'Accepted Towing Capacity'
        return 'Too Much Towing Capacity'
    
class Motorcycle(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    def mileage(self, mileage):
        if mileage < 3:
            return 'Good Mileage'
        return 'Bad Mileage'
    def towing_capacity(self, towing_capacity):
        return 'No Towing Capacity'
    
class Truck(Vehicle):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
    def mileage(self, mileage):
        if mileage < 25:
            return 'Good Mileage'
        return 'Bad Mileage'
    def towing_capacity(self, towing_capacity):
        if towing_capacity < 1000:
            return 'Accepted Towing Capacity'
        return 'Too Much Towing Capacity'
print(' ')    
car = Car('Toyota', 'Corolla', 2015)
print('Mileage:', car.mileage(12))
print('Towing Capacity:', car.towing_capacity(800))
motorcycle = Motorcycle('Honda', 'CBR', 2018)
print('Mileage:', motorcycle.mileage(5))
print('Towing Capacity:', motorcycle.towing_capacity(0))
truck = Truck('Ford', 'F150', 2019)
print('Mileage:', truck.mileage(20))
print('Towing Capacity:', truck.towing_capacity(1200))

#4.Build an employee hierarchy with a base class Employee. Create subclasses 
#for different types of employees like Manager, Engineer, and Salesperson.Each 
#subclass should have attributes like salary and methods related to their roles.
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def role(self):
        pass
    def work(self):
        pass
    def display(self):
        return self.name, self.salary

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def role(self):
        return 'Manager'
    def work(self):
        return 'Planning, Organizing, Staffing, Directing, and Controlling'
    
class Engineer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def role(self):
        return 'Engineer'
    def work(self):
        return 'Designing, Developing, Building, and Testing'
    
class Salesperson(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def role(self):
        return 'Salesperson'
    def work(self):
        return 'Selling, Negotiating, and Networking'
print(' ')    
manager = Manager('John', 50000)
print('Name and Salary:', manager.display())
print('Role:', manager.role())
print('Work:', manager.work())
engineer = Engineer('Alice', 60000)
print('Name and Salary:', engineer.display())
print('Role:', engineer.role())
print('Work:', engineer.work())
salesperson = Salesperson('Bob', 40000)
print('Name and Salary:', salesperson.display())
print('Role:', salesperson.role())
print('Work:', salesperson.work())


#5.Create a class hierarchy for animals, starting with a base class Animal.
#Then, create subclasses like Mammal, Bird, and Fish. Add properties and 
#methods to represent characteristics unique to each animal group.
class Animal:
    def __init__(self, type):
        self.type = type
    
class Mammal(Animal):
    def __init__(self, type, legs, sound):
        super().__init__(type)
        self.legs = legs
        self.sound = sound
    def display(self):
        return self.type, self.legs, self.sound
    
class Bird(Animal):
    def __init__(self, type, wings, sound):
        super().__init__(type)
        self.wings = wings
        self.sound = sound
    def display(self):
        return self.type, self.wings, self.sound
    
class Fish(Animal):
    def __init__(self, type, fins, sound):
        super().__init__(type)
        self.fins = fins
        self.sound = sound
    def display(self):
        return self.type, self.fins, self.sound
print(' ')    
mammal = Mammal('Mammal', 4, 'Roar')
print('Mammal:', mammal.display())
bird = Bird('Bird', 2, 'Chirp')
print('Bird:', bird.display())
fish = Fish('Fish', 0, 'Blub')
print('Fish:', fish.display())


#6.Design a library catalog system with a base class LibraryItem and
#subclasses for different types of items like Book, DVD, and Magazine. 
#Include methods to check out, return, and display information about each item.
class LibraryItem:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.status = 'Available'
    def checkout(self):
        self.status = 'Checked Out'
    def return_item(self):
        self.status = 'Available'
    def display(self):
        return self.title, self.author, self.pages, self.status
    
class Book(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author, pages)
        
class DVD(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author, pages)
        
class Magazine(LibraryItem):
    def __init__(self, title, author, pages):
        super().__init__(title, author, pages)
  
print(' ')        
book = Book('Harry Potter', 'J.K. Rowling', 300)
print('Book:', book.display())
book.checkout()
print('Book:', book.display())
book.return_item()
print('Book:', book.display())
#same for the others
    