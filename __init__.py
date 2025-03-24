import os

import jmcomic
from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    Message,
)
from nonebot.params import CommandArg
from nonebot.plugin.on import on_command

from .utils import *  # noqa

jm = on_command("jm", aliases={"JM"}, priority=30, block=True)


@jm.handle()
async def _(bot: Bot, event: GroupMessageEvent, msg: Message = CommandArg()):
    id = msg.extract_plain_text().strip()
    option = jmcomic.create_option_by_file("./data/jm/option.yml")
    await jm.send("正在下载中...", at_sender=True)
    jmcomic.download_album(id, option)

    await bot.call_api(
        "upload_group_file",
        group_id=event.group_id,
        file=f"file:///{os.getcwd()}/data/jm/{id}.pdf",
        name=f"{id}.pdf",
    )
