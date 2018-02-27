import command_server

def thanks(*args):
   message = 'спасибо на хлеб не намажешь'
   return message, ''

thanks_command = command_server.Command()

thanks_command.keys = ['спасибо', 'пасиб' , 'спс', 'спасибочки', 'пасиба']
thanks_command.description = 'поблагодарить душку-бота'
thanks_command.process = thanks