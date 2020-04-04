import argparse
import os

import mining

parser = argparse.ArgumentParser(description='Start cpuminer-multi with preconfigured mining pool configurations')
parser.add_argument('-f', '--file', help='file path of cpuminer-multi; see https://github.com/tpruvot/cpuminer-multi')
parser.add_argument('-q', '--quiet', help='qiet mode of cpuminer-multi; see https://github.com/tpruvot/cpuminer-multi')
parser.add_argument('-t', '--threads', type=int, help='qiet mode of cpuminer-multi')
parser.add_argument('-c', '--currency', help='crypto currency to mine as symbol e.g. BTC for Bitcoin')
parser.add_argument('-a', '--algorithm', help='hash algorithm for crypto currency e.g. sha256d, scrypt; see https://github.com/tpruvot/cpuminer-multi')
parser.add_argument('-d', '--difficulty', type=int, help='difficulty for hash algorithm')
parser.add_argument('-p', '--pool', help='mining pool identifier like in CSV defined e.g. CoinFoundry')


args = parser.parse_args()
poolConfig = mining.MiningPoolConfigurationResolver\
    .resolvePoolConfig(args.currency, args.algorithm, args.pool, args.difficulty)

os.system(args.file
          + (' --quiet' if args.quiet else '')
          + ' --algo ' + args.algorithm
          # + ' --threads=' + args.threads
          + ' ' + poolConfig.getPoolArgs())
