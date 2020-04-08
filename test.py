

import unittest
from HW04 import git_reader


class TestGit(unittest.TestCase):
    def test1(self):
        self.assertEqual(git_reader("richkempinski"),
                         {'hellogitworld': 30, 'helloworld': 6, 'Mocks': 10, 'Project1': 2, 'threads-of-life': 1})

    def test2(self):
        self.assertEqual(git_reader("asdfasfas"), {})


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)