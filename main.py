#SCRIPT TO CALL ALL THE OTHER EXERCISES


class Exercises:
    def __init__(self,ex):
        self.ex = ex

    def say_hi(self):
        print('You have selected exercise number', self.ex)

    def say_bye(self):
        print('Goodbye :)')

    def ex1(self):
        import ex1

    def ex2(self):
        import ex2

    def ex3(self):
        import ex3

    def ex4(self):
        import ex4


ex = int(input("Which exercise do you want to execute?\n1.Convert video\n2.Compare videos\n3.Live streaming\n4.Choose IP for live streaming\n"))

while ex>4 or ex<1:
    print("Try again bro")
    ex = int(input(
        "Which exercise do you want to execute?\n1.Convert video\n2.Compare videos\n3.Live streaming\n4.Choose IP for live streaming\n"))

n = Exercises(ex)
n.say_hi()

if ex==1:
    n.ex1()

elif ex==2:
    n.ex2()

elif ex ==3:
    n.ex3()

elif ex ==4:
    n.ex4()

n.say_bye()

