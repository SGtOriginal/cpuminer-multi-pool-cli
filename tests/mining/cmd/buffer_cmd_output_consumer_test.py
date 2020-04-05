import unittest

from mining.cmd import BufferCommandOutputConsumer


class BufferCommandOutputConsumerTestCase(unittest.TestCase):

    def test_consum_output_line_1(self):
        output_line = 'fooBar'
        output_consumer = BufferCommandOutputConsumer()

        output_consumer.consum(output_line)

        self.assertListEqual([output_line], output_consumer.output_lines)

    def test_consum_output_line_n(self):
        output_line = 'fooBar'
        output_consumer = BufferCommandOutputConsumer()

        output_consumer.consum(output_line + str(1))
        output_consumer.consum(output_line + str(2))

        self.assertListEqual([output_line + str(1), output_line + str(2)], output_consumer.output_lines)


if __name__ == '__main__':
    unittest.main()
