import command_server

def song(*args):
   #message='<iframe width="347" height="195" src="https://www.youtube.com/embed/v6zl6VdvU8A" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>'
   #message = 'https://www.youtube.com/watch?v=v6zl6VdvU8A'
   message = "Пока в процессе имплементации сорян"
   attachment = 'https://www.youtube.com/watch?v=v6zl6VdvU8A'
   return message, attachment

song_command = command_server.Command()

song_command.keys = ['песня']
song_command.description = 'присылает ссылочку на случайный клип нтрю пока тестируем'
song_command.process = song