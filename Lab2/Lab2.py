from file_manager import FileManager

# Zad 1

def foo(a_list, b_list):
    c_list = []
    for i in range(len(a_list)):
        if(i % 2 == 0):
            c_list.append(a_list[i])
    for i in range(len(b_list)):
        if(i % 2 == 1):
            c_list.append(b_list[i])
    print(c_list)


x = [1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d"]
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, "a", "b", "c", "d"]

foo(x, y)

# Zad 2


def foo1(data_text):
    tab = []
    for i in range(len(data_text)):
        tab.append(data_text[i])

    dic = {
        "Długość": len(data_text),
        "Litery": tab,
        "Drukowane": data_text.upper(),
        "Małe": data_text.lower()
    }

    print(dic)


z = "qwertyuiop"

foo1(z)

# Zad 3


def foo2(text, letter):
    for i in letter:
        if i in text:
            text = text.replace(i, "")
    print(text)


c = "Rabarbar"
lit = "a"

foo2(c, lit)

# Zad 4

def foo3(temperature_type, num_of_temp):
    temperature_type = temperature_type.lower()
    if(temperature_type == "kelwin"):
        kelwin = num_of_temp + 273.15
        return kelwin
    elif(temperature_type == "fahrenheit"):
        fahrenheit = (num_of_temp * 1.8000) + 32.00
        return fahrenheit
    elif(temperature_type == "rankine"):
        rankine = (num_of_temp * 1.8000) + 491.67
        return rankine
    else:
        print("Podana nazwa nie jest obsługiwana!")

print("Temperatura w Kelwin",foo3("Kelwin", 0))
print("Temperatura w Fahrenheit",foo3("Fahrenheit", 0))
print("Temperatura w Rankine",foo3("Rankine", 0))
print("Temperatura w ",foo3("Rankine23", 0))

# Zad 5

class Calculator:
    def add(a, b):
        return(a+b)

    def difference(a, b):
        return(a-b)

    def multiply(a, b):
        return(a*b)

    def divide(a, b):
        return(a/b)


print("Dodawanie: ", Calculator.add(1, 2))
print("Odejmowanie: ", Calculator.difference(1, 2))
print("Mnożenie: ", Calculator.multiply(1, 2))
print("Dzielenie: ", Calculator.divide(1, 2))

# Zad 6


class ScienceCalculator(Calculator):
    def potegowanie(a, b):
        return(a**b)


print("Dodawanie: ", ScienceCalculator.add(1, 2))
print("Odejmowanie: ", ScienceCalculator.difference(1, 2))
print("Mnożenie: ", ScienceCalculator.multiply(1, 2))
print("Dzielenie: ", ScienceCalculator.divide(1, 2))
print("Potegowanie", ScienceCalculator.potegowanie(2, 2))

# Zad 7

def foo4(text):
    print(text[::-1])

text = "Patryk"
foo4(text)

# Zad 9


FileManager.update_file("./Lab2/test.txt")
FileManager.read_file("./Lab2/test.txt")
