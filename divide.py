from main import ArithmeticOpsInterface

class DivideOp(ArithmeticOpsInterface):
    def add(self, a: int, b: int) -> int:
        '''Add the given numbers'''
        pass

    def subtract(self, a: int, b: int) -> int:
        '''Subtract b from a'''
        pass

    def multiply(self, a: int, b: int) -> int:
        '''Multiply the given numbers'''
        pass

    def divide(self, a: int, b: int) -> int:
        '''Divide a with b'''
        return a/b