# Student Test Score Calculator

import math

class Student():
    # Class constructor
    def __init__(self, name, firstTest, secondTest):
        self.Name=name
        self.FirstTest=firstTest
        self.SecondTest=secondTest

    # Method that calculates final classification of a student
    def FinalClassification(self):
        return math.floor((self.FirstTest + self.SecondTest)/2+0.5)
    

if __name__ == "__main__":
    student = Student("Bárbara Oliveira", 14, 16)
    print(f"{student.Name} had the final classification of {student.FinalClassification()}.")