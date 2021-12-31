# # 3
# Students room:
# Реализуйте студенческую комнату с помощью ООП:
#
# Copy:
# Steve = Student("Steven Schultz", 23, "English")
# Johnny = Student("Jonathan Rosenberg", 24, "Biology")
# Penny = Student("Penelope Meramveliotakis", 21, "Physics")
# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>

class StudentRoom:
    def __init__(self, student1, student2, student3):
        self.student1 = student1
        self.student2 = student2
        self.student3 = student3

    def info_is_Student(self):
        print('Student1' + self.student1 +
              '\nStudent2' + self.student2 +
              '\nStudent3' + self.student3)



room = StudentRoom('"Steven Schultz", 23, "English"', '"Jonathan Rosenberg", 24, "Biology"', '"Penelope Meramveliotakis", 21, "Physics"')

room.info_is_Student()
