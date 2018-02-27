import command_server

def info(*args):
   message = 'Йо, смотри пока как тут все устроено:\n'
   for c in command_server.command_list:
        message += c.keys[0] + ' - ' + c.description + '\n'
   return message, ''

info_command = command_server.Command()
info_command.keys = ['хелп', 'помощь', 'помоги', 'help']
info_command.description = 'сопсно какие команды поддерживаются'
info_command.process = info
