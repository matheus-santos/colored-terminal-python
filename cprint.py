# Consts
class struct_color:
    BLACK = 30
    RED = 31
    GREEN = 32
    YELLOW = 33
    BLUE = 34
    MAGENTA = 35
    CYAN = 36
    WHITE = 37


# Ctor
# Base for further methods
def _cprint(message, color):
    return CSI+"31;49m" + message + CSI + "0m"

# Variables
CSI = "\x1B["  # Control Sequence Introducer
reset = CSI+"m"  # Reseting configs
colors = struct_color()  # Object with consts representing ANSI colors
methods = [  # Method's name to build dinamically
    "black", "red", "green", "yellow",
    "blue", "magenta", "cyan", "white"
]

# Building functions using dinamic programming
for method in methods:
    exec """def {0}(message):\n
        return _cprint(message, colors.{1})
    """.format(method, method.upper())
