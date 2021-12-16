# Copyright (C) 2019 The Raphielscape Company LLC.
# RAM-UBOT MINTA
# Licensed under the Raphielscape Public License, Version 1.d (the "License");
# you may not use this file except in compliance with the License
# OWN MY CODE RENDY
# OWN BY Sayonara
# CREDIT Krisnadiwangga
# DONT'T REMOVE CREDIT FUCK DICK
""" Userbot module containing commands related to the \
    Information Superhighway (yes, Internet). """

import asyncio
import random
import time
from datetime import datetime

import redis
from speedtest import Speedtest

from userbot import (
    ALIVE_NAME,
    CMD_HELP,
    DEVS,
    REPO_NAME,
    StartTime,
)
from userbot.events import register

absen = [
    "**Hadir Ganteng** 🥵",
    "**Hadir Bang Bagas** 😎",
    "**Hadir Kak** 😉",
    "**Hadir Sayang** 😘",
    "**Hadir Kak Maap Telat** 🥺",
    "**PUJI TUHAN BAGAS** 🙏🏻",
    "**HIDUP LORD BAGAS** 😈",
]

pacar = [
    "**Bagas mau jadi pacar aku ga?** 💘",
    "**Bagas mending sama aku** 😎",
    "**Hai ganteng** 🥰",
    "**Mau ga bang jadi pacar aku?** 😁",
    "**Mending pc aku bang** 🥺",
    "**Bagas Punya Gua Anj!** 😘",
    "**Bismillah Slipkol Sama Bang Bagas**",
    
]


async def get_readable_time(seconds: int) -> str:
    count = 0
    up_time = ""
    time_list = []
    time_suffix_list = ["Dtk", "Mnt", "Jam", "Hari"]

    while count < 4:
        count += 50
        remainder, result = divmod(
            seconds, 60) if count < 3 else divmod(
            seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        up_time += time_list.pop() + ", "

    time_list.reverse()
    up_time += ":".join(time_list)

    return up_time


@register(incoming=True, from_users=DEVS, pattern=r"^.absen$")
async def _(sayo):
    await sayo.reply(random.choice(absen))


@register(incoming=True, from_users=DEVS, pattern=r"^.pacar$")
async def _(asadekontol):
    await asadekontol.reply(random.choice(pacar))


@register(outgoing=True, pattern="^.pings$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Connecting to server...`")
    await pong.edit("💀")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**`{ALIVE_NAME}`**\n"
                    f"✧ **-ꜱɪɢɴᴀʟ- :** "
                    f"`%sms` \n"
                    f"✧ **-ᴜᴘᴛɪᴍᴇ- :** "
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^.ping$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**█▒▒▒▒▒▒▒▒▒**") 
    await pong.edit("**███▒▒▒▒▒▒▒**") 
    await pong.edit("**█████▒▒▒▒▒**") 
    await pong.edit("**███████▒▒▒**") 
    await pong.edit("**██████████**")
    await pong.edit("👻")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"卍════〠 **TEST-PING** 〠════卍\n"
        f"✨ **Pɪɴɢᴇʀ :** "
        f"`%sms` \n"
        f"☂️ **Uᴘᴛɪᴍᴇ :** "
        f"`{uptime}` \n"
        f"✠➲ **Oᴡɴᴇʀ :** `{ALIVE_NAME}`" % (duration)
    )


@register(outgoing=True, pattern="^Ping$")
@register(incoming=True, from_users=DEVS, pattern=r"^\.cpi$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("PONG!!")
    await asyncio.sleep(2)
    await pong.edit(f"{REPO_NAME}")
    await asyncio.sleep(3)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"{REPO_NAME}!!\n"
                    f"OWNER : {ALIVE_NAME}\n `%sms`\n"
                    f"`{uptime}` \n" % (duration))


@register(outgoing=True, pattern="^Speed$")
async def speedtst(spd):
    """ For .speed command, use SpeedTest to check server speeds. """
    await spd.edit("`Menjalankan Tes Kecepatan Jaringan, Mohon Tunggu...🔥`")
    test = Speedtest()

    test.get_best_server()
    test.download()
    test.upload()
    test.results.share()
    result = test.results.dict()

    await spd.edit("**Kecepatan Jaringan:\n**"
                   "✧ **Dimulai Pada :** "
                   f"`{result['timestamp']}` \n"
                   f" **━━━━━━━━━━━━━━━━━**\n\n"
                   "✧ **Download:** "
                   f"`{speed_convert(result['download'])}` \n"
                   "✧ **Upload:** "
                   f"`{speed_convert(result['upload'])}` \n"
                   "✧ **Signal:** "
                   f"`{result['ping']}` \n"
                   "✧ **ISP:** "
                   f"`{result['client']['isp']}` \n"
                   f"✧ **BOT:** {REPO_NAME}")


