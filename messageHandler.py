import vk_core_processing
import importlib
import os
from command_server import command_list

def load_modules():
   files = os.listdir("mysite/commands")
   modules = filter(lambda x: x.endswith('.py'), files)
   for m in modules:
       importlib.import_module("commands." + m[0:-3])

def get_answer(body):
   message = "Привет, кожаный ублюдок! начни че-нить писать или напиши хелп -\
   и я объясню, чего тут и как . Есичо - я только родился, а мой батя алкаш,\
   поэтому не обессудь, дождись ответа кожаных админов, чтоб их"
   attachment = " "
   arg = None
   command = body.split(" ", 1)[0]
   try:
       arg = body.split(" ", 1)[1]
   except IndexError:
       pass
   for c in command_list:
       if command in c.keys:
           #message, attachment = "Теплее! аргумент :", ''
           #if arg:
           #   message += arg
           message, attachment = c.process(arg)
   return message, attachment

def create_answer(data, token):
   load_modules()
   user_id = data['user_id']
   message, attachment = get_answer(data['body'].lower())
   vk_core_processing.send_message(user_id, token, message, attachment)