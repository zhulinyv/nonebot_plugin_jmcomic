import os
from importlib.metadata import version

import jmcomic
from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    Message,
)
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.plugin.on import on_command

from .utils import *  # noqa

try:
    __version__ = version("nonebot_plugin_jmcomic")
except Exception:
    __version__ = "0.0.0"

__plugin_meta__ = PluginMetadata(
    name="nonebot-plugin-jmcomic",
    description="下载禁漫并发送",
    usage="jm + id",
    homepage="https://github.com/zhulinyv/nonebot_plugin_jmcomic",
    type="application",
    supported_adapters={"~onebot.v11"},
    config=None,
    extra={
        "author": "zhulinyv",
        "version": __version__,
    },
)

jm = on_command("jm", aliases={"JM"}, priority=30, block=True)


@jm.handle()
async def _(bot: Bot, event: GroupMessageEvent, msg: Message = CommandArg()):
    id = msg.extract_plain_text().strip()
    option = jmcomic.create_option_by_file("./data/jm/option.yml")
    await jm.send("正在下载中...", at_sender=True)
    jmcomic.download_album(id, option=option)

    await bot.call_api(
        "upload_group_file",
        group_id=event.group_id,
        file=f"file:///{os.getcwd()}/data/jm/{id}.pdf",
        name=f"{id}.pdf",
    )
