import unittest

from project.my_python_app import load_template

class LoadTemplateCase(unittest.TestCase):
    def test_load_template(self):
        self.assertIn("src = test1/tests/abc:bazel", load_template.load_template())

if __name__ == "__main__":
    unittest.main()