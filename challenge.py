class Person:
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    gender = input("Enter your gender: ")

    def details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def info(self):
        print("Name: " + self.name + ", Age: " + self.age + ", Gender: " + self.gender)

    def voter_check(self):
        pass


person = Person()


class Voter(Person):

    def set_age(self):
        age = self.age

    def set_gender(self):
        gender = self.gender

    def set_name(self):
        name = self.name

    def voter_check(self):
        age = self.age
        if age < '18':
            print("The person is too young to vote")
        else:
            try:
                print("The person is able to vote")
            finally:
                print("The voting check is completed")

    def print_info(self):
        print("My name is {}".format(self.name))
        print("My age is {}".format(self.age))
        print("My gender is {}".format(self.gender))


person = Voter()
person.set_name()
person.set_age()
person.set_gender()
person.print_info()
person.voter_check()
