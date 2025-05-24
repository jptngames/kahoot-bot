import asyncio
from random import randint
import kahoot
from kahoot import KahootClient
from kahoot.packets.impl.respond import RespondPacket
from kahoot.packets.server.game_over import GameOverPacket
from kahoot.packets.server.game_start import GameStartPacket
from kahoot.packets.server.question_end import QuestionEndPacket
from kahoot.packets.server.question_ready import QuestionReadyPacket
from kahoot.packets.server.question_start import QuestionStartPacket

client: KahootClient = KahootClient()
print('''

██╗  ██╗ █████╗ ██╗  ██╗ ██████╗  ██████╗ ████████╗    ██████╗  ██████╗ ████████╗
██║ ██╔╝██╔══██╗██║  ██║██╔═══██╗██╔═══██╗╚══██╔══╝    ██╔══██╗██╔═══██╗╚══██╔══╝
█████╔╝ ███████║███████║██║   ██║██║   ██║   ██║       ██████╔╝██║   ██║   ██║   
██╔═██╗ ██╔══██║██╔══██║██║   ██║██║   ██║   ██║       ██╔══██╗██║   ██║   ██║   
██║  ██╗██║  ██║██║  ██║╚██████╔╝╚██████╔╝   ██║       ██████╔╝╚██████╔╝   ██║   
╚═╝  ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝    ╚═╝       ╚═════╝  ╚═════╝    ╚═╝  
''')
async def game_start(packet: GameStartPacket):
    print('Quiz iniciado!!')

async def game_over(packet: GameOverPacket):
    print('\n\nJogo Finalizado\nBot by https://github.com/jptngames\nAVISO: Para usar o modo revanche, deixe o programa rodando sem parar. Se ele parar por algum motivo, vá até a linha 43 e troque o nome que aparece entre aspas\nnão recomendado usar esse método.')

async def question_start(packet: QuestionStartPacket):
    print('Questão iniciada')
    question_number: int = packet.game_block_index
    choice: int = randint(0,3)
    await client.send_packet(RespondPacket(client.game_pin, choice, question_number))
    print(f'Questão respondida: Alternativa {choice + 1}')

async def question_end(packet: QuestionEndPacket):
    print('Questão Encerrada!!')

async def question_ready(packet: QuestionReadyPacket):
    print('Questão lida!!')

async def main():
    # variavel que armazena o nick/nome do computador
    nick: str = 'Computador'

    # eventos:
    client.on("game_start", game_start)
    client.on("game_over", game_over)
    client.on("question_start", question_start)
    client.on("question_end", question_end)
    client.on("question_ready", question_ready)

    # entrando no quiz:
    print(f'O bot será conectado como: {nick}')
    while True:
        try:
            # váriavel responsavel pelo codigo:
            game_pin: int = input('Coloque o código do quiz: ')
            await client.join_game(game_pin, nick)
            break
        except kahoot.exceptions.GameNotFoundError:
            print(f'O código {game_pin} está incorreto!!')
    
    
# NÃO MEXA NO CÓDIGO!! MODIFICAÇÕES PODEM QUEBRAR O BOT INTEIRO PRINCIPALMENTE A PARTE ACIMA DESSE COMENTÁRIO E A PARTE DEBAIXO!!
if __name__ == '__main__':
    asyncio.run(main())