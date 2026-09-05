"""
Project: 30 Days Of Python challenge
Author (Original): Asabeneh Yetayeh (https://github.com/Asabeneh/30-Days-Of-Python)
Day: 21 - Classes and Objects (https://github.com/Asabeneh/30-Days-Of-Python/blob/master/21_Day_Classes_and_objects/21_classes_and_objects.md)
Challenger: KataTNT
"""

## Exercise: Level 1
# 1. Python has the module called statistics and we can use this module to do all the statistical calculations. However, to learn how to make function and reuse function let us try to develop a program, which calculates the measure of central tendency of a sample (mean, median, mode) and measure of variability (range, variance, standard deviation). In addition to those measures, find the min, max, count, percentile, and frequency distribution of the sample. You can create a class called Statistics and create all the functions that do statistical calculations as methods for the Statistics class. Check the output below.
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
                return {"mode": mode, "count": count}
            
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

    def freq_dist(self):
        count_table = {}
        for item in self.data:
            if not item in count_table:
                count_table[item] = 1
            else:
                count_table[item] += 1
        result = []
        for k, v in count_table.items():
            count_self = self.count()
            result.append((k, v / count_self * 100))
        result.sort(key=lambda x: x[0])
        return result
    
    def describe(self):
        print("Count:", self.count())
        print("Sum:", self.sum())
        print("Min:", self.min())
        print("Max:", self.max())
        print("Range:", self.range())
        print("Mean:", self.mean())
        print("Median:", self.median())
        print("Mode:", self.mode())
        print("Standard Deviation:", self.std()) 
        print("Variance:", self.var()) 
        print("Frequency Distribution:", self.freq_dist())

ages = [31, 26, 34, 37, 27, 26, 32, 32, 26, 27, 27, 24, 32, 33, 27, 25, 26, 38, 37, 31, 34, 24, 33, 29, 26]
data = Statistics(ages)
data.describe()

## Exercises: Level 2
# 1. Create a class called PersonAccount. It has firstname, lastname, incomes, expenses properties 
# and it has total_income, total_expense, account_info, add_income, add_expense and account_balance methods. 
# Incomes is a set of incomes and its description. The same goes for expenses.
class PersonAccount:
    def __init__(self, firstname: str, lastname: str, incomes: list, expenses: list):
        self.firstname = firstname
        self.lastname = lastname
        self.incomes = incomes
        self.expenses = expenses

    def total_income(self):
        return sum(income["amount"] for income in self.incomes)
    
    def total_expense(self):
        return sum(expense["amount"] for expense in self.expenses)
    
    def account_info(self):
        print("---Account Information---")
        print("Firstname:", self.firstname)
        print("Lastname:", self.lastname)
        print("Incomes:")
        for income in self.incomes:
            print(f"+{income["amount"]}: {income["description"]}")
        print("Expenses:")
        for expense in self.expenses:
            print(f"-{expense["amount"]}: {expense["description"]}")
        print("Account balance:", self.account_balance())

    def add_income(self, amount, description):
        if amount <= 0:
            print("Invalid income amount!")
            return
        init_length = len(self.incomes)
        try:
            self.incomes.append({"amount": amount, "description": description})

            if len(self.incomes) == init_length + 1:
                print(f"Income added successfully!")
            else:
                print("Failed to add income!")
        except Exception as e:
            print(f"An error occurred while adding income: {e}")

    def add_expense(self, amount, description):
        if amount <= 0:
            print("Invalid expense amount!")
            return
        init_length = len(self.expenses)
        try:
            self.expenses.append({"amount": amount, "description": description})

            if len(self.expenses) == init_length + 1:
                print(f"Expense added successfully!")
            else:
                print("Failed to add expense!")
        except Exception as e:
            print(f"An error occurred while adding expense: {e}")

    def account_balance(self):
        return self.total_income() - self.total_expense()

ken_account = PersonAccount("Ken", "Kaneki", [{"amount": 800, "description": "salary"}], [{"amount": 500, "description": "renting"}])
ken_account.add_income(300, "overtime pay")
ken_account.add_expense(30, "food")
ken_account.add_expense(55, "books")
ken_account.account_info()
