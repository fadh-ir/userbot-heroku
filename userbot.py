from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession
import os

# GUNAKAN DATA KAMU (Sudah dimasukkan)
API_ID = 20520397
API_HASH = "bc7b06533abffb51a57904962a93c276"
SESSION_STRING = "1BVts0JUBu3m-B3vBDW3QyR89P0f_pzpL1nmQ4 GIic4wWyoZbEsRVMiNJI14jFAGP01HnV5TbwA9 PlBeahFXl1SHCkzhcFIoAjBrKjgiNdhRz60M61 ¿YIVU9rTnFS5Yv6fa4W0TF5hWHM0YWB1vP90Wd 06GRqLqQ5GtMJB_00Fc8_-HCfKWbHSko7Ways8 9fAMwPWOAY_eAbTeY4X9AS1z7PxFkllhEs0aPa YpJrrgg9BGfS9dIhIJDvTSk_K5V2ro4j_mpZS2 tFbPvz0rnKBg9aiZMzqpntM1t-28BNG0gk7pfg CqmyvLdH9v0yJUfnLlvk0IuEoVkvZ6suftIH2w LPllPjlZX0="

client = TelegramClient(StringSession(SESSION_STRING), API_ID, API_HASH)

@client.on(events.NewMessage(pattern="/gcast (.+)", outgoing=True))
async def gcast_handler(event):
    if event.sender_id != 6213226014:  # ID pemilik bot
        await event.reply("❌ Kamu tidak diizinkan menggunakan perintah ini.")
        return

    msg = event.pattern_match.group(1)
    done = 0
    failed = 0

    async for dialog in client.iter_dialogs():
        try:
            await client.send_message(dialog.id, msg)
            done += 1
        except:
            failed += 1

    await event.reply(f"✅ GCAST selesai!\nSukses: {done} grup/chat\nGagal: {failed}")

print("🔄 Menjalankan userbot...")
client.start()
client.run_until_disconnected()
