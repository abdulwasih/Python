limit = int(input("Enter the limit"))
list = []


def details(name, age, height, mark):
    dic = {"name": name, "age": age, "height": height, "mark": mark}
    return dic

def takeSecond(elem):
    return elem[1]

#list.append(details("wasih", 23, 170, 90))

#list.append(details("shamli", 23, 165, 95))
#list.append(details("razal", 23, 167, 90))

for i in range(limit):
    name = input("Enter the name : ")
    age = int(input("Enter the age : "))
    height = float(input("Enter the height : "))
    mark = int(input('Enter the mark : '))
    list.append(details(name, age, height, mark))

    print(list)

list.sort(key=dic.value())


