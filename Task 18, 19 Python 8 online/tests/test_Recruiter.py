import unittest
from Staff import Recruiter



class TestRecruiter(unittest.TestCase):
    def setUp(self):
        self.recruiter = Recruiter("Name", 300, "name@example.com")

    def test_work(self):
        self.assertEqual(self.recruiter.work(), "I come to the office and start to hiring.")
