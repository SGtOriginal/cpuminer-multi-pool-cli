from mining.pool.config.pool_config import PoolConnectionConfiguration, PoolConfiguration
from mining.pool.config.pool_connection_info import PoolConnectionInfo


def resolve_connection_info(
        pool_config: PoolConfiguration,
        currency_name_or_symbol: str = None,
        hash_algorithm: str = None,
        difficulty: int = None) -> PoolConnectionInfo:
    connection_candidate = _filter_first_exactly_matching_connection_candidate(
        pool_config,
        currency_name_or_symbol,
        hash_algorithm,
        difficulty)
    if connection_candidate is None:
        pass  # TODO non_exatly_matching_where_necessary_and_possible
    return PoolConnectionInfo(pool_config.pool_name, connection_candidate.base_url, connection_candidate.port) \
        if connection_candidate is not None else None


def _filter_first_exactly_matching_connection_candidate(
        pool_config: PoolConfiguration,
        currency_name_or_symbol: str = None,
        hash_algorithm: str = None,
        difficulty: int = None) -> PoolConnectionConfiguration:
    currency_config = _filter_list(
        currency_name_or_symbol,
        pool_config.currency_configs,
        lambda c, s: c.currency.matches(s))
    if currency_config is not None:
        hash_algorithm_config = _filter_list(
            hash_algorithm,
            currency_config.hash_algorithm_configs,
            lambda c, s: c.algorithm_name.lower() == s)
        if hash_algorithm_config is not None:
            connection_config = _filter_list(
                difficulty,
                hash_algorithm_config.connection_configs,
                lambda c, s: c.difficulty == s)
            if connection_config is not None:
                return connection_config

    # if currency_name_or_symbol is not None:
    #     for currency_config in pool_config.currency_configs:
    #         if hash_algorithm is not None \
    #                 and currency_config.currency.matches(currency_name_or_symbol):
    #             for hash_algorithm_config in currency_config.hash_algorithm_configs:
    #                 if hash_algorithm_config.algorithm_name.lower() == hash_algorithm.lower():
    #                     for connection_config in hash_algorithm_config.connection_configs:
    #                         if connection_config.difficulty == difficulty:
    #                             return connection_config
    return None


def _filter_list(search_key, list, matches):
    # try find exact match (also None as value possible)
    if search_key is not None:
        for item in list:
            if matches(item, search_key):
                return item
    elif len(list) > 0:
        return list[0]  # iterate over items until there is matching
    else:
        return None
