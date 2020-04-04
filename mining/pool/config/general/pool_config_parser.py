from parser import JsonParser

class PoolConfigurationParser:

    def parse(self, input: str):
        parser = JsonParser()
        data = parser.json2obj(input)
        pass
