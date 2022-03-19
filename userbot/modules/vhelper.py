""" Userbot module for other small commands. """
from userbot import CMD_HELP, ALIVE_NAME
from userbot.events import register


# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.helpmy$")
async def usit(e):
    await e.edit(
        f"**Hai {DEFAULTUSER} Kalau Anda Tidak Tau Perintah Untuk Memerintah Ku Ketik** `.xhelp` Atau Bisa `.help` atau Minta Bantuan Ke:\n"
        "\n[Bagaskara😈](t.me/ybgskr_ex)"
        "\n\n[Support](https://t.me/allfucek)"
        "\n\n[Channel](https://t.me/loveisfuckedup)")


@register(outgoing=True, pattern="^.rvars$")
async def var(m):
    await m.edit(
        f"**Disini Daftar Vars Dari {DEFAULTUSER}:**\n"
        "\n[DAFTAR VARS](https://raw.githubusercontent.com/ybgskr12/BAGAS-USERBOT/BAGAS-USERBOT/varshelper.txt)")


CMD_HELP.update({
    "Bagashelper":
    "`.helpmy`\
\nPenjelasan: Bantuan Untuk Bagaskara-Userbot.\
\n`.rvars`\
\nPenjelasan: Untuk Melihat Beberapa Daftar Vars."
})
