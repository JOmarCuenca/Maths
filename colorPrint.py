import enum

class ColorType(enum.Enum):
    successGreen    = '\033[92m'
    successBlue     = '\033[94m'
    header          = '\033[95m'
    warning         = '\033[93m'
    fail            = '\033[91m'
    bold            = '\033[1m'
    underline       = '\033[4m'
    endc            = '\033[0m'

class CLColors:

    @staticmethod
    def getColorString(string = "",color = ColorType.header) -> str:
        return f"{color.value}{string}{ColorType.endc.value}"

    @staticmethod
    def printSucces(s):
        s = CLColors.getColorString(s,ColorType.successGreen)
        print(s)
    
    @staticmethod
    def printError(s):
        s = CLColors.getColorString(s,ColorType.fail)
        print(s)

    @staticmethod
    def printWarning(s):
        s = CLColors.getColorString(s,ColorType.warning)
        print(s)

    @staticmethod
    def printOkB(s):
        s = CLColors.getColorString(s,ColorType.successBlue)
        print(s)