# from mining.pool.config.general import json
#
# import mining.impl
#
# class MiningPoolConfigurationResolver:
#
#     def __init__(self, file):
#         with open(file) as json_file:
#             self.data = json.load(json_file)
#
#     def resolvePoolConfig(self, currencyOrSymbol, algorithm, pool, difficulty=None):
#         for c in self.data:
#             currency = c['currency']
#             symbol = c['symbol']
#             if currencyOrSymbol.lower() == currency.lower() or currencyOrSymbol.lower() == symbol.lower():
#                 for a in c['algoritms']:
#                     if algorithm.lower() == a['name'].lower():
#                         for p in a['pools']:
#                             if pool.lower() == p['name'].lower():
#                                 if difficulty is None or difficulty == p['difficulty']:
#                                     return c
#         return None
