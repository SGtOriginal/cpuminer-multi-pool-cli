class PoolUserConfiguration:

    def __init__(self,
                 pool_name: str,
                 username: str,
                 password: str):
        self.pool_name = pool_name
        self.username = username
        self.password = password

    def __str__(self) -> str:
        return 'PoolCurrencyConfiguration{' \
               + 'pool_name=' + self.pool_name \
               + ', username=' + self.username \
               + ', password=' + self.password \
               + '}'
