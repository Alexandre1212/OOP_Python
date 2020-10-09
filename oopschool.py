import random
class Data:
    def __init__(self, *info):
        self.info = list(info)
    def __getitem__(self, item):
        return self.info[item]
    def __len__(self):
        return len(self.info)
class Teacher:
    def teach(self, info, *pupil):
        for i in pupil:
            i.study(info)
class Pupil:
    def __init__(self):
        self.knowledge = []
    def study(self, info):
        self.knowledge.append(info)
    def forget(self):
        self.knowledge.remove(random.choice(self.knowledge))
 
lesson = Data('class', 'object', 'inheritance', 'polymorphism', 'encapsulation')
TFHirianov = Teacher()
usual1 = Pupil()
usual2 = Pupil()
solo = Pupil()
c = Pupil()
for n in range(len(lesson)):
    TFHirianov.teach(lesson[n], usual1, usual2)
solo.study(lesson[3])
print(solo.knowledge)
print(usual1.knowledge)
print(usual2.knowledge)
usual1.forget()
print(usual1.knowledge)