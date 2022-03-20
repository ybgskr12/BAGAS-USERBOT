#create by Bagaskara
#Yang Copas Doang, Lu kontol

from time import sleep
from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern='^.jancok(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("**Woi Jancok !**")
    sleep(2)
    await typew.edit("**Lu Tau ga ? Lu itu Djancok Gausah Sok Keras !**")
    sleep(2)
    await typew.edit("**Muka Lu Kayak Kontol**")

# Create by myself @ybgskr_ex 

@register(outgoing=True, pattern='^.huek(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("**Huek Cuih !**")
    sleep(2)
    await typew.edit("**Sempak Lu Kagak Pernah Ganti Ya !**")
    sleep(2)
    await typew.edit("**Pantes Kontol Lu Burik**")
    sleep(2)
    await typew.edit("**Order Vcs Aja Gaada Yang Mau Gblk !**")
    sleep(2)
    await typew.edit("**Makanya Jadi Orang Cakepan Dikit Kontol !**")
    sleep(2)
    await typew.edit("**Mending Lu Diem Unggas !!**")

# Create by myself @ybgskr_ex

@register(outgoing=True, pattern='^.galak(?: |$)(.*)')
    async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(2)
    await typew.edit("**Jangan kek anjing lu pada !**")
    sleep(2)
    await typew.edit("**Djancok Lu !**")

#Reqwest by Kemal Luqman

CMD_HELP.update({
    "djancok":
    "`.jancok` ; `.huek` ; `.galak`\
    \nUsage: liat aja."
})
