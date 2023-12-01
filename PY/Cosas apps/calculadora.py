
class Calculadora:
    def __init__(self, num, num2):
        self.num = num
        self.num2 = num2
    
    def sum(self):
        result = self.num + self.num2
        return result
    def rest(self):
        result = self.num - self.num2
        return result
    def mult(self):
        result = self.num * self.num2
        return result
    def div(self):
        result = self.num / self.num2
        return result
    
parameter = Calculadora(3,2)


print (parameter.sum(), parameter.rest(), parameter.mult(), parameter.div())