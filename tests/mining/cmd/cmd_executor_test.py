import unittest

from mining.cmd import Command
from mining.cmd_executor import BufferCommandOutputConsumer, CommandExecutor


class CommandExecutorTestCase(unittest.TestCase):

    test_command = Command('echo', ['FooBar'])

    def test_executor_executes_command_and_reads_output(self):
        output_consumer = BufferCommandOutputConsumer()
        executor = CommandExecutor(output_consumer)
        executor.execute(self.test_command)
        self.assertEqual(['FooBar'], output_consumer.output_lines)


if __name__ == '__main__':
    unittest.main()
