from mining.app.cmd_args import parse_command_line_arguments
from mining.cmd import Command
from mining.cmd_executor import CommandExecutor, ConsoleCommandOutputConsumer, FileCommandOutputConsumer
from mining.pool.config.general.pool_config_resolver import JsonFilePoolConfigurationResolver
from mining.pool.config.selection.pool_selector import PoolSelector
from mining.pool.config.user.pool_user_config_resolver import CsvFilePoolUserConfigurationResolver


def _create_command(args):
    pool_config_file = cmd_args.get_pool_config_file(args)
    if pool_config_file is None:
        pool_config_file = 'pool_config.json'
    pool_user_config_file = cmd_args.get_pool_user_config_file(args)
    if pool_user_config_file is None:
        pool_user_config_file = 'pool_user_config.csv'

    pool_config_resolver = JsonFilePoolConfigurationResolver(pool_config_file)
    pool_user_config_resolver = CsvFilePoolUserConfigurationResolver(pool_user_config_file)
    pool_selector = PoolSelector(pool_config_resolver, pool_user_config_resolver)

    pool_selection_info = cmd_args.get_pool_selection_info(args)
    selected_pool_config = pool_selector.select_pool(pool_selection_info)
    if selected_pool_config is None:
        raise LookupError('No pool configuration in "' + pool_config_file + '" found')
    pool_config, pool_user_config = selected_pool_config
    pool_connection_info = pool_config.connection_info(
        pool_selection_info.currency_name_or_symbol,
        pool_selection_info.hash_algorithm,
        pool_selection_info.difficulty)
    if pool_connection_info is None:
        raise LookupError('No pool configuration in "' + pool_config_file + '" found')

    cmd_file_name = cmd_args.get_executive_file(args)
    if cmd_file_name is None:
        cmd_file_name = './cpuminer-multi/cpuminer'

    args = cmd_args.get_cpuminer_multi_args(args) \
           + cmd_args.get_pool_args(pool_selection_info, pool_connection_info, pool_user_config)
    return Command(cmd_file_name, args)


cmd_args = parse_command_line_arguments()

log_file = cmd_args.get_log_file(cmd_args)
cmd_output_consumer = ConsoleCommandOutputConsumer() \
    if log_file is None else FileCommandOutputConsumer(log_file)

cmd_executor = CommandExecutor(cmd_output_consumer)

cmd = _create_command(cmd_args)
cmd_executor.execute(cmd)

# poolConfig = mining.MiningPoolConfigurationResolver\
#     .resolvePoolConfig(args.currency, args.algorithm, args.pool, args.difficulty)
#
# os.system(args.file
#           + (' --quiet' if args.quiet else '')
#           + ' --algo ' + args.algorithm
#           # + ' --threads=' + args.threads
#           + ' ' + poolConfig.getPoolArgs())
