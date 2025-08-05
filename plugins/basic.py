from pyrogram import Client, filters
from pyrogram.types import Message, ChatPermissions

OWNER = "👑 Owner: @KRIYANSH_CHOUDHARY"

@Client.on_message(filters.command("lock") & filters.group & filters.user("admin"))
async def lock_group(_, message: Message):
    await message.chat.set_permissions(ChatPermissions())
    await message.reply_text("🔒 Group has been locked.\n" + OWNER)

@Client.on_message(filters.command("unlock") & filters.group & filters.user("admin"))
async def unlock_group(_, message: Message):
    await message.chat.set_permissions(
        ChatPermissions(can_send_messages=True, can_send_media_messages=True)
    )
    await message.reply_text("🔓 Group has been unlocked.\n" + OWNER)

@Client.on_message(filters.command("mute") & filters.group & filters.user("admin"))
async def mute_user(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("किसी यूज़र के मैसेज पर reply करो।")
    user_id = message.reply_to_message.from_user.id
    await message.chat.restrict_member(user_id, ChatPermissions())
    await message.reply_text(f"🔇 User muted.\n{OWNER}")

@Client.on_message(filters.command("unmute") & filters.group & filters.user("admin"))
async def unmute_user(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("किसी यूज़र के मैसेज पर reply करो।")
    user_id = message.reply_to_message.from_user.id
    await message.chat.unban_member(user_id)
    await message.reply_text(f"🔊 User unmuted.\n{OWNER}")

@Client.on_message(filters.command("ban") & filters.group & filters.user("admin"))
async def ban_user(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("किसी यूज़र के मैसेज पर reply करो।")
    user_id = message.reply_to_message.from_user.id
    await message.chat.ban_member(user_id)
    await message.reply_text(f"🚫 User banned.\n{OWNER}")

@Client.on_message(filters.command("unban") & filters.group & filters.user("admin"))
async def unban_user(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("किसी यूज़र के मैसेज पर reply करो।")
    user_id = message.reply_to_message.from_user.id
    await message.chat.unban_member(user_id)
    await message.reply_text(f"✅ User unbanned.\n{OWNER}")

@Client.on_message(filters.command("purge") & filters.group & filters.user("admin"))
async def purge_messages(_, message: Message):
    if not message.reply_to_message:
        return await message.reply("जिस मैसेज से डिलीट शुरू करनी है, उस पर reply करो।")
    from_id = message.reply_to_message.id
    to_id = message.id
    for msg_id in range(from_id, to_id):
        try:
            await message.chat.delete_messages(msg_id)
        except:
            pass
    await message.reply_text(f"🧹 Messages purged.\n{OWNER}")
