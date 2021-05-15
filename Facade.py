"""Here is the example of Facade design pattern"""

"""Here is the main head that knows which subclasses are responsible for what operation.
   It also delegates requests to appropriate subclasses"""

class Facade:
    def __init__(self):
        self._system_1 = System1()
        self._system_2 = System2()

    def operation(self):
        self._system_1.operation1()
        self._system_1.operation2()
        self._system_2.operation3()
        self._system_2.operation4()


"""This implements subclasses functionality. It handles the work requested by the Facade class
   It has no knowledge about facade so it doesn't keep any references to it """


class System1:

    def operation1(self):
        print("Commencing first operation")

    def operation2(self):
        print("Commencing second operation")


class System2:
    """This implements subclasses functionality. It handles the work requested by the Facade class
       It has no knowledge about facade so it doesn't keep any references to it """

    def operation3(self):
        print("Commencing third operation")

    def operation4(self):
        print("Commencing forth operation")


"""Below we start the program with this function"""


def main():
    facade = Facade()
    facade.operation()


if __name__ == "__main__":
    main()
