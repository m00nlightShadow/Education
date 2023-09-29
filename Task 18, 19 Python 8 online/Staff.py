import traceback
from utils import working_days
from exceptions import EmailAlreadyExistsException, EmailTypeError
from datetime import datetime
import requests

YEAR = datetime.now().year
MONTH = datetime.now().month
URL = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'


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
        if '@' not in self.email:
            raise EmailTypeError(f'{self.email} has wrong type')
        else:
            with open("emails.csv", "r") as emails_csv:
                if self.email in emails_csv.read():
                    raise EmailAlreadyExistsException(f'{self.email} already in file emails.csv')

    def save_email(self):
        with open("emails.csv", "r+") as emails_csv:
            if self.email not in emails_csv.read():
                emails_csv.write(self.email + '\n')
            else:
                try:
                    self.validate()
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


class Candidate:
    def __init__(self,
                 first_name: str,
                 lastname: str,
                 email: str,
                 tech_stack: list,
                 main_skill: str,
                 main_skill_grade: str,
                 ):
        self.first_name = first_name
        self.lastname = lastname
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def full_name(self):
        return f'{self.first_name} {self.lastname}'

    @classmethod
    def generate_candidates(cls, url):
        candidates = []
        try:
            response = requests.get(url)
            if response.status_code == 200:
                lines = response.text.split('\n')
                for line in lines[1:]:
                    data = line.strip().split(',')
                    full_name = data[0]
                    email = data[1]
                    tech_stack = data[2].split('|')
                    main_skill = data[3]
                    main_skill_grade = data[4]
                    first_name, last_name = full_name.split(' ')
                    new_candidate = cls(first_name, last_name, email, tech_stack, main_skill, main_skill_grade)
                    candidates.append(new_candidate)
        finally:
            return candidates


howard = Candidate('Howard',
                   'Smith',
                   'HoSm@data.com',
                   tech_stack=['HTML', 'JavaScript', 'TypeScript', 'Django', 'Python'],
                   main_skill='Python',
                   main_skill_grade='Senior',
                   )

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


candidates_list = [candidate.full_name for candidate in Candidate.generate_candidates(URL)]
print(candidates_list)
