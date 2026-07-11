marks = {
    "Harry": 100,
    "Shubam": 56,
    "Rohan": 23,
    0 : "Deepak",

}

# print(marks.items())
# print(marks.keys())
# print(marks.values())


# marks.update({"Harry":99, "Deepak" : 89})
# print(marks)

# print(marks.get("Harry"))
# print(marks["Harry"])
print(marks.get("Harry2"))  #print none
# print(marks["Harry2"])    #Return an error


marks.pop("Rohan")
marks.setdefault("Dipu", 582)
# marks.clear()
marks.copy()
print(marks)