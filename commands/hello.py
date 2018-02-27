import command_server

def hello(*args):
   message = 'Че-кого, братюнь/сестрюнь'
   return message, ''

hello_command = command_server.Command()

hello_command.keys = ['привет', 'hello', 'дратути', 'здравствуй',
                        'здравствуйте', 'прив', 'привеееет', 'эй', 'зига', 'йо',
                        'чекого', 'че-кого']
hello_command.description = 'ну это типа поздороваться'
hello_command.process = hello