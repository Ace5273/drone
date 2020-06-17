import re
from inspect import  currentframe

def convert(all_command: str):

    # Get the command and the others
    command,*rest = all_command.split(' ')

    # Set the string params
    str_params= '' if len(rest) == 0 else ' ' + ' '.join(map(lambda a: '{'+a+'}',rest))
    send_params = f'\'{command}\'' if str_params=='' else f'f\'{command}{str_params}\''

    # Set the func params
    func_params=', '.join(['self',*rest])

    # Change the function name if end with \?
    func_name = command if command[-1] != '?' else 'get_'+command[:-1]
    
    # Create the function as a string
    func_as_string=f'def {func_name}({func_params}):\n    self.send({send_params})'

    return func_as_string

def change_text_file():

    with open('./text.txt','r') as f:
        text = f.read()
    
    all_commands = re.findall(r'[^ \n][\w ]+[\w\?]',text)

    with open('./result.txt','w') as f:
        f.write('\n\n'.join(map(convert,all_commands)))

change_text_file()
