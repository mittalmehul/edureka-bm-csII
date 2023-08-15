from main import ArithmeticOpsInterface

class AdditionOp(ArithmeticOpsInterface):
    
    def add(self, a: int, b: int) -> int:
        return a + b
    
    def subtract(self, a: int, b: int) -> int:
        '''Subtract b from a'''
        pass

    def multiply(self, a: int, b: int) -> int:
        '''Multiply the given numbers'''
        pass

    def divide(self, a: int, b: int) -> int:
        '''Divide a with b'''
        pass