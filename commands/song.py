import command_server
import random

def song(*args):
   message = "ну чет такое например\n"
   link_list = ["s5D6JSCGD0c", "QLBRYAPRBy4", "iw-p3EBEGlA", "cdX8r3ZSzN4"]
   message +="https://youtu.be/" + link_list[random.randint(0,len(link_list)-1)]
   attachment = ""
   return message, attachment

song_command = command_server.Command()

song_command.keys = ['песня']
song_command.description = 'присылает ссылочку на случайный клип нтр. \
                            вроде работает, но клипов пока немного'
song_command.process = song