import colorama
from colorama import *

colorama.init(autoreset=True)
print(f"{Fore.RED} Cool")

print(f"{Back.BLUE} Cool")

print(f"{Style.BRIGHT} Cool")

print(f"{Fore.RED + Back.BLUE + Style.BRIGHT} Cool")
