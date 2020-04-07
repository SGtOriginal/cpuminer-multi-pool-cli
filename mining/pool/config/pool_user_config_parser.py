from mining.pool.config.pool_user_config import PoolUserConfiguration


def parse_pool_user_configurations(rows: dict) -> [PoolUserConfiguration]:
    return list(map(lambda row: PoolUserConfiguration(row['pool_name'], row['username'], row['password']), rows))
