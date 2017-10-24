import sys
from colorama import init,Fore, Back, Style

colorCode = {
	'Error': Fore.RED + Back.WHITE,
	'Warning': Fore.BLACK + Back.YELLOW,
	'Data': Fore.GREEN,
	'Correct': Fore.BLUE + Back.WHITE,
	'Information': Style.RESET_ALL,
	'Strong': Fore.WHITE + Back.GREEN,
	'Default': Style.RESET_ALL
}

# Initialization of the colorama class. 
# Required prior to logging messages.
def initColorama():
    init()
    pass

# Log color messages to console.
# @params:  message: Message to log (str, numbers or vectors)
def log(message, colorCode = '', bold = False):
    'This works only in terminal'
    if not ("idlelib" in sys.modules):
        if (bold):
            print(colorCode + '\033[1m' + str(message) + '\033[0m' + Style.RESET_ALL)
        else:
            print(colorCode + str(message) + Style.RESET_ALL)
    else:
        print(message)
    pass