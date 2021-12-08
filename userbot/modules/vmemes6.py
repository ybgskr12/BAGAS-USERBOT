# OWN MY CODE RENDY
# CREDITS @Randi356
# DONT'T REMOVE CREDIT YOU FUCK GBAN

from time import sleep
from userbot import CMD_HELP, bot
from userbot.events import register
from telethon import events
import asyncio


@register(outgoing=True, pattern='^.jamet(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("WOI JAMET!!!")
    sleep(2)
    await typew.edit("CUMA MAU BILANG")
    sleep(2)
    await typew.edit("GAUSAH SOK ASIK")
    sleep(2)
    await typew.edit("EMANG KENAL?")
    sleep(2)
    await typew.edit("GAUSAH REPLY")
    sleep(2)
    await typew.edit("KITA BUKAN KAWAN")
    sleep(2)
    await typew.edit("GAUSAH PC ANJING")
    sleep(2)
    await typew.edit("BOCAH KAMPUNG")
    sleep(2)
    await typew.edit("MENTAL PUKII")
    sleep(2)
    await typew.edit("LEMBEK NGENTOT😆")
 
@register(outgoing=True, pattern='^.berantem(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WOI ANJING!!!**")
    sleep(2)
    await typew.edit("**BERANTEM YO NGENTOT**")
    sleep(2)
    await typew.edit("**JANGAN JADI BENCI KETAKUTAN YA ANJING, SAHRELOCK SEKARANG BANGSAT**")
    sleep(2)
    await typew.edit("**JANGAN MENTAL SOSMED DOANG LU**")

@register(outgoing=True, pattern='^.rp(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WOI ANAK RP NGENTOT, DENGER NI YA PLASTIK MAH UDAH PLASTIK AJA!!!**")
    sleep(2)
    await typew.edit("**GOBLOK KOK DI RAWAT, UDAH NGEMBAH PLASTIK SAMPAH LAGI HAHAHA**")
    sleep(2)
    await typew.edit("**MAKAN TUH PLASTIK AWOKWOKWOKWOK**")
    
CMD_HELP.update({
    "memes12":
    "`.jamet`\
    \nUsage:\
    \n\n.berantem\
    \nUsage:\
    \n\n.rp\
    \nUsage:"
 
}) 
