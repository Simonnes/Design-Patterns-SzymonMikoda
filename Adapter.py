"""We start with making a base class"""
class EnglishSocketSystem:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass

    def earth(self): pass


"""Then we give this class values"""
class Socket(EnglishSocketSystem):
    def voltage(self):
        return 95

    def live(self):
        return 1

    def neutral(self):
        return -1

    def earth(self):
        return 0


"""Here we have our target Socket system for this project"""
class PolishSocketSystem:
    def voltage(self): pass

    def live(self): pass

    def neutral(self): pass


"""Here is the adapter that will help us change the voltage so we won't destroy our microwave"""
class Adapter(PolishSocketSystem):
    __socket = None

    def __init__(self, socket):
        self.__socket = socket

    def voltage(self):
        return 40

    def live(self):
        return self.__socket.live()

    def neutral(self):
        return self.__socket.neutral()


"""Here is our receiver of the electricity through the adapter above"""
class Microwave:
    __power = None

    def __init__(self, power):
        self.__power = power

    def cook(self):
        if self.__power.voltage() > 50:
            print("Too much power!")
        else:
            if self.__power.live() == 1 and \
                    self.__power.neutral() == -1:
                print("Please wait, microwaving food.")
            else:
                print("There is no power.")

"""In main we 'plug' the microwave into adapter and adaptor in socket system"""
def main():
    # Plug in
    socket = Socket()
    adapter = Adapter(socket)
    microwave = Microwave(adapter)

    """This command starts the microwave"""
    microwave.cook()

    return 0


if __name__ == "__main__":
    main()

