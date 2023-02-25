class FilterPrime():
    def isPrime(self, number):
        if (number < 2):
            return False
        else:
            for i in range(2, number):
                if(number % i == 0):
                    return False
        return True   

    def filterPrimes(self, listofnums):
        return filter(lambda x : self.isPrime(x), listofnums)

prime_filter = FilterPrime()
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
prime_numbers = list(prime_filter.filterPrimes(nums))
print(prime_numbers)