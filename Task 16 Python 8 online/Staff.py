import utils

YEAR = 2023
MONTH = 8


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

    '''You can enter the number of days for salary calculation,
     or the calculation will be made for the number of working 
     days from the beginning of the current month'''
    def check_salary(self):
        count_of_days = input(f"Нow many days to count for {self.name}'s salary?\n")
        if not count_of_days:
            return f"{self.name}'s salary - {self.salary_per_day * len(utils.working_days(YEAR, MONTH))}"
        else:
            return f"{self.name}'s salary - {self.salary_per_day * int(count_of_days)}"


class Developer(Employee):
    def __init__(self, name: str, salary_per_day: int, tech_stack: list):
        super().__init__(name, salary_per_day)
        self.tech_stack = tech_stack

    def work(self):
        return 'I come to the office and start to coding.'

    def __le__(self, other):
        return len(self.tech_stack) <= len(other.tech_stack)

    def __lt__(self, other):
        return len(self.tech_stack) < len(other.tech_stack)

    def __eq__(self, other):
        return len(self.tech_stack) == len(other.tech_stack)

    def __ge__(self, other):
        return len(self.tech_stack) >= len(other.tech_stack)

    def __gt__(self, other):
        return len(self.tech_stack) > len(other.tech_stack)

    def __add__(self, other):
        if isinstance(other, Developer):
            name = self.name + " " + other.name
            tech_stack = list(set(self.tech_stack + other.tech_stack))
            salary_per_day = max(self.salary_per_day, other.salary_per_day)
            return Developer(name, salary_per_day, tech_stack)


class Recruiter(Employee):
    def work(self):
        return 'I come to the office and start to hiring.'


alex = Developer('Alex', 1000, ['HTML', 'JavaScript', 'TypeScript', 'Django', 'Python'])
tom = Recruiter('Tom', 200)
jack = Recruiter('Jack', 100)
terry = Recruiter('Terry', 150)
jane = Developer('Jane', 1200, ['HTML', 'CSS', 'JavaScript', 'TypeScript', 'SQL'])
new_developer = alex + jane

# Team
print(alex)
print(tom)
print(jack)
print(terry)
print(jane)

# Start working
print(alex.work())
print(tom.work())
print(jack.work())
print(terry.work())
print(jane.work())

# Monthly salary
print(tom.check_salary())
print(jack.check_salary())
print(terry.check_salary())
print(jane.check_salary())
print(alex.check_salary())

# Adding developer Class
print(new_developer.name)
print(new_developer.tech_stack)
print(new_developer.salary_per_day)

# Comparing the salaries of employees
print(alex.salary_per_day <= tom.salary_per_day)
print(alex.salary_per_day > terry.salary_per_day)
print(jane.salary_per_day > jack.salary_per_day)
print(jack.salary_per_day >= tom.salary_per_day)
print(terry.salary_per_day == jane.salary_per_day)
print(alex.salary_per_day > jane.salary_per_day)

# Comparing tech stack of Developers
print(alex.tech_stack > jane.tech_stack)
