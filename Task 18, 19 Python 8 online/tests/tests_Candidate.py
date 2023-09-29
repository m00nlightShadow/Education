import unittest
from Staff import Candidate


class TestCandidate(unittest.TestCase):
    def setUp(self):
        self.candidate = Candidate(
            'Howard',
            'Smith',
            'HoSm@data.com',
            tech_stack=['HTML', 'JavaScript', 'TypeScript', 'Django', 'Python'],
            main_skill='Python',
            main_skill_grade='Senior',
        )

    def test_full_name(self):
        self.assertEqual(self.candidate.full_name, "Howard Smith")

    def test_generate_candidates(self):
        candidates = Candidate.generate_candidates("https://example.com/candidates.csv")
        self.assertIsInstance(candidates, list)
        self.assertTrue(all(isinstance(candidate, Candidate) for candidate in candidates))
