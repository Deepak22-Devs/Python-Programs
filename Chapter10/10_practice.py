from random import randint

class train:
    def __init__(self, trainNo):
        self.TrainNo = trainNo
    def book(self, fro , to):
        print(f"Ticket is booked in Train No: {self.TrainNo} from {fro} to {to}")
    def getstatus(self):
        print(f"Train no: {self.TrainNo} is running on time")
        pass
    def getfare(self, fro , to):
        print(f"Ticket fare in Train No: {self.TrainNo} from {fro} to {to} is {randint(222,5555)}")

t = train(23465)
t.book("Berhampur", "Puri")
t.getstatus()
t.getfare("Berhampur", "Puri")
