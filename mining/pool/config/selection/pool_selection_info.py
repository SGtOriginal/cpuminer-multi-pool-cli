from mining.pool.config.general.pool_config import PoolConfiguration
from mining.pool.config.user.pool_user_config import PoolUserConfiguration


class PoolSelectionInfo:

    def __init__(self,
                 pool_name: str,
                 currency_name_or_symbol: str,
                 hash_algorithm: str,
                 difficulty: int = None):
        self.pool_name = pool_name
        self.currency_name_or_symbol = currency_name_or_symbol
        self.hash_algorithm = hash_algorithm
        self.difficulty = difficulty

    def matches_pool_configuration(self, pool_config: PoolConfiguration) -> bool:
        return pool_config.pool_name.lower() == self.pool_name.lower()

    def matches_pool_user_configuration(self, pool_user_config: PoolUserConfiguration) -> bool:
        return pool_user_config.pool_name.lower() == self.pool_name.lower()
