from mining.currency import Currency
from mining.json_parser import json2obj
from mining.pool.config.pool_config import PoolConfiguration, PoolCurrencyConfiguration, \
    PoolHashAlgorithmConfiguration, PoolConnectionConfiguration


def parse_pool_configurations(json_input: str) -> [PoolConfiguration]:
    parsed_pool_configs = json2obj(json_input)
    if parsed_pool_configs is None:
        return []
    pool_configs = []
    for parsed_pool_config in parsed_pool_configs:
        pool_config = _parse_pool_configuration(parsed_pool_config)
        pool_configs.append(pool_config)
        for currency in parsed_pool_config.currencies:
            currency_config = _parse_currency_config(currency.currency)
            pool_config.currency_configs.append(currency_config)
            for hash_algorithm in currency.algorithms:
                hash_algorithm_config = _parse_pool_hash_algorithm_configuration(hash_algorithm)
                currency_config.hash_algorithm_configs.append(hash_algorithm_config)

                connection_configs = list(map(_parse_pool_connection_configuration, hash_algorithm.connections))
                hash_algorithm_config.connection_configs.extend(connection_configs)
    return pool_configs


def _parse_pool_configuration(pool) -> PoolConfiguration:
    return PoolConfiguration(pool.name, [])


def _parse_currency_config(currency):
    return PoolCurrencyConfiguration(Currency(
        currency.name,
        currency.symbol if hasattr(currency, 'symbol') else None
    ), [])


def _parse_pool_hash_algorithm_configuration(hash_algorithm):
    return PoolHashAlgorithmConfiguration(hash_algorithm.name, [])


def _parse_pool_connection_configuration(connection) -> PoolConnectionConfiguration:
    return PoolConnectionConfiguration(
        connection.difficulty if hasattr(connection, 'difficulty') else None,
        connection.baseurl,
        connection.port)
