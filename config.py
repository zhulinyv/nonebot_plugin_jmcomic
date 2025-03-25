from nonebot.plugin import get_plugin_config
from nonebot import get_driver
from pydantic import BaseModel, Field


class Config(BaseModel):
    jm_client: bool = True
    enable_auth: bool = Field(default=True)
    allowed_users: list[int] = Field(default_factory=lambda: list)
    allowed_groups: list[int] = Field(default_factory=list)


jm_config = get_plugin_config(Config)
