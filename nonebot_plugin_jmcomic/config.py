from nonebot.plugin import get_plugin_config
from pydantic import BaseModel


class Config(BaseModel):
    jm_client: bool = True


jm_config = get_plugin_config(Config)
