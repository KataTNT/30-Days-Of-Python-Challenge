"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 21 - Classes and Objects (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/21_Day_Classes_and_objects/21_classes_and_objects.md)
Challenger: KataTNT
"""

## Exercise: Level 1
# 1.
from math import sqrt

class Statistics:
    def __init__(self, data: list[int | float]):
        self.data = data
    def count(self) -> int:
        return len(self.data)
    def sum(self) -> int | float:
        return sum(self.data)
    def min(self):
        return min(self.data) 
    def max(self):
        return max(self.data)
    def range(self):
        return self.max() - self.min()
    def mean(self):
        return self.sum() / self.count()
    def median(self):
        sorted_self = sorted(self.data)
        median_index = len(sorted_self) // 2
        if len(sorted_self) % 2 != 0:
            return sorted_self[median_index]
        else:
            return (sorted_self[median_index - 1] + sorted_self[median_index]) / 2
    def mode(self):
        mode = None
        count_table = {}
        for item in self.data:
            if not item in count_table:
                count_table[item] = 1
            else:
                count_table[item] += 1
        for item, count in count_table.items():
            if count == max(count_table.values()):
                mode = item
                return {'mode': mode, 'count': count}
    def var(self):
        x = []
        for xi in self.data:
            x.append((xi, (xi - self.mean()) ** 2))
        ss = 0
        for xi, s in x:
            ss += s
        return ss / (self.count() - 1)
    def std(self):
        return sqrt(self.var())
    def describe(self):
        print('Count:', self.count())
        print('Sum:', self.sum())
        print('Min:', self.min())
        print('Max:', self.max())
        print('Range:', self.range())
        print('Mean:', self.mean())
        print('Median:', self.median())
        print('Mode:', self.mode())
        print('Standard Deviation:', self.std()) 
        print('Variance:', self.var()) 
        # print('Frequency Distribution:', data.freq_dist())

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
data.describe()

