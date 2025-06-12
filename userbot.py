from telethon import TelegramClient, events, sync
from telethon.sessions import StringSession
import os

# GUNAKAN DATA KAMU (Sudah dimasukkan)
API_ID = 20520397
API_HASH = "bc7b06533abffb51a57904962a93c276"
SESSION_STRING = "1BVts0LoBu0S0ohX1bZVU09Xv52zdpmoIuywvVyp96ynodflj03v_BJWwxEStiw71f7HAzgbp40cvGJXP2e9hCZRgQRF3yevuyU0eYyGx9aFLxbfDwW2DqSuLV1nRRQSJmlZpkk-74Bp_gBq00pQIQd5pR5tQtep5zqcqRJyY05Y3FE7v0URXmsgb8JDujX1YPp6A04perYxP4JysFTwKodoCr3v-PmxHpFB8INBtiB755x4awV-FOLVrzGyW100XprpZ48ZeLAHvAHZ1qTRPtc2DmogeGbAFFxBnhy0nB3gVjKcsc5zDcg5LGA00Fmp6BvE5mwFdos2l15SaCE0y2NBq6iyY5g8=
"

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
