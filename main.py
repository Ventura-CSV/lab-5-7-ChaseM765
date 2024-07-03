
def splitlist(numbers):
    #first = min(numbers)
    first = numbers[0]
    for x in numbers:
        if x < first:
            first = x    
    
    ind = numbers.index(first)
    mem = numbers[0]
    numbers[0] = numbers[ind]
    numbers[ind] = mem
    
    
    
    #mem = numbers[0]
    #numbers[0] = numbers[4]
    #numbers[4] = mem
    numbers.remove(first)
    
    return first, numbers
    
    


def main():

    numbers = [5, 4, 3, 2, 1]

    first, others = splitlist(numbers)
    print(first)  # Expected output     1
    print(others)  # Expected output     4 3 2 5


if __name__ == '__main__':
    main()
