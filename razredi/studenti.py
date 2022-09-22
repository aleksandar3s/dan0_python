

class Student(object):
    def __init__(self, ocene, vpisna_st, ime, letnik):
        self.ocene = ocene
        self.vpisna_st = vpisna_st
        self.ime = ime
        self.letnik = letnik

    def oceni(self):
        print(self.oceni)

    def napreduj(self):
        pass

class Fakulteta(Student):
    def __init__(self, student, spisek_studentov):
        self.spisek_studentov = spisek_studentov
        self.student = student

    def vpis(self, novi_student):
        self.spisek_studentov.append(novi_student)
        print(self.spisek_studentov)

    def izpis(self, izpisan_student):
        self.spisek_studentov.pop(izpisan_student) 




if __name__ == "__main__":
    student1 = Student({"Matematika":10, "Robotika":10, "Osnove elektrotehnike": 10}, 64190377, "Aleksandar", 3)
    student2 = Student({"Matematika":8, "Robotika":10, "Osnove elektrotehnike": 9}, 64190377, "Ana", 1)
    student3 = Student({"Matematika":9, "Robotika":10, "Osnove elektrotehnike": 7}, 64190377, "Manca", 2)
    fakulteta1 = Fakulteta(student1, [])
    print(fakulteta1.vpis())
    
