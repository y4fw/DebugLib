# Setup Colors
ResetColor = "\033[0m"
GreenColor = "\033[32m"
RedColor = "\033[31m"
YellowColor = "\033[33m"
BlueColor = "\033[34m"

# Functions
def sucess(msg):
    print(f"{GreenColor}[SUCESSO] {msg}{ResetColor}")

def error(msg):
    print(f"{RedColor}[ERRO] {msg}{ResetColor}")

def warn(msg):
    print(f"{YellowColor}[AVISO] {msg}{ResetColor}")

def info(msg):
    print(f"{BlueColor}[INFO] {msg}{ResetColor}")
