import itertools
from colorama import Fore, Style, init

init(autoreset=True)

RED = Fore.LIGHTRED_EX
GREEN = Fore.LIGHTGREEN_EX
CYAN = Fore.LIGHTCYAN_EX
RESET = Style.RESET_ALL

def is_valid_positioning(positions):
    """Ensure no consecutive positions."""
    for i in range(len(positions) - 1):
        if positions[i] + 1 == positions[i + 1]:
            return False
    return True

def generate_dot_aliases(email):
    prefix, domain = email.split('@')
    
    dot_aliases = [email]  # Start with the original email
    
    # Generate aliases for 0 to len(prefix)-1 dots
    for num_dots in range(1, len(prefix)):
        for positions in itertools.combinations(range(1, len(prefix)), num_dots):
            if is_valid_positioning(positions):
                dotted_prefix = list(prefix)
                for pos in sorted(positions, reverse=True):
                    dotted_prefix.insert(pos, '.')
                dot_aliases.append(''.join(dotted_prefix) + '@' + domain)

    return dot_aliases

ex = print(f'{CYAN}Example: Generate dot-aliases for a Gmail address{RESET}')
email = input(f'Enter a Gmail address {RED}(without @ domain):{RESET}{GREEN} ')

# Ensure that the input has the "@gmail.com" suffix or set to default
if not email.endswith("@gmail.com") and not email.endswith("@googlemail.com"):
    email += "@gmail.com"

for domain in ["@gmail.com", "@googlemail.com"]:
    current_email = email.replace("@gmail.com", domain)
    dot_aliases = generate_dot_aliases(current_email)
    
    print(f"{CYAN}{current_email} (for {domain}):{RESET}")
    for alias in dot_aliases:
        print(f"{GREEN}{alias}")
    print("-----")
