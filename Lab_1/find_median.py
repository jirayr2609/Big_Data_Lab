import sys
if __name__=='__main__':
    numbers=[]
    for filename in sys.argv[1:]:
        with open(filename,'rb') as fi:
            for line in fi:
                numbers.append(int(line))
    numbers.sort()
    print(numbers[int(len(numbers)/2)])
    #print(numbers[len(numbers)//2])
