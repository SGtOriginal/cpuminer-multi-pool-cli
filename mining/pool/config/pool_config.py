from mining.currency import Currency


class PoolConnectionConfiguration:

    def __init__(self,
                 difficulty: float,
                 base_url: str,
                 port: int):
        self.difficulty = difficulty
        self.base_url = base_url
        self.port = port

    def __eq__(self, other):
        if not isinstance(other, PoolConnectionConfiguration):
            return False

        return self.difficulty == other.difficulty

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

    def __eq__(self, other):
        if not isinstance(other, PoolHashAlgorithmConfiguration):
            return False

        return self.algorithm_name == other.algorithm_name

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

    def __eq__(self, other):
        if not isinstance(other, PoolCurrencyConfiguration):
            return False

        return self.currency == other.currency

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

    def __eq__(self, other):
        if not isinstance(other, PoolConfiguration):
            return False

        return self.pool_name == other.pool_name

    def __str__(self) -> str:
        return 'PoolConfiguration{' \
               + 'pool_name=' + self.pool_name \
               + '}'
