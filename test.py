

import unittest
from HW04 import git_reader


class TestGit(unittest.TestCase):
    def test1(self):
        self.assertEqual(git_reader("richkempinski"),
                         ['Repo: hellogitworld Number of commits: 30',
                          'Repo: helloworld Number of commits: 6',
                          'Repo: Mocks Number of commits: 10',
                          'Repo: Project1 Number of commits: 2',
                          'Repo: richkempinski.github.io Number of commits: 9',
                          'Repo: threads-of-life Number of commits: 1',
                          'Repo: try_nbdev Number of commits: 2',
                          'Repo: try_nbdev2 Number of commits: 5'])

    def test2(self):
        self.assertEqual(git_reader("asdfasfas"), [])


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)