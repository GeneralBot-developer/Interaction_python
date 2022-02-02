import discord

default_send = discord.ext.commands.Context.send


class Button_View(discord.ui.View):
    def __init__(self, item_list: list):
        for item in item_list:
            self.add_item(item)


class Activate_Interaction:
    def __init__(self):
        discord.ext.commands.Context.send = self.new_send

    async def new_send(self, **kwargs):
        for pg_key, pg_val in kwargs.items():
            if pg_key == "components":
                Button_View(pg_val)
                del kwargs["components"]
                break
        return await default_send(self, kwargs, view=Button_View)
