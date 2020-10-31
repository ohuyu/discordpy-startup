from discord.ext import commands
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
tenple = "テンプレートはこちらです。\n\n【名前】\n【年齢】\n【住み】\n【趣味】\n【一言】"

if message.channel.id in [772085784442044426]:
    [await (await message.channel.fetch_message(m.id)).delete() for m in await message.channel.history(limit=100).flatten() if m.content == tenple]
    await message.channel.send(f"{tenple}")

tenple = "テンプレートはこちらです。\n\n【名前】\n【年齢】\n【住み】\n【趣味】\n【一言】" #テンプレの中身

if message.channel.id in [772085784442044426]: 
    for m in await message.channel.history(limit=100).flatten(): #発言されるごとにチャンネル内の100メッセージを取得(BOTが止まってた時期も考慮するための100)
        if m.content == tenple: #mはメッセージオブジェクト。オブジェクトの内容からメッセージを取得してもしもテンプレと同じだった場合は次の処理
            get_message = await message.channel.fetch_message(m.id) #そのチャンネルからメッセージを取得するための処理
            await get_message .delete() #取得したメッセージを削除
    await message.channel.send(f"{tenple}") #forを回し終えて再度テンプレを送信する


bot.run(token)
