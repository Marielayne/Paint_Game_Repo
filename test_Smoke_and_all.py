""" Smoke test and unittest to ensure quiz works correctly """

import unittest # imports module to allow tests for the quiz
import os # imports module to allow saving to Mac and Windows
import tempfile # imports tempfile to store temp data for T-D-D
import csv # imports module to allow read and write of csv
from quiz_gui import QuizResult  # import to test call quiz functions


class SmokeTest(unittest.TestCase):
    def test_ut_works(self):
        self.assertEqual(5*2, 10)


# -- Tests CSV read and wrtie --
class TestCSVSave(unittest.TestCase):
    def setUp(self):
        """Set up temporary directory for CSV testing"""
        self.test_dir = tempfile.TemporaryDirectory()
        self.csv_path = os.path.join(self.test_dir.name, "quiz_results.csv")

        # Sample team and quiz result
        self.team_name = "Test team 1"
        self.department = "R&D"
        self.members = ["Aaron", "Marie", "Silvia"]
        self.score = 3
        self.total_questions = 5

        # Create QuizResult instance
        self.quiz_result = QuizResult(
            self.team_name,
            self.department,
            self.members,
            self.score,
            self.total_questions
        )

    def tearDown(self):
        """Clean up temporary files"""
        self.test_dir.cleanup()

    def test_csv_write_and_content(self):
        """Test saving QuizResult to CSV"""
        # Write CSV
        data = self.quiz_result.get_csv_data()
        with open(self.csv_path, mode='a', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=data.keys())
            if os.path.getsize(self.csv_path) == 0:
                writer.writeheader()
            writer.writerow(data)

        # Verify CSV exists
        self.assertTrue(os.path.exists(self.csv_path))

        # Read back the CSV and check content
        with open(self.csv_path, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            rows = list(reader)
            self.assertEqual(len(rows), 1)
            self.assertEqual(rows[0]["Team Name"], self.team_name)
            self.assertEqual(rows[0]["Department"], self.department)
            self.assertEqual(rows[0]["Members"], ", ".join(self.members))
            self.assertEqual(rows[0]["Score"], f"{self.score}/{self.total_questions}")
            self.assertEqual(rows[0]["Percentage"], f"{int((self.score/self.total_questions)*100)}%")

# -- Tests score function -- 
class TestQuizScoring(unittest.TestCase):
    def test_percentage_calculation(self):
        """Test that percentage is calculated correctly"""
        result = QuizResult("Team A", "Sales", ["Marie"], score=4, total_questions=5)
        self.assertIsInstance(result.percentage, 80)


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)