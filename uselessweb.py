# meta developer: @amm1e

import requests
import random
from .. import loader, utils
from .. import loader

@loader.tds
class uselesswmod(loader.Module):
    """Бесполезный модуль для вывода бесполезных сайтов."""
    strings = {"name": "uselessweb"}

    @loader.command()
    async def uselessweb(self, message):
        """- Рандомный бесполезный сайт."""
        response = requests.get('https://gist.githubusercontent.com/quest/07bbc6908f84b50a9fc8/raw/d8983a0723d07203816b78953ff52f07423c808d/uselessweb.json')
        file = response.json()
        uselesswebr = random.choice(file['uselessweb'])
        await message.edit(f'<emoji document_id=5318759457801385682>👍</emoji> <b>Ваш рандомный сайт</b>:  {uselesswebr}')