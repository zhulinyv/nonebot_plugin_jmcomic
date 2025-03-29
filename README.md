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

    plugins = ["nonebot_plugin_jmcomic"]

</details>

## ⚙️ 配置

在 nonebot2 项目的 env 文件中添加下表中的必填配置

| 配置项 | 必填 | 类型 | 默认值 | 说明 |
|:-----:|:----:|:----:|:----:|:----:|
| jm_client | 否 | bool | True | 为 True 时, 将使用 file:/// 协议发送文件(客户端使用 NapCat/LLOB); 为 False 时使用绝对路径发送(客户端使用 Lagrange) |
| enable_auth | 否 | bool | True | 为 True 时启用用户权限验证功能，只有允许的用户和群组才能使用本插件 |
| allowed_users | 否 | list[int] | [] | 允许使用本插件的用户ID列表 |
| allowed_groups | 否 | list[int] | [] | 允许使用本插件的群组ID列表 |

关于代理等配置请移步[插件配置目录](https://github.com/nonebot/plugin-localstore)下 `option.yml` 文件并参考 [option_file_syntax](https://github.com/hect0x7/JMComic-Crawler-Python/blob/master/assets/docs/sources/option_file_syntax.md) 进行配置.

默认不需要更改.


## 🎉 使用

jm + id

例如: jm 114514

![qq_pic_merged_1742800962464](https://github.com/user-attachments/assets/81a89e70-53be-4a76-94fd-0bd5225b4057)


## 📚 待办

本插件仅提供了基本功能, 欢迎大家 pr.
