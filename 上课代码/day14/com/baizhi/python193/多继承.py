class Father:
    money=100

class StepFather:
    money=1000

class Son(Father,StepFather):
    pass

s=Son()
print(s.money)