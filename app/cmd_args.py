import argparse

from cpuminer_multi.cmd_params import param_quiet, param_threads, param_algo, param_url, param_pass, param_user, \
    param_max_temp
from mining.pool.config.general.pool_connection_info import PoolConnectionInfo
from mining.pool.config.selection.pool_selection_info import PoolSelectionInfo
from mining.pool.config.user.pool_user_config import PoolUserConfiguration


def parse_command_line_arguments():
    parser = argparse.ArgumentParser(
        description='Start cpuminer-multi with preconfigured mining pool configurations'
                    + '; see https://github.com/tpruvot/cpuminer-multi')
    parser.add_argument('-f', '--file', help='file path of cpuminer-multi; default: "./cpuminer-multi/cpuminer"')
    parser.add_argument('-q', '--quiet', action='store_true', help='qiet mode of cpuminer-multi')
    parser.add_argument('-t', '--threads', type=int, help='quiet mode of cpuminer-multi')
    parser.add_argument('--max-temp', type=int, help='max temperature of cpuminer-multi')
    parser.add_argument('-p', '--pool', help='mining pool identifier from configuration file e.g. CoinFoundry')
    parser.add_argument('-c', '--currency',
                        help='crypto currency to mine as identifier from configuration file or symbol'
                             + ' e.g. Bitcoin or BTC for Bitcoin')
    parser.add_argument('-a', '--algorithm',
                        help='hash algorithm for crypto currency e.g. sha256d, scrypt')
    parser.add_argument('-d', '--difficulty', type=int, help='difficulty for hash algorithm (optional)')
    parser.add_argument('--pool-config-file',
                        help='file path of JSON mining pool configuration; default: "pool_config.json"')
    parser.add_argument('--pool-user-config-file',
                        help='file path of CSV mining pool user configuration; default: "pool_user_config.csv"')
    parser.add_argument('-l', '--log-file',
                        help='file path of log file. Output will be writen only to this file.'
                             + ' If not given the output will be written to output')

    return parser.parse_args()


def get_executive_file(args) -> str:
    return args.file


def get_pool_config_file(args) -> str:
    return args.pool_config_file


def get_pool_user_config_file(args) -> str:
    return args.pool_user_config_file


def get_log_file(args) -> str:
    return args.log_file


def get_cpuminer_multi_args(args) -> [str]:
    result = []
    if args.quiet:
        result.append(param_quiet)
    if args.threads is not None and args.threads > 0:
        result.append(param_threads(args.threads))
    if args.max_temp is not None and args.max_temp > 40:
        result.append(param_max_temp(args.max_temp))
    return result


def get_pool_selection_info(args):
    return PoolSelectionInfo(args.pool, args.currency, args.algorithm, args.difficulty)


def get_pool_args(
        pool_selection_info: PoolSelectionInfo,
        pool_connection_info: PoolConnectionInfo,
        pool_user_configuration: PoolUserConfiguration) -> [str]:
    return [
        param_algo(pool_selection_info.hash_algorithm.lower()),
        param_url(pool_connection_info.base_url, pool_connection_info.port),
        param_user(pool_user_configuration.username),
        param_pass(pool_user_configuration.password),
    ]
