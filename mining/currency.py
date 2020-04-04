class Currency:

    def __init__(self, name: str, symbol: str):
        self.name = name
        self.symbol = symbol

    def matches(self, currency_name_or_symbol: str):
        return currency_name_or_symbol.lower() in [self.name.lower(), self.symbol.lower()]
