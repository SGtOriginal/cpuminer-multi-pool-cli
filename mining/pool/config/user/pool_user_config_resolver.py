from csv import DictReader
from typing import overload

from mining.pool.config.user.pool_user_config import PoolUserConfiguration
from mining.pool.config.user.pool_user_config_parser import parse_pool_user_configurations


class PoolUserConfigurationResolver:

    @overload
    def resolve_all(self) -> [PoolUserConfiguration]:
        pass


class BufferPoolUserConfigurationResolver(PoolUserConfigurationResolver):

    def __init__(self, pool_user_configurations: PoolUserConfiguration):
        self.pool_user_configurations = pool_user_configurations

    def resolve_all(self) -> [PoolUserConfiguration]:
        return self.pool_user_configurations


class CsvFilePoolUserConfigurationResolver(PoolUserConfigurationResolver):

    def __init__(self, file_name: str):
        self.file_name = file_name

    def resolve_all(self) -> [PoolUserConfiguration]:
        with open(self.file_name, 'r') as csvfile:
            rows = DictReader(csvfile)
            return parse_pool_user_configurations(rows)
