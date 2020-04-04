from mining.currency import Currency

class PoolConfiguration:

    def __init__(self,
                 pool_name: str,
                 base_url: str,
                 port: int,
                 currency: Currency,
                 hash_algorithm: str,
                 difficulty: float,
                 default_password: str=None):
        self.pool_name = pool_name
        self.base_url = base_url
        self.port = port
        self.currency = currency
        self.hash_algorithm = hash_algorithm
        self.difficulty = difficulty
        self.default_password = default_password
