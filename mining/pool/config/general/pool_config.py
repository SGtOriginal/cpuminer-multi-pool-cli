from mining.currency import Currency
from mining.pool.config.general.pool_connection_info import PoolConnectionInfo


class PoolConnectionConfiguration:

    def __init__(self,
                 difficulty: float,
                 base_url: str,
                 port: int):
        self.difficulty = difficulty
        self.base_url = base_url
        self.port = port

    def __str__(self) -> str:
        return 'PoolPortConfiguration{' \
               + 'difficulty=' + str(self.difficulty) \
               + ', base_url=' + self.base_url \
               + ', port=' + str(self.port) \
               + '}'


class PoolHashAlgorithmConfiguration:

    def __init__(self,
                 algorithm_name: str,
                 connection_configs: [PoolConnectionConfiguration] = []):
        self.algorithm_name = algorithm_name
        self.connection_configs = connection_configs

    def __str__(self) -> str:
        return 'PoolHashAlgorithmConfiguration{' \
               + 'algorithm_name=' + str(self.algorithm_name) \
               + '}'


class PoolCurrencyConfiguration:

    def __init__(self,
                 currency: Currency,
                 hash_algorithm_configs: [PoolHashAlgorithmConfiguration] = []):
        self.currency = currency
        self.hash_algorithm_configs = hash_algorithm_configs

    def __str__(self) -> str:
        return 'PoolCurrencyConfiguration{' \
               + 'currency=' + str(self.currency) \
               + '}'


class PoolConfiguration:

    def __init__(self,
                 pool_name: str,
                 currency_configs: [PoolCurrencyConfiguration] = []):
        self.pool_name = pool_name
        self.currency_configs = currency_configs

    def __str__(self) -> str:
        return 'PoolConfiguration{' \
               + 'pool_name=' + self.pool_name \
               + '}'

    def connection_info(self,
                        currency_name_or_symbol: str,
                        hash_algorithm: str,
                        difficulty: int = None) -> PoolConnectionInfo:
        connection_candidate = self._filter_first_connection_candidates(currency_name_or_symbol,
                                                                        hash_algorithm,
                                                                        difficulty)
        return PoolConnectionInfo(self.pool_name, connection_candidate.base_url, connection_candidate.port) \
            if connection_candidate is not None else None

    def _filter_first_connection_candidates(self,
                                            currency_name_or_symbol: str,
                                            hash_algorithm: str,
                                            difficulty: int = None) -> PoolConnectionConfiguration:
        for currency_config in self.currency_configs:
            if currency_config.currency.matches(currency_name_or_symbol):
                for hash_algorithm_config in currency_config.hash_algorithm_configs:
                    if hash_algorithm_config.algorithm_name.lower() == hash_algorithm.lower():
                        for connection_config in hash_algorithm_config.connection_configs:
                            if difficulty is None or connection_config.difficulty == difficulty:
                                return connection_config
        return None
