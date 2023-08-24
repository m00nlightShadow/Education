import traceback
from utils import working_days
from exceptions import EmailAlreadyExistsException
from datetime import datetime


YEAR = datetime.now().year
MONTH = datetime.now().month


class Employee:
    def __init__(self,
                 name: str,
                 salary_per_day: int,
                 email: str,
                 ):
        self.name = name
        self.salary_per_day = salary_per_day
        self.email = email
        self.save_email()

    def work(self):
        return 'I come to the office'

    def validate(self):
        with open("emails.csv", "r") as emails_csv:
            if self.email in emails_csv.read():
                raise EmailAlreadyExistsException(f'{self.email} already in file emails.csv')

    def save_email(self):
        with open("emails.csv", "a") as emails_csv:
            try:
                self.validate()
                emails_csv.write(self.email + '\n')
            except EmailAlreadyExistsException:
                with open('logs.txt', 'a') as logs:
                    logs.write(f'{datetime.now()} | {traceback.format_exc()} \n')

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
            return f"{self.name}'s salary - {self.salary_per_day * len(working_days(YEAR, MONTH))}"
        else:
            return f"{self.name}'s salary - {self.salary_per_day * int(count_of_days)}"


class Developer(Employee):
    def __init__(self, *args, tech_stack: list, **kwargs):
        super().__init__(*args, **kwargs)
        self.tech_stack = tech_stack

    def work(self):
        return super().work() + ' and start to coding.'

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
            email = self.email.split('@')[0] + other.email.split('@')[0] + '@' + self.email.split('@')[1]
            return Developer(name, salary_per_day, email, tech_stack=tech_stack)


class Recruiter(Employee):
    def work(self):
        return super().work() + ' and start to hiring.'


alex = Developer('Alex',
                 salary_per_day=1000,
                 email='alex@gmail.com',
                 tech_stack=['HTML', 'JavaScript', 'TypeScript', 'Django', 'Python'],
                 )
tom = Recruiter('Tom',
                salary_per_day=200,
                email='tom@gmail.com',
                )
jack = Recruiter('Jack',
                 salary_per_day=100,
                 email='jack@gmail.com',
                 )
jane = Developer('Jane',
                 salary_per_day=1200,
                 email='jane@gmail.com',
                 tech_stack=['HTML', 'CSS', 'JavaScript', 'TypeScript', 'SQL'],
                 )

new_developer = alex + jane

# Team
print(alex)
print(tom)
print(jack)
print(jane)

# Start working
print(alex.work())
print(tom.work())
print(jack.work())
print(jane.work())

# Monthly salary
print(tom.check_salary())
print(jack.check_salary())
print(jane.check_salary())
print(alex.check_salary())

# Adding developer Class
print(new_developer.name)
print(new_developer.tech_stack)
print(new_developer.salary_per_day)
print(new_developer.email)

# Comparing the salaries of employees
print(alex.salary_per_day <= tom.salary_per_day)
print(jane.salary_per_day > jack.salary_per_day)
print(jack.salary_per_day >= tom.salary_per_day)
print(alex.salary_per_day > jane.salary_per_day)

# Comparing tech stack of Developers
print(alex.tech_stack > jane.tech_stack)
