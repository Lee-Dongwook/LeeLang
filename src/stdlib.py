import time
import math

class Stdlib:
    
    @staticmethod
    def length(value):
        if isinstance(value, str):
            return len(value)
        raise Exception("lengt() expects a string")
    
    @staticmethod
    def uppercase(value):
        if isinstance(value, str):
            return value.upper()
        raise Exception("uppercase() expects a string")

    @staticmethod
    def lowercase(value):
        if isinstance(value, str):
            return value.lower()
        raise Exception("lowercase() expects a string")
    
    @staticmethod
    def sqrt(value):
        return math.sqrt(value)

    @staticmethod
    def abs(value):
        return abs(value)

    @staticmethod
    def pow(base, exponent):
        return math.pow(base, exponent)

    @staticmethod
    def time():
        return time.time()

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)