def speed_convert(size):
    """
    Hi human, you can't read bytes?
    """
    power = 2**10
    zero = 0
    units = {0: '', 1: 'Kb/s', 2: 'Mb/s', 3: 'Gb/s', 4: 'Tb/s'}
    while size > power:
        size /= power
        zero += 1
    return f"{round(size, 2)} {units[zero]}"


@register(outgoing=True, pattern="^Pong$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    start = datetime.now()
    await pong.edit("PONG")
    await asyncio.sleep(1)
    await pong.edit("💀")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 9000
    await pong.edit(f"**Oᴡɴᴇʀ : {ALIVE_NAME}**\n`%sms`" % (duration))

@register(outgoing=True, pattern="^.hacker$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("CONNECTING.... ")
    await asyncio.sleep(1)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**ʙᴀɢᴀs-ᴜsᴇʀʙᴏᴛ.... !!**\n**ʙᴀɢᴀsᴋᴀʀᴀ ᴏɴʟɪɴᴇ** : `%sms`\n**ᴜᴘᴛɪᴍᴇs ᴘʀᴇᴇᴍ** : `{uptime}🔥`" % (duration))

@register(outgoing=True, pattern="^.crot$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8==✊=D")
    await pong.edit("8=✊==D")
    await pong.edit("8✊===D")
    await pong.edit("8=✊==D")
    await pong.edit("8==✊=D")
    await pong.edit("8===✊D")
    await pong.edit("8===✊D💦")
    await pong.edit("8====D💦💦")
    await pong.edit("** PINGGGG!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**ᴋᴇᴋᴜᴀᴛᴀɴ!! **\n**ɴɢᴇɴᴛᴏᴛ** : `%sms`\n**ʙᴏᴛ ᴜᴘᴛɪᴍᴇ** : `{uptime}🌹`" % (duration)) 

@register(outgoing=True, pattern="^.sping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("✧")
    await pong.edit("**✧✧**")
    await pong.edit("**✧✧✧**")
    await pong.edit("__DUAR LAKIK__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**{ALIVE_NAME}**        \n"
                    f"➾ᴋᴇᴄᴇᴘᴀᴛᴀɴ : '%sms'  \n"
                    f"➾ʙʀᴀɴᴄʜ    : ⚡ʙᴀɢᴀs-ᴜsᴇʀʙᴏᴛ⚡` \n" % (duration))

@register(outgoing=True, pattern="^.xping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("__Loading.__")
    await pong.edit("__Loading..__")
    await pong.edit("__Loading...__")
    await pong.edit("__Loading.__")
    await pong.edit("__Loading..__")
    await pong.edit("__Loading...__")
    await pong.edit("__Loading.__")
    await pong.edit("__Loading..__")
    await pong.edit("__Loading...__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⚡ʙᴀɢᴀs-ᴜsᴇʀʙᴏᴛ⚡**\n"
                    f"➾ __Signal__    __:__ "
                    f"`%sms` \n"
                    f"➾ __Uptime__ __:__ "
                    f"`{uptime}` \n" % (duration))

@register(outgoing=True, pattern="^.sinyal$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**Mengecek Sinyal...**")
    await pong.edit("**0% ▒▒▒▒▒▒▒▒▒▒**")
    await pong.edit("**20% ██▒▒▒▒▒▒▒▒**")
    await pong.edit("**40% ████▒▒▒▒▒▒**")
    await pong.edit("**60% ██████▒▒▒▒**")
    await pong.edit("**80% ████████▒▒**")
    await pong.edit("**100% ██████████**")
    await asyncio.sleep(2)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**🔥ʙᴀɢᴀs-ᴜsᴇʀʙᴏᴛ🔥**\n\n"
                    f"** ▹  Sɪɢɴᴀʟ   :** "
                    f"`%sms` \n"
                    f"** ▹  Uᴘᴛɪᴍᴇ  :** "
                    f"`{uptime}` \n"
                    f"** ▹  Oᴡɴᴇʀ   :** `{ALIVE_NAME}` \n" % (duration))

@register(outgoing=True, pattern="^.vping$")
async def redis(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**✿**")
    await pong.edit("**✿✿**")
    await pong.edit("**✿✿✿**")
    await pong.edit("**◕‿- PONG!!**")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**🔥ʙᴀɢᴀs-ᴜsᴇʀʙᴏᴛ🔥**\n"
                    f"♡︎ **ᴘᴏɴɢ !! :** "
                    f"`%sms` \n"
                    f"♡︎ **ᴜᴘᴛɪᴍᴇ !! :** "
                    f"`{uptime}` \n"
                    f"**♡︎ ᴍʏ ɴᴀᴍᴇ :** `{ALIVE_NAME}`" % (duration))


@register(outgoing=True, pattern=r"^\.punk$")
async def pingme(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    datetime.now()
    await pong.edit(".                       /¯ )")
    await pong.edit(".                       /¯ )\n                      /¯  /")
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /"
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸"
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ "
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')"
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /"
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´"
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              ("
    )
    await pong.edit(
        ".                       /¯ )\n                      /¯  /\n                    /    /\n              /´¯/'   '/´¯¯`•¸\n          /'/   /    /       /¨¯\\ \n        ('(   (   (   (  ¯~/'  ')\n         \\                        /\n          \\                _.•´\n            \\              (\n              \\  "
    )


@register(outgoing=True, pattern="^.bping$")
async def redis(pong):
    """For .ping command, ping the userbot from any chat."""
    await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("**🐖 LARI ADA KONTOL🐖 **")
    await pong.edit("**🐖🐖 ADA KONTIOL 🐖🐖**")
    await pong.edit("**🐖🐖🐖 ADA KONTOL 🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖 LU MEMEQ 🐖🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖🐖 KONTOL 🐖🐖🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖🐖🐖 KONTOL 🐖🐖🐖🐖🐖🐖**")
    await pong.edit("**🐖🐖🐖🐖🐖🐖🐖 KONTOL 🐖🐖🐖🐖🐖🐖🐖**")
    await pong.edit("`.................🐖`")
    await pong.edit("`................🐖.`")
    await pong.edit("`...............🐖..`")
    await pong.edit("`..............🐖...`")
    await pong.edit("`.............🐖....`")
    await pong.edit("`............🐖.....`")
    await pong.edit("`...........🐖......`")
    await pong.edit("`..........🐖.......`")
    await pong.edit("`.........🐖........`")
    await pong.edit("`........🐖.........`")
    await pong.edit("`.......🐖..........`")
    await pong.edit("`......🐖...........`")
    await pong.edit("`.....🐖............`")
    await pong.edit("`....🐖.............`")
    await pong.edit("`...🐖..............`")
    await pong.edit("`..🐖...............`")
    await pong.edit("`.🐖................`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(
        f"**{ALIVE_NAME}**        \n"
        f"**➾ᴋᴇᴄᴇᴘᴀᴛᴀɴ : ** %sms  \n"
        f"**➾ʙʀᴀɴᴄʜ : ** 🔥ʙᴀɢᴀs-ᴜsᴇʀʙᴏᴛ🔥 \n" % (duration)) 

@register(outgoing=True, pattern="^!uping$")
async def pingme(pong):
    """ For !ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("`Pinging...`")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**OWNER** - {ALIVE_NAME}\n\n"
                    f"ᴘᴏɴɢ !! : "
                    f"`%sms` \n"
                    f"ᴜᴘᴛɪᴍᴇ !! : "
                    f"`{uptime}` \n" % (duration))

@register(outgoing=True, pattern="^.peler$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("⚡")
    await pong.edit("__**PELER⚡**__")
    await pong.edit("__**P⚡LER**__")
    await pong.edit("__**PE⚡ER**__")
    await pong.edit("__**PEL⚡R**__")
    await pong.edit("__**⚡PELER KONTOL⚡**__")
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**⚡ʙᴀɢᴀs-ᴜsᴇʀʙᴏᴛ⚡**\n"
                    f"⚡ **ᴋᴏɴᴛᴏʟ !! :** "
                    f"`%sms` \n"
                    f"⚡ **ᴜᴘᴛɪᴍᴇ !! :** "
                    f"`{uptime}` \n" % (duration))
    
@register(outgoing=True, pattern="Lakik$")
async def pingme(pong):
    """ For .ping command, ping the userbot from any chat.  """
    uptime = await get_readable_time((time.time() - StartTime))
    start = datetime.now()
    await pong.edit("💀")
    await asyncio.sleep(3)
    await pong.edit("__**LAKIK**__")
    await pong.edit("__**💀AKIK**__")
    await pong.edit("__**L💀KIK**__")
    await pong.edit("__**LA💀IK**__")
    await pong.edit("__**LAK💀K**__")
    await pong.edit("__**LAKI💀**__")
    await pong.edit("__**DUAR**__")
    await asyncio.sleep(1)
    await pong.edit("😈")
    await asyncio.sleep(2)
    await pong.edit("__**USERBOT-LAKIK**__")
    await asyncio.sleep(1)
    end = datetime.now()
    duration = (end - start).microseconds / 1000
    await pong.edit(f"**💀ʙᴀɢᴀs-ᴜsᴇʀʙᴏᴛ💀**\n"
                    f"💀 **ᴘɪɴᴋɪɴɢ !!:** "
                    f"`%sms` \n"
                    f"💀 **ᴜᴘᴛɪᴍᴇ !! :** "
                    f"`{uptime}` \n" % (duration))
   
CMD_HELP.update({
    "ping": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ping` or `.pings` or `.crot` or `.hacker` or `.xping` or `.vping` or `.punk` `!uping` `peler` `Lakik`\
         \n↳ : Untuk Menunjukkan Ping Bot Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Speed` or `.sping` or `.sinyal` or `.bping`\
         \n↳ : Untuk Menunjukkan Kecepatan Jaringan Anda.\
         \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `Pong`\
         \n↳ : Sama Seperti Perintah Ping."})
