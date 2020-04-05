from typing import overload

from mining.pool.config.general.pool_config import PoolConfiguration
from mining.pool.config.general.pool_config_parser import parse_pool_configurations


class PoolConfigurationResolver:

    @overload
    def resolve_all_pool_configurations(self) -> [PoolConfiguration]:
        pass


class BufferPoolConfigurationResolver(PoolConfigurationResolver):

    def __init__(self, pool_configurations: [PoolConfiguration]):
        self.pool_configurations = pool_configurations

    def resolve_all(self) -> [PoolConfiguration]:
        return self.pool_configurations


class JsonFilePoolConfigurationResolver(PoolConfigurationResolver):

    def __init__(self, file_name: str):
        self.file_name = file_name

    def resolve_all(self) -> [PoolConfiguration]:
        with open(self.file_name, 'r') as file:
            json = file.read()
            return parse_pool_configurations(json)
