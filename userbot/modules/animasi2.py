# credit by @kyuraxx
# own kyura

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.djancok(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("ᴡᴏɪ ᴋᴀʟᴀᴜ ᴅᴇᴘʟᴏʏ ʙᴀɢᴀsᴋᴀʀᴀ-ᴜsᴇʀʙᴏᴛ")
    sleep(3)
    await typew.edit("ᴊᴏɪɴ ᴊᴜɢᴀ sᴜᴘᴘʀᴏᴛ ɴʏᴀ ᴅᴊᴀɴᴄᴏᴋ !")
    sleep(3)
    await typew.edit("ᴅᴇᴘʟᴏʏ ᴅᴏᴀɴɢ ɢᴀ ᴊᴏɪɴ")
    sleep(3)
    await typew.edit("ᴅᴀsᴀʀ ᴅᴊᴀɴᴄᴏᴋ..")

CMD_HELP.update({
    "animasi2":
    "`.djancok` ;
})
