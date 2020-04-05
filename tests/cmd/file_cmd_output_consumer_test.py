import os
import unittest
from datetime import date

from cmd.cmd_executor import FileCommandOutputConsumer


class FileCommandOutputConsumerTestCase(unittest.TestCase):

    def test_consum_output_line_1(self):
        file_name = 'mining.log'
        file_name_2 = 'mining_' + str(date.today()) + '.log'
        output_line = 'fooBar'
        output_consumer = FileCommandOutputConsumer(file_name)

        output_consumer.consum(output_line)
        with open(file_name_2, 'r') as file:
            output = file.read().strip()

        self.assertEqual(output_line, output)

        os.remove(file_name_2)

    def test_consum_output_line_n_append(self):
        file_name = 'mining.log'
        file_name_2 = 'mining_' + str(date.today()) + '.log'
        output_line = 'fooBar'
        output_consumer = FileCommandOutputConsumer(file_name)

        output_consumer.consum(output_line + str(1))
        output_consumer.consum(output_line + str(2))
        with open(file_name_2, 'r') as file:
            output = file.read().strip()

        self.assertEqual(output_line + str(1) + '\n' + output_line + str(2), output)

        os.remove(file_name_2)


if __name__ == '__main__':
    unittest.main()
