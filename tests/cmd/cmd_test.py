import unittest

from cmd.cmd import Command


class CommandTestCase(unittest.TestCase):

    def test_local_installation(self):
        cmd = Command('cpuminer', ['arg1', 'arg2', 'arg3'])
        self.assertEqual('cpuminer', cmd.name)
        self.assertListEqual(['arg1', 'arg2', 'arg3'], cmd.args)

    def test_docker(self):
        cmd = Command('docker run cpuminer-multi:alpine cpuminer', ['arg1', 'arg2', 'arg3'])
        self.assertEqual('docker', cmd.name)
        self.assertLessEqual(['run', 'cpuminer-multi:alpine', 'cpuminer', 'arg1', 'arg2', 'arg3'], cmd.args)


if __name__ == '__main__':
    unittest.main()
