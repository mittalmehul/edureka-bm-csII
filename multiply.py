from main import ArithmeticOpsInterface

class MultiplyOp(ArithmeticOpsInterface):
    def add(self, a: int, b: int) -> int:
        '''Add the given numbers'''
        pass

    def subtract(self, a: int, b: int) -> int:
        '''Subtract b from a'''
        pass

    def multiply(self, a: int, b: int) -> int:
        '''Multiply the given numbers'''
        return a*b

    def divide(self, a: int, b: int) -> int:
        '''Divide a with b'''
        pass