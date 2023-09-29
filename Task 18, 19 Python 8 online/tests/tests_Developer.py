from Staff import Developer
from unittest import TestCase


class TestDeveloper(TestCase):
    def setUp(self):
        self.developer1 = Developer(
            name="Name_1",
            salary_per_day=200,
            email="Name_1@example.com",
            tech_stack=["Python", "JavaScript"]
        )
        self.developer2 = Developer(
            name="Name_2",
            salary_per_day=250,
            email="Name_2@example.com",
            tech_stack=["Python", "Java", "JavaScript"]
        )

    def test_work(self):
        self.assertEqual(self.developer1.work(), "I come to the office and start to coding.")

    def test_comparison_operators(self):
        self.assertTrue(self.developer1 < self.developer2)
        self.assertFalse(self.developer1 > self.developer2)
        self.assertTrue(self.developer1 == self.developer1)

    def test_add_developers(self):
        combined_developer = self.developer1 + self.developer2
        self.assertEqual(combined_developer.name, "Name_1 Name_2")
        self.assertEqual(combined_developer.salary_per_day, 250)
        self.assertEqual(combined_developer.email, "Name_1Name_2@example.com")
        self.assertEqual(set(combined_developer.tech_stack), {"Python", "JavaScript", "Java"})
