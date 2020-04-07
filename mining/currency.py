class Currency:

    def __init__(self, name: str, symbol: str = None):
        self.name = name
        self.symbol = symbol

    def __eq__(self, other):
        if not isinstance(other, Currency):
            return False

        return self.name == other.name

    def __str__(self) -> str:
        return 'Currency{' \
               + 'name=' + str(self.name) \
               + ', symbol=' + str(self.symbol) \
               + '}'

    def matches(self, currency_name_or_symbol: str):
        return currency_name_or_symbol.lower() == self.name.lower() \
               or (self.symbol is not None and currency_name_or_symbol.lower() == self.symbol.lower())
