import unittest
from Staff import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.employee = Employee("Name", 300, "name@example.com")

    def test_work(self):
        self.assertEqual(self.employee.work(), "I come to the office")

    def test_salary_calculation(self):
        self.employee.check_salary()


if __name__ == '__main__':
    unittest.main()
