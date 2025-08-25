# make an interactive converstaion tool that replys, seemingly human
from colorama import Fore, Style
name = input(Fore.CYAN + "What is your name? : " + Style.RESET_ALL).strip().title()
#split user's nam into first and last name
first, middle, last = name.split(" ")
print(Fore.BLUE + f"Hello {first}")
age = input(Fore.CYAN + "what is your age? : " + Fore.YELLOW) 
print(Fore.BLUE + f"Wow," + Fore.YELLOW + name + Fore.BLUE + f", you look great for " + Fore.YELLOW + age + Fore.BLUE + f" years old!")


