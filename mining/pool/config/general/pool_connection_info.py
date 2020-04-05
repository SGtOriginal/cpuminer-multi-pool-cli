class PoolConnectionInfo:

    def __init__(self,
                 pool_name: str,
                 base_url: str,
                 port: int):
        self.pool_name = pool_name
        self.base_url = base_url
        self.port = port