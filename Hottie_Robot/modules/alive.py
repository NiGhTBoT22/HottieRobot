# This Module Made By @AASFCYBERKING
# I Really Hardworked For This Module
# So Plz Give Credits
import asyncio
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from Hottie_Robot.events import register
from Hottie_Robot import telethn as borg
from Hottie_Robot import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins

edit_time = 5
""" =======================Hottie====================== """
file1 = "https://telegra.ph/file/960c13008180026ba29d8.jpg"
file2 = "https://telegra.ph/file/2bb74f438315a77ad3197.jpg"
file3 = "https://telegra.ph/file/f20d978416c131377ae65.jpg"
file4 = "https://telegra.ph/file/8deb66fd79cfbc3f70758.jpg"
file5 = "https://telegra.ph/file/51190abbdf5f8095f21a9.jpg"
""" =======================Hottie====================== """

BUTTON = [
    [
        Button.url("【►Sᴜᴘᴘᴏʀᴛ◄】", "https://t.me/Hottie_support"),
        Button.url("【►Updates◄】", "https://t.me/Hottie_Updates"),
    ]
]


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ("week", 60 * 60 * 24 * 7),
    ("day", 60 * 60 * 24),
    ("hour", 60 * 60),
    ("min", 60),
    ("sec", 1),
)


async def _human_time_duration(seconds):
    if seconds == 0:
        return "inf"
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append("{} {}{}".format(amount, unit, "" if amount == 1 else "s"))
    return ", ".join(parts)


@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    pm_caption = f"** ♡ Hey {yes.sender.first_name} I,m Hottie **\n\n"
    pm_caption += f"**♡ My Uptime :** `{uptime}`\n\n"
    pm_caption += f"**♡ Telethon Version :** `{version.__version__}`\n\n"
    pm_caption += "**♡ My Master :** [Δŕyαŋ](https://t.me/Storm_terror)/[Kishore](https://t.me/@AASFCYBERKING) "
    BUTTON = [
        [
            Button.url("【►Sᴜᴘᴘᴏʀᴛ◄】", "https://t.me/Hottie_support"),
            Button.url("【►Updates◄】", "https://t.me/Hottie_Updates"),
        ]
    ]
    on = await borg.send_file(
        yes.chat_id, file=file1, caption=pm_caption, buttons=BUTTON, reply_to=yes
    )

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file1, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file2, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file4, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file5, buttons=BUTTON)