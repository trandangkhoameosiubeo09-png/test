class Vehicle():
    def __init__(self, licensePlateNumber, price, status):
        self.licensePlateNumber = licensePlateNumber
        self.price = price
        self.status = status

    def adjustTotal(self, total, days):
        return total

class Motorbike(Vehicle):
    def __init__(self, licensePlateNumber, price, status, cc):
        super().__init__(licensePlateNumber, price, status)
        self.cc = cc

    def adjustTotal(self, total, days):
        if self.cc >= 50:
            total *= 1.1

        return total
    
class Car(Vehicle):
    def __init__(self, licensePlateNumber, price, status, seats):
        super().__init__(licensePlateNumber, price, status)
        self.seats = seats

    def adjustTotal(self, total, days):
        if days > 5:
            total *= 0.85

        return total

class ElectricalBike(Vehicle):
    def __init__(self, licensePlateNumber, price, status, PinPercentage):
        super().__init__(licensePlateNumber, price, status)
        self.PinPercentage = PinPercentage

        def adjustTotal(self, total, days):
            return total

class Customers():
    def __init__(self, name, phoneNumber, deposit):
        self.name = name
        self.phoneNumber = phoneNumber
        self.__deposit = deposit

    def getDeposit(self):
        return self.__deposit

    def AddDeposit(self, added):
        self.__deposit += added

    def setDeposit(self, val):
        self.__deposit = val

class Rent():
    def __init__(self, Vehicle, days, rentDay, customer):
        self.Vehicle = Vehicle
        self.days = days
        self.rentDay = rentDay
        self.customer = customer

    def Total(self):
        total = self.Vehicle.price * self.days

        total = self.Vehicle.adjustTotal(total, self.days)

        return total

    def checkDeposit(self):
        total = self.Total()
        deposit = self.customer.getDeposit()

        if deposit < total * 0.3:
            print(f"Your deposit isn't enough to rent {self.Vehicle.__class__.__name__} {self.Vehicle.licensePlateNumber} for {self.days} days")

            return False

        return True

def AddCustomer(customers):
    name = input("Name: ")
    phoneNumber = int(input("PhoneNumber: "))
    deposit = int(input("Deposit: "))
    customers.append(Customers(name, phoneNumber, deposit))
    print(f'Customer {name} with {phoneNumber} and {deposit} vnd on account has been added successfully')

def AddVehicle(vehicles):

    type = input(
        "Press C to add a Car\n"
        "Press E to add a Electricalbike\n"
        "Press M to add a Motobike\n"
    ).lower()
    licensePlateNumber = input("LicensePlateNumber: ")
    price = int(input("Price: "))
    status = input("Status: ")

    if type == 'c':
        seats = int(input("Seats: "))
        car = Car(licensePlateNumber, price, status, seats)
        vehicles.append(car)

        print(f"Car ({seats} seats) with license plate {licensePlateNumber} and status {status} has been added successfully. The rental price per day is {price} vnd")

    if type == 'e':
        pinPercentage = int(input("PinPercentage: "))
        electricalBike = ElectricalBike(licensePlateNumber, price, status, pinPercentage)
        vehicles.append(electricalBike)

        print(f"ElectricalBike with license plate {licensePlateNumber}, {pinPercentage}% pin and status {status} has been added successfully. The rental price per day is {price} vnd")

    if type == 'm':
        cc = int(input("CC: "))
        motorbike = Motorbike(licensePlateNumber, price, status, cc)
        vehicles.append(motorbike)

        print(f"Motobike with license plate {licensePlateNumber}, {cc}cc and status {status} has been added successfully. The rental price per day is {price} vnd")

def AddDeposit(customers):
    phonenumber = int(input("Phonenumber: "))

    for customer in customers:
        if customer.phoneNumber == phonenumber:
            add = int(input("Add: "))
            customer.AddDeposit(add)
            print(f"{add} vnd has been added to {phonenumber}")

            return 

    print("PhoneNumber not found")
        
