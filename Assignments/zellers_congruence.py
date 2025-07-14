class DateCalculator:
    def __init__(self, day: int, month: int, year: int):
        self.daysOfTheWeek = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
        self.day = day

        if month < 3:
            self.month = month + 12
            self.year = year - 1
        else:
            self.month = month
            self.year = year

    def getDay(self):
        K = self.year % 100
        J = self.year // 100
        day = (self.day + (13 * (self.month + 1)) // 5 + K + (K // 4) + J // 4 + 5 * J) % 7
        return self.daysOfTheWeek[day]

dateCalculator1 = DateCalculator(10, 2, 2006)
print(dateCalculator1.getDay())