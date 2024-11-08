# meta developer: @amm1e
# говнокод

from hikkatl.types import Message
from .. import utils, loader


@loader.tds
class AmeActions(loader.Module):
    """AmeActions"""
    strings = {"name": "AmeActions — Действия"}
    
    @loader.command()
    async def kiss(self, message: Message):
        """- kiss [reply] Целовать человека из репли"""
        me = await self._client.get_me()
        reply = await message.get_reply_message()
        susr = me.username
        if reply == None:
            await utils.answer(message,"❌ | <b>Команда работает в ответ на сообщение пользователя.</b>")
        elif reply != None:
            usr = reply.sender.username
            if susr == usr:
                await utils.answer(message,"❌ |<b> Самолюбие конечно хорошо, но держи его при себе.</b>")
            else:
                await utils.answer(message, f"<emoji document_id=5222102889547185747>💋</emoji> | <b> {susr} поцеловал(а)@{usr}</b>")
                
    @loader.command()
    async def hug(self, message: Message):
        """- hug [reply] Обнимать человека из репли"""
        me = await self._client.get_me()
        reply = await message.get_reply_message()
        susr = me.username
        if reply == None:
            await utils.answer(message,"❌ | <b>Команда работает в ответ на сообщение пользователя.</b>")
        elif reply != None:
            usr = reply.sender.username
            if susr == usr:
                await utils.answer(message,"❌ | <b>Кто тебе запрещает обняться с самим собой в реальной жизни? </b>")
            else:
                await utils.answer(message, f"<emoji document_id=5222325171284622461>💘</emoji> | <b> {susr} обнял(а) @{usr}</b>")
                
    @loader.command()
    async def push(self, message: Message):
        """- push [reply] Толкать человека из репли"""
        me = await self._client.get_me()
        reply = await message.get_reply_message()
        susr = me.username
        if reply == None:
            await utils.answer(message,"❌ | <b>Команда работает в ответ на сообщение пользователя.</b>")
        elif reply != None:
            usr = reply.sender.username
            if susr == usr:
                await utils.answer(message,"❌ | <b>Покажи всем как ты толкаешь самого себя.</b>")
            else:
                await utils.answer(message, f"<emoji document_id=5449552292980214333>🙌</emoji> | <b> {susr} толкнул(а) @{usr}</b>")
                
    @loader.command()
    async def hit(self, message: Message):
        """- hit [reply] Ударить человека из репли"""
        me = await self._client.get_me()
        reply = await message.get_reply_message()
        susr = me.username
        if reply == None:
            await utils.answer(message,"❌ | <b>Команда работает в ответ на сообщение пользователя.</b>")
        elif reply != None:
            usr = reply.sender.username
            if susr == usr:
                await utils.answer(message,"❌ | <b>Мазохизм не приветствуется.</b>")
            else:
                await utils.answer(message, f"<emoji document_id=5404854933402965409>💔</emoji> | <b> {susr} ударил(а) @{usr}</b>")
                
    @loader.command()
    async def scold(self, message: Message):
        """- scold [reply] Ругать человека из репли"""
        me = await self._client.get_me()
        reply = await message.get_reply_message()
        susr = me.username
        if reply == None:
            await utils.answer(message,"❌ | <b>Команда работает в ответ на сообщение пользователя.</b>")
        elif reply != None:
            usr = reply.sender.username
            if susr == usr:
                await utils.answer(message,"❌ | <b>Я посмотрю как ты наругаешь самого себя. </b>")
            else:
                await utils.answer(message, f"<emoji document_id=5222102889547185747>💋</emoji> | <b> {susr} наругал(а) @{usr}</b>")
                
    @loader.command()
    async def kill(self, message: Message):
        """- hug [reply] Обнимает человека из репли"""
        me = await self._client.get_me()
        reply = await message.get_reply_message()
        susr = me.username
        if reply == None:
            await utils.answer(message,"❌ | <b>Команда работает в ответ на сообщение пользователя.</b>")
        elif reply != None:
            usr = reply.sender.username
            if susr == usr:
                await utils.answer(message,"❌ | <b>Суицид? </b>")
            else:
                await utils.answer(message, f"<emoji document_id=5449603119623193071>⚰️</emoji> | <b> {susr} убил(а) @{usr}</b>")
                
    @loader.command(en_doc="bite")
    async def bite(self, message: Message):
        """- bite [reply] Кусать человека из репли"""
        me = await self._client.get_me()
        reply = await message.get_reply_message()
        susr = me.username
        if reply == None:
            await utils.answer(message,"❌ | <b>Команда работает в ответ на сообщение пользователя.</b>")
        elif reply != None:
            usr = reply.sender.username
            if susr == usr:
                await utils.answer(message,"❌ | <b>Это какой-то фетиш? </b>")
            else:
                await utils.answer(message, f"👄 | <b> {susr} укусил(а) @{usr}</b>")
                
    @loader.command()
    async def caction(self, message: Message):
        """- caction (args) [reply] Кастомное действие"""
        args = utils.get_args_raw(message)
        me = await self._client.get_me()
        reply = await message.get_reply_message()
        susr = me.username
        if reply == None:
            await utils.answer(message,"❌ | <b>Команда работает в ответ на сообщение пользователя.</b>")
        elif reply != None:
            usr = reply.sender.username
            if susr == usr:
                await utils.answer(message,f"❌ | <b>Увы, но на себе эту команду применить нельзя.</b>")
            else:
                await utils.answer(message, f"👤 | <b> {susr} {args} @{usr}</b>")
