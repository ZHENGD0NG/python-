#定义一个学生类
#要求：
#1. 属性包括学生姓名，学号，以及语数英三科的成绩
#2. 能够设置学生某科目的成绩
#3. 能够打印出该学生的所有科目的成绩

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.grades = {"语文": 0, "数学": 0, "英语": 0}

    def set_grade(self, course, grade):    #满足2选项，（谁，哪个科目，成绩）
        if course in self.grades:          #判断科目是否存在，存在在改，不存在不管
            self.grades[course] = grade    #如果这门课是self.grades里面的键，那么就把对应的值，更新成传入的参数grade

    def print_grades(self):    #这个就不需要新的参数了，因为是可以直接从上面的self.grades获取到的
        print(f"学生{self.name}(学号:{self.student_id})的成绩为:")
        for course in self.grades:     #要让他循环打印各科分数
            print(f"{course}:{self.grades[course]}分")

chen = Student("小陈", "100618")
chen.set_grade("语文", 92)
chen.set_grade("数学", 94)
chen.print_grades()