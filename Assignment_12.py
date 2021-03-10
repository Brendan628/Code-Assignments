def getNumbers(numberOfNumbers):
    numberList = []
    for NumberIndex in range(numberOfNumbers):
        userNumber = int(input("Enter number " + str((NumberIndex + 1)) + ": "))
        numberList.append(userNumber)
    return numberList
def findLowestNumber(numberList):
    lowestNumber = min(numberList)
    return lowestNumber
def findHighestNumber(numberList):
    highestNumber = max(numberList)
    return highestNumber
def calculateTotal(numberList):
    total = 0
    for NumberIndex in range(len(numberList)):
        total = total + numberList[NumberIndex]
    return total
def calculateAverage(numberList, total):
    totalNumberOfNumbers = len(numberList)
    average = total/totalNumberOfNumbers
    return average
def printnumbers(numberList, lowestNumber, highestNumber, total, average):
    print()
    print("Numbers provided:")
    for NumberIndex in range(len(numberList)):
        if NumberIndex == len(numberList) - 1:
            print(numberList[NumberIndex], end = ". " + "\n")
        else: print(numberList[NumberIndex], end = ", ")
    print("\nLowest number: " + str(lowestNumber), "\nHighest number: " + str(highestNumber),\
    "\nTotal of numbers: " + str(total), "\nAverage of numbers: " + str(average))
def main():
    NUMBER_OF_NUMBERS = 10
    numberList = []
    numberList = getNumbers(NUMBER_OF_NUMBERS)
    lowestNumber = findLowestNumber(numberList)
    highestNumber = findHighestNumber(numberList)
    total = calculateTotal(numberList)
    average = calculateAverage(numberList, total)
    printnumbers(numberList, lowestNumber, highestNumber, total, average)
main()