import command_server
import random
MAX_SECONDS = 84400

def call(*args):
   if args and args[0]:
       if args[0].lower() == 'тыжпрограммиста':
            message = "Заявка принята.\n Тыжпрограммист приедет через \n"
            for i in range(3):
                seconds = random.randint(0,MAX_SECONDS)
                m, s = divmod(seconds, 60)
                h, m = divmod(m, 60)
                message += str(h) + " часов " + str(m) + " минут " + str(s) + " секунд. \
                Ой то есть через... \n"
            message += "К сожалению, в данный момент все тыжпрограммисты заняты.\
            Вам напишет первый освободивший оператор"
       else:
           message = "Таких не держим тут, сорян"
   else:
       message = "Кого тебе вызвать-то, врача лол? Смотри, тут нужно так:\
                  вызвать ПРОБЕЛ %кого_вызвать% пока можно вызвать только \
                  тыжпрограммиста, но ты можешь попробовать что-то еще каешн"
   return message, ''

call_command = command_server.Command()

call_command.keys = ['вызвать', 'вызов']
call_command.description = 'компьютерный мастер Владислав'
call_command.process = call