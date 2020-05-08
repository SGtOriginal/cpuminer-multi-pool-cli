from mining.pool.config.pool_config import PoolConnectionConfiguration, PoolConfiguration
from mining.pool.config.pool_connection_info import PoolConnectionInfo


def resolve_connection_info(
        pool_config: PoolConfiguration,
        currency_name_or_symbol: str = None,
        hash_algorithm: str = None,
        difficulty: float = None) -> PoolConnectionInfo:
    hash_algorithm_name, connection_candidate = _filter_first_matching_connection_candidate(
        pool_config,
        currency_name_or_symbol,
        hash_algorithm,
        difficulty)
    if connection_candidate is None:
        pass  # TODO non_exatly_matching_where_necessary_and_possible
    return PoolConnectionInfo(
        pool_config.pool_name,
        hash_algorithm_name,
        connection_candidate.base_url,
        connection_candidate.port
    ) if connection_candidate is not None else None


def _filter_first_matching_connection_candidate(
        pool_config: PoolConfiguration,
        currency_name_or_symbol: str = None,
        hash_algorithm: str = None,
        difficulty: float = None) -> PoolConnectionConfiguration:
    currency_config_candidates = _find_candidates(
        currency_name_or_symbol,
        pool_config.currency_configs,
        lambda c, s: s is not None and c.currency.matches(s),
        False)
    for currency_config_candidate in currency_config_candidates:
        if len(currency_config_candidate.hash_algorithm_configs) == 0:
            continue
        hash_algorithm_config_candidates = _find_candidates(
            hash_algorithm,
            currency_config_candidate.hash_algorithm_configs,
            lambda c, s: c.algorithm_name.lower() == s,
            False)
        for hash_algorithm_config_candidate in hash_algorithm_config_candidates:
            if len(hash_algorithm_config_candidate.connection_configs) == 0:
                continue
            connection_config_candidates = _find_candidates(
                difficulty,
                hash_algorithm_config_candidate.connection_configs,
                lambda c, s: c.difficulty == s,
                True)
            return hash_algorithm_config_candidate.algorithm_name, connection_config_candidates[0]
    return None


def _find_candidates(search_key, list_, matches, allow_none):
    if not allow_none and search_key is None:
        return list_  # iterate over items until there is matching
    # try find exact match (also None as value possible)
    for item in list_:
        if matches(item, search_key):
            return [item]
    return []  # no exact match found
