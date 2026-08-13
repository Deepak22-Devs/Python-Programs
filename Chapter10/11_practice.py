from random import randint

class train:
    def __init__(slf, trainNo):
        slf.TrainNo = trainNo
    def book(slf, fro , to):
        print(f"Ticket is booked in Train No: {slf.TrainNo} from {fro} to {to}")
    def getstatus(slf):
        print(f"Train no: {slf.TrainNo} is running on time")
        pass
    def getfare(slf, fro , to):
        print(f"Ticket fare in Train No: {slf.TrainNo} from {fro} to {to} is {randint(222,5555)}")

t = train(23465)
t.book("Berhampur", "Puri")
t.getstatus()                                                          
t.getfare("Berhampur", "Puri")
