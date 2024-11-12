#meta developer: @amm1e & @AmeMods

from telethon import types
from telethon.tl.types import DocumentAttributeFilename
from PIL import Image
import io
import zipfile
from .. import loader, utils

@loader.tds
class ImageCutMod(loader.Module):
    """Модуль для разрезания изображения на части."""
    
    strings = {"name": "ImageCut"}

    MAX_ROWS = 10
    MAX_COLS = 10

    @loader.command()
    async def cut(self, message):
        """Использование: .cut <кол-во по вертикали> <кол-во по горизонтали>"""
        imagesinzip = int() 
        args = utils.get_args(message)
        await message.edit("<emoji document_id=5220046725493828505>✍️</emoji> <b>Ожидайте...</b>") 
        if len(args) != 2:
            await message.edit("<emoji document_id=5220197908342648622>❗</emoji> <b>Укажите количество частей по вертикали и горизонтали. Пример:</b> <code>.cut 2 2</code>")
            return

        try:
            rows = int(args[0])
            cols = int(args[1])
        except ValueError:
            await message.edit("<emoji document_id=5220197908342648622>❗</emoji> <b>Аргументы должны быть числами.</b>")
            return

        if rows > self.MAX_ROWS or cols > self.MAX_COLS:
            await message.edit(f"<emoji document_id=5220197908342648622>❗</emoji> <b>Максимальное количество частей: {self.MAX_ROWS} по вертикали и {self.MAX_COLS} по горизонтали.</b>")
            return
        
        reply = await message.get_reply_message()
        if not reply or not reply.media:
            await message.edit("<emoji document_id=5220197908342648622>❗</emoji> <b>Пожалуйста, ответьте на изображение для разрезания.</b>")
            return

        image = io.BytesIO()
        image = await reply.download_media(image)
        image = Image.open(image)

        width, height = image.size
        part_width = width // cols
        part_height = height // rows

        archive = io.BytesIO()
        with zipfile.ZipFile(archive, 'w') as zip_file:
            for row in range(rows):
                for col in range(cols):
                    left = col * part_width
                    top = row * part_height
                    right = left + part_width
                    bottom = top + part_height
                    part = image.crop((left, top, right, bottom))

                    part_io = io.BytesIO()
                    part.save(part_io, format="PNG")
                    part_io.seek(0)
                    imagesinzip += 1
                    part_filename = f"part_{row+1}_{col+1}.png"
                    zip_file.writestr(part_filename, part_io.read())
                    part_io.close()

        image.close()

        archive.seek(0)
        await message.delete() 
        await self.client.send_file(
            message.chat_id,
            file=archive,
            caption=f"<emoji document_id=5222148368955877900>🔥</emoji> <b>Количество разрезанных фотографий: {imagesinzip}.</b>",
            force_document=True,
            reply_to=reply,
            attributes=[DocumentAttributeFilename("cut_images.zip")]
        )
        
        archive.close()