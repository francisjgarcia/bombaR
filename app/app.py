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
check_user_1 = str(os.getenv("CHECK_USER_1"))
check_user_2 = str(os.getenv("CHECK_USER_2"))

class Bot(commands.Bot):
    check_user_count = 0
    verified_keys = False

    def __init__(self):
        super().__init__(token=oauth_token, prefix=bot_prefix, initial_channels=[channel])

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')

    @commands.command(name='llave')
    async def keys(self, ctx: commands.Context):
        username = ctx.author.name
        global first_key_user
        global verified_keys

        if username == check_user_1 or username == check_user_2:
            if bot.check_user_count == 0:
                first_key_user = username
                await ctx.send(f'¡Atención! {username} está calentito. ¿Estamos listos para el caos?')
                bot.check_user_count += 1
            elif bot.check_user_count == 1 and username != first_key_user:
                await ctx.send(f'Pos va a ser que {username} se une a la fiesta....')
                bot.check_user_count += 1
                verified_keys = True
            elif bot.check_user_count == 1 and username == first_key_user:
                await ctx.send(f'¡Eh, eh, eh! Quieto parao {username} no te pases de listo, sólo tienes una llave, parguela')
            elif bot.check_user_count == 2:
                await ctx.send(f'¡Tú, tonto {username}, no ves que ya hay dos llaves! ¡A la mierda, dale ya caña!')
        else:
            await ctx.send(f'{username} eres un parguela')

    @commands.command(name='catella')
    async def stop(self, ctx: commands.Context):
        username = ctx.author.name
        if username == check_user_1 or username == check_user_2:
            global verified_keys
            verified_keys = False
            await ctx.send(f"{username} es un abuelo, sa cansao ya de la fiesta")
        else:
            await ctx.send(f'{username} eres un parguela')

    @commands.command(name='bombaR')
    async def bomba_r(self, ctx: commands.Context):
        global verified_keys
        previous_verified_keys = verified_keys
        if verified_keys == True:
            # Leer comandos desde los archivos correspondientes
            with open('comandos_prioritarios.txt', 'r') as file:
                comandos_prioritarios = [line.strip() for line in file.readlines()]
            with open('comandos_secundarios.txt', 'r') as file:
                comandos_secundarios = [line.strip() for line in file.readlines()]

            while True:
                # Elegir un comando con más frecuencia del listado prioritario
                if random.random() < 0.8:   # Ajusta el porcentaje según la frecuencia deseada
                    mensaje = random.choice(comandos_prioritarios)
                else:
                    mensaje = random.choice(comandos_secundarios)
                await ctx.send(mensaje)
                time.sleep(.5)  # Ajusta el tiempo de espera entre mensajes

        else:
            await ctx.send('Esperando la llave de ambos usuarios...')

bot = Bot()
bot.run()
