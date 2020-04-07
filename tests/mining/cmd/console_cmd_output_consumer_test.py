import unittest

from mining.cmd_executor import ConsoleCommandOutputConsumer
from tests.test_console import captured_output


class ConsoleCommandOutputConsumerTestCase(unittest.TestCase):

    def test_consum_output_line_1(self):
        prefix = '* '
        output_line = 'fooBar'
        output_consumer = ConsoleCommandOutputConsumer(prefix)

        with captured_output() as (out, err):
            output_consumer.consum(output_line)
        output = out.getvalue().strip()

        self.assertEqual(prefix + output_line, output)

    def test_consum_output_line_1(self):
        prefix = '* '
        output_line = 'fooBar'
        output_consumer = ConsoleCommandOutputConsumer(prefix)

        with captured_output() as (out, err):
            output_consumer.consum(output_line + str(1))
            output_consumer.consum(output_line + str(2))
        output = out.getvalue().strip()

        self.assertEqual(prefix + output_line + str(1) + '\n' + prefix + output_line + str(2), output)


if __name__ == '__main__':
    unittest.main()
