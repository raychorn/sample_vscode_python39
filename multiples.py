import timeit

def isMultiple(num):
	return ( (num % 5 == 0) or (num % 3 == 0) )

if (__name__ == '__main__'):
    def main():
        starttime = timeit.default_timer()
        sumOfMultiples = 0

        for i in range(0, 1000):
            if (isMultiple(i)):
                sumOfMultiples += i
        print("Sum is {}".format(sumOfMultiples))
        elapsed = timeit.default_timer() - starttime
        print("Time elapsed is: {} {:.2f} ms".format(elapsed, elapsed * 10**5))

    main()

