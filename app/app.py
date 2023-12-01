from dotenv import load_dotenv
from twitchio.ext import commands
import random
import os
import time

# Cargar variables desde el archivo .env
load_dotenv()

# Obtener variables del entorno
oauth_token = str(os.getenv("OAUTH_TOKEN"))
bot_prefix = str(os.getenv("BOT_PREFIX"))
channel = str(os.getenv("CHANNEL"))

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=oauth_token, prefix=bot_prefix, initial_channels=[channel])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    # Leer comandos desde los archivos correspondientes
    with open('comandos_prioritarios.txt', 'r') as file:
        comandos_prioritarios = [line.strip() for line in file.readlines()]

    with open('comandos_secundarios.txt', 'r') as file:
        comandos_secundarios = [line.strip() for line in file.readlines()]

    @commands.command()
    async def bombaR(self, ctx: commands.Context):
        while True:
            # Elegir un comando con más frecuencia del listado prioritario
            if random.random() < 0.7:  # Ajusta el porcentaje según la frecuencia deseada
                mensaje = random.choice(bot.comandos_prioritarios)
            else:
                mensaje = random.choice(bot.comandos_secundarios)
            await ctx.send(mensaje)
            time.sleep(.3)  # Ajusta el tiempo de espera entre mensajes

bot = Bot()
bot.run()