<div align="center">
  <a href="https://v2.nonebot.dev/store"><img src="https://github.com/A-kirami/nonebot-plugin-template/raw/resources/nbp_logo.png" width="180" height="180" alt="NoneBotPluginLogo"></a>
  <br>
  <p><img src="https://github.com/A-kirami/nonebot-plugin-template/raw/resources/NoneBotPlugin.svg" width="240" alt="NoneBotPluginText"></p>
</div>

<h1 align="center">nonebot_plugin_jmcomic</h1>
<h4 align="center">✨下载禁漫本子并发送✨</h4>

<p align="center">
    <img src="https://img.shields.io/badge/Python-3.9+-blue">
    <a href="https://github.com/zhulinyv/nonebot_plugin_jmcomic/raw/main/LICENSE"><img src="https://img.shields.io/github/license/zhulinyv/nonebot_plugin_jmcomic" alt="license"></a>
    <img src="https://img.shields.io/github/issues/zhulinyv/nonebot_plugin_jmcomic">
    <img src="https://img.shields.io/github/stars/zhulinyv/nonebot_plugin_jmcomic">
    <img src="https://img.shields.io/github/forks/zhulinyv/nonebot_plugin_jmcomic">
</p>


## 💿 安装

<details>
<summary>使用 nb-cli 安装</summary>
在 nonebot2 项目的根目录下打开命令行, 输入以下指令即可安装

    nb plugin install nonebot-plugin-jmcomic

</details>

<details>
<summary>使用包管理器安装</summary>
在 nonebot2 项目的插件目录下, 打开命令行, 根据你使用的包管理器, 输入相应的安装命令

<details>
<summary>pip</summary>

    pip install nonebot-plugin-jmcomic
</details>
<details>
<summary>pdm</summary>

    pdm add nonebot-plugin-jmcomic
</details>
<details>
<summary>poetry</summary>

    poetry add nonebot-plugin-jmcomic
</details>
<details>
<summary>conda</summary>

    conda install nonebot-plugin-jmcomic
</details>

打开 nonebot2 项目根目录下的 `pyproject.toml` 文件, 在 `[tool.nonebot]` 部分追加写入

    plugins = ["nonebot_plugin_nai3"]

</details>

## ⚙️ 配置

请移步 `data/jm/option.yml` 文件并参考 [option_file_syntax](https://github.com/hect0x7/JMComic-Crawler-Python/blob/master/assets/docs/sources/option_file_syntax.md) 进行配置.

默认不需要更改.


## 🎉 使用

jm + id

例如: jm 114514
