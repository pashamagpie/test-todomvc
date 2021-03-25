# from typing import Literal

import pydantic


# EnvContext = Literal['local', 'prod']


class Options(pydantic.BaseSettings):

    context = 'local'

    BROWSER_NAME: str = 'chrome'
    BROWSER_QUIT: bool = False


options = Options(_env_file=f'config.{Options().context}.env')


# if __name__ == '__main__':
#     print(options.__repr__())
