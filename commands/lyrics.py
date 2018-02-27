import command_server
from utils import get_song_alias

def lyrics(*args):
    message = "Чет ты не так делаешь, по-моему. ща научу как надо:\
               текст ПРОБЕЛ %песня%. Песню можно в свободной форме.\
               Например текст хуяк я понимаю. ну и все вот в таком духе"
    if args and args[0]:
        path = "mysite/content/texts/"
        name = path + get_song_alias(args[0]) + ".txt"
        message = name
        try:
            f= open(name,'r')
            message = f.read()
            f.close()
        except FileNotFoundError:
            message = 'Сорян, чет такого не найду. Может, и не было такого. \
            А может админы не добавили'
    return message, ''

lyrics_command = command_server.Command()
lyrics_command.keys = ['текст']
lyrics_command.description = 'текст песни, пока в разработке'
lyrics_command.process = lyrics
