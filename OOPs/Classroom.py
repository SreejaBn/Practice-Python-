class Student:
    def __init__(self, name, score):
        self.name= name
        self.score= score

    def __str__(self):
        return f"Student: {self.name}, Score: {self.score}"
    
class Classroom:
    def __init__(self, class_name):
        self.class_name= class_name
        self.students= []

    def add_student(self, student_object):
        self.students.append(student_object)

    def get_average(self):
        if not self.students:
            return 0
        
        total_score= 0
        for s in self.students:
            total_score += s.score

        return total_score/len(self.students)
    
    def get_top_student(self):
        if not self.students:
            return 0
        
        top_student= self.students[0]
        for s in self.students:
            if (s.score > top_student.score):
                top_student= s
            else:
                return top_student
        

s1 = Student("Alice", 90)
s2 = Student("Bob", 80)
s3 = Student("Charlie", 98)

my_class = Classroom("Python 101")

my_class.add_student(s1)
my_class.add_student(s2)
my_class.add_student(s3)

print(f"Average Score: {my_class.get_average()}")
print(f"The top student is: {my_class.get_top_student()}")
