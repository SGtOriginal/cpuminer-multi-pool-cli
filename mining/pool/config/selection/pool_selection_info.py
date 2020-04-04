class PoolSelectionInfo:

    def __init__(self,
                 pool_name: str,
                 currency_name_or_symbol: str,
                 difficulty: int=None):
        self.pool_name = pool_name
        self.currency_name_or_symbol = currency_name_or_symbol
        self.difficulty = difficulty