def RemoveVehicle(vehicles):
    plate = input("LicensePlateNumber: ")

    for vehicle in vehicles:
        if vehicle.licensePlateNumber == plate:
            vehicles.remove(vehicle)
            print(f"{plate} has been removed")

            return
        
    print("Vehicle not found.")

def RentVehicle(vehicles, rents, customer):
    vehicleType = input(
            "Press C to rent a Car\n"
            "Press E to rent a Electricalbike\n"
            "Press M to rent a Motorbike\n"
        ).lower()
    
    print("Available vehicles:")

    for vehicle in vehicles:
        if vehicle.status == "available":

            if vehicleType == "c" and vehicle.__class__.__name__ == "Car":
                print(vehicle.licensePlateNumber)

            elif vehicleType == "e" and vehicle.__class__.__name__ == "ElectricalBike":
                print(vehicle.licensePlateNumber)

            elif vehicleType == "m" and vehicle.__class__.__name__ == "MotorBike":
                print(vehicle.licensePlateNumber)

    plate = input("Choose license plate: ")

    for vehicle in vehicles:
        if vehicle.licensePlateNumber == plate:

            if (vehicleType == "c" and vehicle.__class__.__name__ == "Car") or \
           (vehicleType == "e" and vehicle.__class__.__name__ == "ElectricalBike") or \
           (vehicleType == "m" and vehicle.__class__.__name__ == "MotorBike"):

                if vehicle.status != "available":
                    print("Vehicle is not available.")
                    return

                days = int(input("How many days do you want to rent: "))
                rentDay = int(input("Rent day: "))

                rent = Rent(vehicle, days, rentDay, customer)

                if rent.checkDeposit():
                    print("Total:", rent.Total(), "vnd")

                    vehicle.status = "unavailable"

                    rents.append(rent)

                    print("Vehicle rented successfully.")

                return

    print("Vehicle not found.")

def ReturnVehicle(rents):

    plate = input("License plate: ")

    for rent in rents:

        if rent.Vehicle.licensePlateNumber == plate:
            vehicle = rent.Vehicle

            returnDay = int(input("Return day: "))

            expectedReturnDay = rent.rentDay + rent.days

            lateDays = 0

            if returnDay > expectedReturnDay:
                lateDays = returnDay - expectedReturnDay

            total = rent.Total()
            total += lateDays * vehicle.price

            if vehicle.__class__.__name__ == "Electricalbike":
                PinPercentage = int(input("Current Pin Percent: "))

                if PinPercentage < 50:
                    total += 100000

            print("Late days:", lateDays)
            print("Total:", total, "vnd")

            customer = rent.customer

            deposit = customer.getDeposit()

            remaining = deposit - total

            if remaining >= 0:
                print("Refund:", remaining, "vnd")
            else:
                print("Additional payment:", -remaining, "vnd")

            customer.setDeposit(0)

            vehicle.status = "available"

            rents.remove(rent)

            print("Vehicle returned successfully")
            return

    print("Vehicle not found.")

def Menu(vehicles, customers, rents):
    while True:
        selectFunction = int(input(
            "Press 1 to add customer\n"
            "Press 2 to add vehicle\n"
            "Press 3 to remove vehicle\n"
            "Press 4 to add deposit\n"
            "Press 5 to rent vehicle\n"
            "Press 6 to return vehicle\n"
            "Press 0 to exit\n"  
            "Choose: "          
        ))

        if selectFunction == 1:
            AddCustomer(customers)

        elif selectFunction == 2:
            AddVehicle(vehicles)

        elif selectFunction == 3:
            RemoveVehicle(vehicles)

        elif selectFunction == 4:
            AddDeposit(customers)

        elif selectFunction == 5:
            phoneNumber = int(input("Phone number: "))

            for customer in customers:
                if customer.phoneNumber == phoneNumber:
                    RentVehicle(vehicles, rents, customer)

        elif selectFunction == 6:
            ReturnVehicle(rents)

        elif selectFunction == 0:
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

def Main():
    vehicles = []
    customers = []
    rents = []

    Menu(vehicles, customers, rents)

Main()