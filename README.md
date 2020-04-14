# cpuminer-multi-pool-cli
Selects a pool out of preconfigured mining pool configurations

This project is a command line interface for https://github.com/tpruvot/cpuminer-multi

It offers following features:
* Load mining pool configuration saved in files
* Run cpuminer-multi with this configuration

## Install with PyInstaller

https://www.pyinstaller.org/

Install PyInstaller:
```shell script
pip install pyinstaller
```

Build native code into directory __dist/__:
```shell script
pyinstaller cpuminer-multi-pool-cli.py
```
