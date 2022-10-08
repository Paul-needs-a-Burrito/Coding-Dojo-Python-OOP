# Assignment: MathDojo
# Objectives:
#     Practice creating a class and creating new instances
#     Practice chaining methods
#     Practice writing flexible functions that can take a varying number of arguments
# 1) Create a Python class called MathDojo that has one attribute, result, and 2 methods: add and subtract. The 2 methods each must take at least 1 parameter, but could take many more.
# 2) Write the add method and test it by calling it 3 times, with different numbers of arguments each time
# 3) Write the subtract method and test it by calling it 3 times, with different numbers of arguments each time
# 4) Make sure you are able to chain methods


class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for i in nums:
            self.result += i
        return self

    def subtract(self, num, *nums):
        self.result -= num
        for i in nums:
            self.result -= i
        return self


mathdojoinstance = MathDojo()

x = mathdojoinstance.add(1).add(1,1,1,1,1,1).add(2,11).subtract(1,1,1,1).subtract(3).subtract(1,2).result

print(x)
