#meta developer: @amm1e & @AmeMods

from telethon import events
from .. import loader, utils

@loader.tds
class AmeMusic(loader.Module):
    """Модуль для поиска музыки, основанный на боте @AmeMusicbot"""
    
    strings = {
        "name": "AmeMusic",
        "searching": "<b>🔍 Ищу музыку...</b>",
        "no_results": "<b>❌ Не удалось найти трек. Попробуйте указать автора.</b>",
        "loading": "<b>⏳ Загрузка трека...</b>",
        "download_error": "<b>❌ Не удалось скачать аудио для песни. Обратитесь в тех.поддержку.</b>",
        "unexpected_error": "<b>❌ Произошла ошибка. Попробуйте позже.</b>", 
        "enter_name": "<b>❌ Введите название трека </b>"
    }
    strings_en = {
        "name": "AmeMusic",
        "searching": "<b>🔍 Search music...</b>",
        "no_results": "<b>❌ Could not find the track, please try again later.</b>",
        "loading": "<b>⏳ Downloading track...</b>",
        "download_error": "<b>❌ Could not download the track.</b>",
        "unexpected_error": "<b>❌ Error, try again later.</b>", 
        "enter_name": "<b>❌ Enter track name </b>"
    }

    async def searchmcmd(self, message):
        """{Название трека} - Поиск трека."""
        args = utils.get_args_raw(message)
        if not args:
            await message.edit(self.strings("enter_name"))
            return

        await message.edit(self.strings("searching"))
        
        try:
            async with message.client.conversation("@AmeMusicbot") as conv:
                await conv.send_message(args)

                while True:
                    response = await conv.get_response()

                    if "Не удалось найти трек" in response.text:
                        await message.edit(self.strings("no_results"))
                        return  

                    elif "Загрузка трека" in response.text:
                        await message.edit(self.strings("loading"))

                    elif "Не удалось скачать аудио" in response.text:
                        await message.edit(self.strings("download_error"))
                        return

                    elif response.media:
                        await message.client.send_message(message.chat_id, response)
                        await message.delete()
                        break

        except Exception as e:
            await message.edit(self.strings("unexpected_error"))