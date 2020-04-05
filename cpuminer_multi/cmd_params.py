param_quiet = '--quiet'


def param_threads(count: int) -> str:
    return '--threads=' + str(count)


def param_max_temp(temp: int) -> str:
    return '--max-temp=' + str(temp)


def param_algo(hash_algorithm: str) -> str:
    return '--algo=' + hash_algorithm


def param_url(base_url: str, port: int) -> str:
    return '--url=stratum+tcp://' + base_url + ':' + str(port)


def param_user(username: str) -> str:
    return '--user=' + username


def param_pass(password: str) -> str:
    return '--pass=' + password
