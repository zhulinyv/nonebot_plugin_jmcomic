import asyncio
import os
from pathlib import Path

import jmcomic
from nonebot import require

require("nonebot_plugin_localstore")

import nonebot_plugin_localstore as store  # noqa

jm_data_dir: Path = store.get_plugin_data_dir()
jm_config_file: Path = store.get_plugin_config_file("option.yml")

jm_data_dir_str = str(jm_data_dir)


async def async_download_album(id):
    option = jmcomic.create_option_by_file(str(jm_config_file))
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(
        None,
        jmcomic.download_album,
        id,
        option,
    )


if not os.path.exists(jm_config_file):
    with open(jm_config_file, "w", encoding="utf-8") as file:
        file.write(
            f"""# 更多配置请参考: https://github.com/hect0x7/JMComic-Crawler-Python/blob/master/assets/docs/sources/option_file_syntax.md
dir_rule:
  base_dir: {jm_data_dir_str}

plugins:
  after_photo:
    - plugin: img2pdf
      kwargs:
        pdf_dir: {jm_data_dir_str}
        filename_rule: Pid
  
  after_album:
    - plugin: img2pdf
      kwargs:
        pdf_dir: {jm_data_dir_str}
        filename_rule: Aname
"""
        )
