from importlib.metadata import version

from nonebot.adapters.onebot.v11 import (
    Bot,
    GroupMessageEvent,
    Message,
)
from nonebot.params import CommandArg
from nonebot.plugin import PluginMetadata
from nonebot.plugin.on import on_command

from .config import jm_config
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
    # 权限验证
    if jm_config.enable_auth:
        user_id = event.user_id
        group_id = event.group_id
        if not (user_id in jm_config.allowed_users or group_id in jm_config.allowed_groups):
            await jm.finish("您没有权限使用该功能", at_sender=True)
            return
            
    id = msg.extract_plain_text().strip()

    await jm.send("正在下载中...", at_sender=True)
    await async_download_album(id)  # noqa

    file = (
        "file:///" + str(jm_data_dir / f"{id}.pdf")  # noqa
        if jm_config.jm_client
        else str(jm_data_dir / f"{id}.pdf")  # noqa
    )

    await bot.upload_group_file(
        group_id=event.group_id,
        file=file,
        name=f"{id}.pdf",
    )
