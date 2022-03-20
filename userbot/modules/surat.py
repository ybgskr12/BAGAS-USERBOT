from time import sleep

from userbot import CMD_HELP
from userbot.events import register


@register(outgoing=True, pattern="^.alfatihah(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**audzūbillãh himinàs'syaitõn-'nirojīm**")
    sleep(1)
    await typew.edit("**bismillāhir-raḥmānir-raḥīm**")
    sleep(1)
    await typew.edit("**al-ḥamdu lillāhi rabbil-'ālamīn**")
    sleep(1)
    await typew.edit("**ar-raḥmānir-raḥīm**")
    sleep(1)
    await typew.edit("**māliki yaumid-dīn**")
    sleep(1)
    await typew.edit("**iyyāka na'budu wa iyyāka nasta'īn**")
    sleep(1)
    await typew.edit("**ihdinaṣ-ṣirāṭal-mustaqīm**")
    sleep(1)
    await typew.edit("**ṣirāṭallażīna an'amta 'alaihim gairil-magḍụbi 'alaihim wa laḍ-ḍāllīn**")
    sleep(1)
    await typew.edit("**Aamiin..**")


@register(outgoing=True, pattern="^.ayatkursi(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(1)
    await typew.edit("**Bismillahir'-rahmanir-rahim**")
    sleep(1)
    await typew.edit("**Allaahu Laailaaha illa huwal hayyul qayyuum**")
    sleep(1)
    await typew.edit("**Laa ta'khudzuhu sinatuw walaa nauum**")
    sleep(1)
    await typew.edit("**Lahuu maa fissamaawaati wamaa fil ardhi**")
    sleep(1)
    await typew.edit("**Mangdzalladzii yasyfa'u 'indahuu illai bi idznih**")
    sleep(1)
    await typew.edit("**Ya'lamu maa baina aiydiihim wamaa kholfahum**")
    sleep(1)
    await typew.edit("*walaa yukhiithuuna bisyayin min 'ilmihii illaa bimaa syaaa**")
    sleep(1)
    await typew.edit("**wasi'a kursiyyuhus samaawaati wal ardho**")
    sleep(1)
    await typew.edit("**Walaa yauduhuu khifdhuhumaa wa huwal'aliyyul 'adhiim**")
    sleep(1)
    await typew.edit("**Alhamdulillah..**")


# Create by @jooganteng

CMD_HELP.update(
    {
        "surat": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.alfatihah`\
    \n↳ : Menulis Surat Alfatihah."
        "surat": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ayatkursi`\
    \n↳ : Menulis Ayat Kursi."
    }
)
