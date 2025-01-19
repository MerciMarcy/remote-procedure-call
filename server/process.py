import math


class Process:
    def __init__(self, method, params):
        self.method = method
        self.params = params

    def floor(self, params):
        x = params[0]
        return math.floor(x)

    def n_root(self, params):
        n = params[0]
        x = params[1]
        return math.pow(x, 1 / n)

    def reverse(self, params):
        s = params[0]
        return s[::-1]

    def valid_anagram(self, params):
        str1 = params[0]
        str2 = params[1]
        if len(str1) != len(str2):
            return False
        return sorted(str1) == sorted(str2)

    def sort(self, params):
        strArr = params[0]
        return sorted(strArr)

    def execute(self):
        process_table = {
            "floor": self.floor,
            "nroot": self.n_root,
            "validAnagram": self.valid_anagram,
            "sort": self.sort,
        }
        try:
            return process_table[self.method](self.params)
        except:
            raise ValueError("request error")
