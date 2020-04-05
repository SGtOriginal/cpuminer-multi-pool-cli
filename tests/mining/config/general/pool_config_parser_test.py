import unittest

from mining.pool.config.general.pool_config_parser import parse_pool_configurations


class PoolConfigurationParserTestCase(unittest.TestCase):

    def test_parse_pool_configurations_0(self):
        json_input = """[]"""

        pool_configs = parse_pool_configurations(json_input)

        self.assertEqual(0, len(pool_configs))

    def test_parse_pool_configurations_1(self):
        json_input = """[{
            "name": "MiningPool",
            "currencies": [
                {
                    "currency": {
                        "name": "Bitcoin",
                        "symbol": "BTC"
                    },
                    "algorithms": [
                        {
                            "name": "sha256d",
                            "connections": [
                                {
                                    "difficulty": 42,
                                    "baseurl": "mining.pool",
                                    "port": 12345
                                }
                            ]
                        }
                    ]
                }
            ]
        }]"""

        pool_configs = parse_pool_configurations(json_input)

        self.assertEqual(1, len(pool_configs))
        pool_config = pool_configs[0]

        self.assertEqual('MiningPool', pool_config.pool_name)

        self.assertEqual(1, len(pool_config.currency_configs))
        currency_config = pool_config.currency_configs[0]

        self.assertEqual('Bitcoin', currency_config.currency.name)
        self.assertEqual('BTC', currency_config.currency.symbol)

        self.assertEqual(1, len(currency_config.hash_algorithm_configs))
        hash_algorithm_config = currency_config.hash_algorithm_configs[0]

        self.assertEqual('sha256d', hash_algorithm_config.algorithm_name)

        self.assertEqual(1, len(hash_algorithm_config.connection_configs))
        connection_config = hash_algorithm_config.connection_configs[0]

        self.assertEqual(42, connection_config.difficulty)
        self.assertEqual('mining.pool', connection_config.base_url)
        self.assertEqual(12345, connection_config.port)

    def test_parse_pool_configurations_1_currency_0(self):
        json_input = """[{
            "name": "MiningPool",
            "currencies": []
        }]"""

        pool_configs = parse_pool_configurations(json_input)

        self.assertEqual(1, len(pool_configs))
        pool_config = pool_configs[0]

        self.assertEqual(0, len(pool_config.currency_configs))

    def test_parse_pool_configurations_1_algorithms_0(self):
        json_input = """[{
            "name": "MiningPool",
            "currencies": [
                {
                    "currency": {
                        "name": "Bitcoin"
                    },
                    "algorithms": []
                }
            ]
        }]"""

        pool_configs = parse_pool_configurations(json_input)

        self.assertEqual(1, len(pool_configs))
        pool_config = pool_configs[0]

        self.assertEqual(1, len(pool_config.currency_configs))
        currency_config = pool_config.currency_configs[0]

        self.assertEqual(0, len(currency_config.hash_algorithm_configs))

    def test_parse_pool_configurations_1_connections_0(self):
        json_input = """[{
            "name": "MiningPool",
            "currencies": [
                {
                    "currency": {
                        "name": "Bitcoin"
                    },
                    "algorithms": [
                        {
                            "name": "sha256d",
                            "connections": []
                        }
                    ]
                }
            ]
        }]"""

        pool_configs = parse_pool_configurations(json_input)

        self.assertEqual(1, len(pool_configs))
        pool_config = pool_configs[0]

        self.assertEqual(1, len(pool_config.currency_configs))
        currency_config = pool_config.currency_configs[0]

        self.assertEqual(1, len(currency_config.hash_algorithm_configs))
        hash_algorithm_config = currency_config.hash_algorithm_configs[0]

        self.assertEqual(0, len(hash_algorithm_config.connection_configs))

    def test_parse_pool_configurations_1_currency_without_symbol(self):
        json_input = """[{
            "name": "MiningPool",
            "currencies": [
                {
                    "currency": {
                        "name": "Bitcoin"
                    },
                    "algorithms": []
                }
            ]
        }]"""

        pool_configs = parse_pool_configurations(json_input)

        self.assertEqual(1, len(pool_configs))
        pool_config = pool_configs[0]

        self.assertEqual(1, len(pool_config.currency_configs))
        currency_config = pool_config.currency_configs[0]

        self.assertEqual(None, currency_config.currency.symbol)

    def test_parse_pool_configurations_n(self):
        json_input = """[
            {
                "name": "MiningPool1",
                "currencies": [
                    {
                        "currency": {
                            "name": "Bitcoin",
                            "symbol": "BTC"
                        },
                        "algorithms": [
                            {
                                "name": "sha256d",
                                "connections": [
                                    {
                                        "difficulty": 1,
                                        "baseurl": "mining1.pool",
                                        "port": 12345
                                    },
                                    {
                                        "difficulty": 2,
                                        "baseurl": "mining2.pool",
                                        "port": 22345
                                    }
                                ]
                            },
                            {
                                "name": "scrypt",
                                "connections": []
                            }
                        ]
                    },
                    {
                        "currency": {
                            "name": "DigiByte",
                            "symbol": "DGB"
                        },
                        "algorithms": []
                    }
                ]
            },
            {
                "name": "MiningPool2",
                "currencies": []
            }
        ]"""

        pool_configs = parse_pool_configurations(json_input)

        self.assertEqual(2, len(pool_configs))
        pool_config1 = pool_configs[0]
        pool_config2 = pool_configs[1]

        self.assertEqual('MiningPool1', pool_config1.pool_name)

        self.assertEqual('MiningPool2', pool_config2.pool_name)

        self.assertEqual(2, len(pool_config1.currency_configs))
        self.assertEqual(0, len(pool_config2.currency_configs))
        currency_config1 = pool_config1.currency_configs[0]
        currency_config2 = pool_config1.currency_configs[1]

        self.assertEqual('Bitcoin', currency_config1.currency.name)
        self.assertEqual('BTC', currency_config1.currency.symbol)

        self.assertEqual('DigiByte', currency_config2.currency.name)
        self.assertEqual('DGB', currency_config2.currency.symbol)

        self.assertEqual(2, len(currency_config1.hash_algorithm_configs))
        self.assertEqual(0, len(currency_config2.hash_algorithm_configs))
        hash_algorithm_config1 = currency_config1.hash_algorithm_configs[0]
        hash_algorithm_config2 = currency_config1.hash_algorithm_configs[1]

        self.assertEqual('sha256d', hash_algorithm_config1.algorithm_name)
        self.assertEqual('scrypt', hash_algorithm_config2.algorithm_name)

        self.assertEqual(2, len(hash_algorithm_config1.connection_configs))
        self.assertEqual(0, len(hash_algorithm_config2.connection_configs))
        connection_config1 = hash_algorithm_config1.connection_configs[0]
        connection_config2 = hash_algorithm_config1.connection_configs[1]

        self.assertEqual(1, connection_config1.difficulty)
        self.assertEqual('mining1.pool', connection_config1.base_url)
        self.assertEqual(12345, connection_config1.port)

        self.assertEqual(2, connection_config2.difficulty)
        self.assertEqual('mining2.pool', connection_config2.base_url)
        self.assertEqual(22345, connection_config2.port)


if __name__ == '__main__':
    unittest.main()
