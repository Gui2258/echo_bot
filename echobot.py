from pyrogram import Client, filters

app = Client("my_bot")


@app.on_message(filters.private)
async def echo(client, message):
    await app.send_message(message.chat.id,f'Hola {message.from_user.first_name} este bot está en desarrollo aún')


app.run()  # Automatically start() and idle()