class Check:
    @staticmethod
    def me(value1: float, value2: float) -> bool:
        return value1 > value2
    
    @staticmethod
    def eq(value1: float, value2: float) -> bool:
        return value1 == value2
    
    @staticmethod
    def le(value1: float, value2: float) -> bool:
        return value1 < value2
    
    @staticmethod
    def meeq(value1: float, value2: float) -> bool:
        return value1 > value2 or value1 == value2
    
    @staticmethod
    def leeq(value1: float, value2: float) -> bool:
        return value1 < value2 or value1 == value2
    
    @staticmethod
    def min(value1: float, value2: float):
        return value1 if Check.le(value1, value2) else value2
    
    @staticmethod
    def max(value1: float, value2: float):
        return value1 if Check.me(value1, value2) else value2
    
    @staticmethod
    def clamp(value1: float, min: float, max: float):
        return Check.max(min, Check.min(value1, max))
    
    @staticmethod
    def floor(value: float):
        return (value * 100 + 0.5 - (value * 100 + 0.5)%1)/100
    

class MathService:
    @staticmethod
    def add(value1: float, value2: float) -> float:
        return value1 + value2
    
    @staticmethod
    def sub(value1: float, value2: float) -> float:
        result = value1 - value2
        if Check.leeq(result, 0):
            return 0
        return result
    
    @staticmethod
    def mul(value1: float, value2: float) -> float:
        return value1 * value2
    
    @staticmethod
    def div(value1: float, value2: float) -> float:
        if Check.eq(value2, 0):
            raise ValueError("Cannot divide by zero.")
        result = value1 / value2
        if Check.leeq(result, 0):
            return 0
        return result
    
    @staticmethod
    def pow(value1: float, value2: float) -> float:
        return value1 ** value2
    
    @staticmethod
    def log_notation(x: float) -> float:
        if Check.leeq(x, 0):
            raise ValueError("x must be positive")
        if Check.eq(x, 1):
            return 0.0
        sub = MathService.sub
        div = MathService.div
        add = MathService.add
        mul = MathService.mul
        app = 0.0
        term = div(sub(x, 1), add(x, 1))
        term2 = mul(term, term)
        num = term
        den = 1
        n = 1000

        for _ in range(n):
            app += div(num, den)
            num *= term2
            den += 2

        return mul(2, app)
    
    @staticmethod
    def log(value1: float, value2: float) -> float:
        try:
            if Check.leeq(value1, 0) or Check.leeq(value2, 0) or Check.eq(value2, 1):
                raise ValueError("Both value1 and value2 must be positive and value2 must be 1 or more.")

            ln1 = MathService.log_notation(value1)
            ln2 = MathService.log_notation(value2)
            result = MathService.div(ln1, ln2)
            return result
        except ValueError as e:
            print(f"Error: {e}")
            return None

    @staticmethod
    def to_float(var: str) -> float:
        try:
            return float(var)
        except ValueError:
            print("Cant take anything else")