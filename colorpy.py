CSI = "\x1B["
reset = CSI+"m"

# Test
# print CSI+"32;41m" + "Colored Text" + CSI + "0m"


def red(message):
    return CSI+"31;49m" + message + CSI + "0m"


def green(message):
    return CSI+"32;49m" + message + CSI + "0m"


def yellow(message):
    return CSI+"33;49m" + message + CSI + "0m"

# Refs:
# https://en.wikipedia.org/wiki/ANSI_escape_code#CSI_codes
# http://stackoverflow.com/a/287896/3147039
