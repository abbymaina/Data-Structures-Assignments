class DayCalculator:
    def __init__(self, year, month, day):
        self.year = year - (month < 3)
        self.month = month + 12 if month < 3 else month
        self.day = day

    def get_weekday(self):
        q, m, Y = self.day, self.month, self.year
        K, J = Y % 100, Y // 100

        h = (q + (13 * (m + 1) // 5) + K + (K // 4) + (J // 4) + 5 * J) % 7

        return ["Saturday", "Sunday", "Monday", "Tuesday",
                "Wednesday", "Thursday", "Friday"][h]


date = DayCalculator(1589, 9, 15)
print(f"September 15, 1589 was a {date.get_weekday()}")