class FizBuz:
    
    length = 100
    
    def get_generator(self):
        return (self.check_number(i) for i in range(1, self.length+1))
        
    def check_number(self, i):
        if i % 3 == 0 and i % 5 == 0:
            return 'FizzBuzz'
        elif i % 3 == 0: 
            return 'Fizz'
        elif i % 5 == 0:
            return 'Buzz'
        else:
            return i
    
    
    def get_generatorb(self):
        for i in range(1, self.length+1):
            if i % 3 == 0 and i % 5 == 0:
                yield 'FizzBuzz'
            elif i % 3 == 0: 
                yield 'Fizz'
            elif i % 5 == 0:
                yield 'Buzz'
            else:
                yield i

