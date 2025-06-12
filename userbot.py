from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession
import os

# GUNAKAN DATA KAMU (Sudah dimasukkan)
API_ID = 20520397
API_HASH = "bc7b06533abffb51a57904962a93c276"
SESSION_STRING = "1BVts0LMBu0HfDDJ1t-bfCtSnTDz4x520RVz493w9U95uR3XZcaSYLi3Ai0JdY1b5wlyTFCFv0aeuUDOQtmcqKqrzkJNIX-SKIOB75F1SBII8Wip32YmbfiftYcLgiJ8LZqFUaCHeK1N8nPD4GQtNea28ysV8d3tI4HZwq4XH3kH6UJB1by2r9GYB714EoQX0uVvB9pnz7xPW7rejSjR3aJvwX9DorVdkWr813tM7b5QCn6N_LmNy4CBF8HhmSQvRtT-7EtgArjJ3FURcwG_jgG1vcv0mtLqfXgofMghY5fskfbgqza3WZx3Sjd3-gHZD4RktgPx8SgTGZE1EKxS7W7XqGRFBk1I"

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
