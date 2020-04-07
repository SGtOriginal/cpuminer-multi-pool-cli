class PoolConnectionInfo:

    def __init__(self,
                 pool_name: str,
                 base_url: str,
                 port: int):
        self.pool_name = pool_name
        self.base_url = base_url
        self.port = port

    def __eq__(self, other):
        if not isinstance(other, PoolConnectionInfo):
            return False

        return self.pool_name == other.pool_name

    def __str__(self) -> str:
        return 'PoolConnectionInfo{' \
               + 'pool_name=' + self.pool_name \
               + ', base_url=' + self.base_url \
               + ', port=' + self.port \
               + '}'
