class Student:  # classes define the template for an object
    # initiize function
    def __init__(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation

    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        return False


# objects contains actual data
chris = Student("Chris", "Computer Science", 4.0, False)
leia = Student("Leia", "Art", 3.6, False)

print(chris.gpa)  # 4.0
print(chris.on_honor_roll())
