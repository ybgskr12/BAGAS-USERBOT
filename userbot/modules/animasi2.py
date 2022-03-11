# credit by @kyuraxx
# own kyura

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.djancok(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**WOI KALAU DEPLOY BAGASKARA-USERBOT**")
    sleep(1)
    await typew.edit("**JOIN JUGA SUPPORT NYA DJANCOK!!**")
    sleep(1)
    await typew.edit("**DEPLOY DOANG GA JOIN**")
    sleep(1)
    await typew.edit("**DASAR DJANCOK!**")

CMD_HELP.update({
    "animasi2":
    "`.djancok`\
    \nUsage: liat aja."
})
