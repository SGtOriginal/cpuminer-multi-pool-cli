# cpuminer-multi-pool-cli
Selects a pool out of preconfigured mining pool configurations

This project is a command line interface for https://github.com/tpruvot/cpuminer-multi

It offers following features:
* Load mining pool configuration saved in files
* Run cpuminer-multi with this configuration
ls dist 
## Install with PyInstaller (Debian Linux)

https://www.pyinstaller.org/

Prerequirements:
```shell script
apt-get install python3 python3-pip python3-dev
```

Install PyInstaller:
```shell script
pip install pyinstaller
```

If you don't find _pyinstaller_:
```
find / -name "pyinstaller"
```

Build native code into directory __dist/__:
```shell script
pyinstaller cpuminer-multi-pool-cli.py
```
