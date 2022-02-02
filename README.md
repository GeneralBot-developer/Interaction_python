# Interaction_python
Pythonでinteractionの作成・送信を楽に行えるライブラリです。

# 使い方/usage
## 1.Interaction_pythonをインストールする
```shell
#discord.pyを使用している場合
pip install Interaction_python["discord.py"]

#pycordを使用している場合
pip install Interaction_python["pycord"]

#nextcordを使用している場合
pip install Interaction_python["nextcord"]
```
上記以外のライブラリを使用したい場合はissueを建ててもらえると対応します。


## 2.ライブラリをインポートする
```python
import discord
from interaction import Button

bot = discord.Bot(command_prefix="!")

Button.Activate_Interaction()

bot.run("TOKEN")
```
# 使用例/example
```python
async def callback(view, button, interaction):
    await interaction.response.send_message("Pong!")

@bot.command()
async def ping(self, ctx):
    await ctx.send(
        content="Pong!",
        components=[
            discord.ui.button(
                label="ping"
            )(callback), ...
        ]
    )
```