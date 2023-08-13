class Employee:

    def __init__(self, name: str, salary_per_day: int):
        self.name = name
        self.salary_per_day = salary_per_day

    def work(self):
        return 'I come to the office.'

    def __str__(self):
        return f'{self.__class__.__name__}: {self.name}'

    def __le__(self, other):
        return self.salary_per_day <= other.salary_per_day

    def __lt__(self, other):
        return self.salary_per_day < other.salary_per_day

    def __eq__(self, other):
        return self.salary_per_day == other.salary_per_day

    def __ge__(self, other):
        return self.salary_per_day >= other.salary_per_day

    def __gt__(self, other):
        return self.salary_per_day > other.salary_per_day


class Developer(Employee):
    def __init__(self, *args):
        super().__init__(*args)

    def work(self):
        return 'I come to the office and start to coding.'


class Recruiter(Employee):
    def __init__(self, *args):
        super().__init__(*args)

    def work(self):
        return 'I come to the office and start to hiring.'


alex = Developer('Alex', 1000)
tom = Recruiter('Tom', 200)
jack = Recruiter('Jack', 100)
terry = Recruiter('Terry', 150)
jane = Developer('Jane', 1200)

print(alex)
print(tom)
print(jack)
print(terry)
print(jane)
print(alex <= tom)
print(alex > terry)
print(jane > jack)
print(jack >= tom)
print(terry == jane)
