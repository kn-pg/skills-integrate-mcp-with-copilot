import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from app import activities


class ActivityTests(unittest.TestCase):
    def test_github_skills_activity_is_listed(self):
        self.assertIn("GitHub Skills", activities)
        self.assertEqual(activities["GitHub Skills"]["max_participants"], 15)
        self.assertEqual(activities["GitHub Skills"]["participants"], [])


if __name__ == "__main__":
    unittest.main()
