def solution(l):
    sorted_list = sorted(l)
    sorted_list = sorted(l, key=lambda l: createArray(l))

    return sorted_list
    
def createArray(l):
    arrayOfStrings = l.split(".")
    if (len(arrayOfStrings) == 1):
        arrayOfStrings.append("-1")
        arrayOfStrings.append("-1")
    elif (len(arrayOfStrings) == 2):
        arrayOfStrings.append("-1")
    
    arrayOfNumbers = list(map(int, arrayOfStrings))

    return arrayOfNumbers

realtest1 = ["1.11", "2.0.0", "1.2", "2", "0.1", "1.2.1", "1.1.1", "2.0"]
realtest2 = ["1.1.2", "1.0", "1.3.3", "1.0.12", "1.0.2"]

print(solution(realtest1))
print(solution(realtest2))