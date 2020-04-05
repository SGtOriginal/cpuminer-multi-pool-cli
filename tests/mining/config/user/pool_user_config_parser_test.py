import unittest

from mining.pool.config.user.pool_user_config_parser import parse_pool_user_configurations


class PoolUserConfigurationParserTestCase(unittest.TestCase):

    def test_parse_pool_user_configurations_0(self):
        csv_input = []

        pool_user_configs = parse_pool_user_configurations(csv_input)

        self.assertEqual(0, len(pool_user_configs))

    def test_parse_pool_user_configurations_1(self):
        csv_input = [
            {
                'pool_name': 'pool1',
                'username': 'user1',
                'password': 'pass1',
            }
        ]

        pool_user_configs = parse_pool_user_configurations(csv_input)

        self.assertEqual(1, len(pool_user_configs))

        self.assertEqual('pool1', pool_user_configs[0].pool_name)
        self.assertEqual('user1', pool_user_configs[0].username)
        self.assertEqual('pass1', pool_user_configs[0].password)

    def test_parse_pool_user_configurations_n(self):
        csv_input = [
            {
                'pool_name': 'pool1',
                'username': 'user1',
                'password': 'pass1',
            },
            {
                'pool_name': 'pool2',
                'username': 'user2',
                'password': 'pass2',
            },
            {
                'pool_name': 'pool3',
                'username': 'user3',
                'password': 'pass3',
            }
        ]

        pool_user_configs = parse_pool_user_configurations(csv_input)

        self.assertEqual(3, len(pool_user_configs))

        self.assertEqual('pool1', pool_user_configs[0].pool_name)
        self.assertEqual('user1', pool_user_configs[0].username)
        self.assertEqual('pass1', pool_user_configs[0].password)

        self.assertEqual('pool2', pool_user_configs[1].pool_name)
        self.assertEqual('user2', pool_user_configs[1].username)
        self.assertEqual('pass2', pool_user_configs[1].password)

        self.assertEqual('pool3', pool_user_configs[2].pool_name)
        self.assertEqual('user3', pool_user_configs[2].username)
        self.assertEqual('pass3', pool_user_configs[2].password)


if __name__ == '__main__':
    unittest.main()
