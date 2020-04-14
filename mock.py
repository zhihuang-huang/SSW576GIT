import unittest
from unittest import mock
import HW04


class TestGit(unittest.TestCase):
    @mock.patch('HW04.git')
    def test1(self, mock_git):
        mock_git("richkempinski").return_value = {'Repo: hellogitworld Number of commits: 30',
                                                  'Repo: helloworld Number of commits: 6',
                                                  'Repo: Mocks Number of commits: 10',
                                                  'Repo: Project1 Number of commits: 2',
                                                  'Repo: richkempinski.github.io Number of commits: 9',
                                                  'Repo: threads-of-life Number of commits: 1',
                                                  'Repo: try_nbdev Number of commits: 2',
                                                  'Repo: try_nbdev2 Number of commits: 5'}
        self.assertEqual(mock_git("richkempinski").return_value, {'Repo: hellogitworld Number of commits: 30',
                                                                  'Repo: helloworld Number of commits: 6',
                                                                  'Repo: Mocks Number of commits: 10',
                                                                  'Repo: Project1 Number of commits: 2',
                                                                  'Repo: richkempinski.github.io Number of commits: 9',
                                                                  'Repo: threads-of-life Number of commits: 1',
                                                                  'Repo: try_nbdev Number of commits: 2',
                                                                  'Repo: try_nbdev2 Number of commits: 5'})

    @mock.patch('HW04.git')
    def test2(self, mock_git):
        mock_git("asdfasfas").return_value = {}
        self.assertEqual(mock_git("asdfasfas").return_value, {})


if __name__ == '__main__':
    print('Running unit tests')
    unittest.main(argv=['first-arg-is-ignored'], exit=False, verbosity=2)
