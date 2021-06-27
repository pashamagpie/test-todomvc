from typing import Literal, Optional

import pydantic


EnvContext = Literal['local', 'prod']
BrowserName = Literal['chrome', 'firefox']


class Settings(pydantic.BaseSettings):

    context: EnvContext = 'local'

    browser_name: BrowserName = 'chrome'
    browser_quit: bool = False
    browser_headless: bool = False
    browser_window_maximize: bool = False
    browser_window_width: int = 800
    browser_window_height: int = 600
    remote_url: Optional[pydantic.AnyHttpUrl] = None
    remote_enable_vnc: bool = True
    remote_screen_resolution: str = '1920x900x24'


settings = Settings(_env_file=f'config.{Settings().context}.env')


# if __name__ == '__main__':
#     print(options.__repr__())
