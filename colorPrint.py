class CLColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    @staticmethod
    def printSucces(s):
        print(f"{CLColors.HEADER}{s}{CLColors.ENDC}")
    
    @staticmethod
    def printError(s):
        print(f"{CLColors.FAIL}{s}{CLColors.ENDC}")

    @staticmethod
    def printWarning(s):
        print(f"{CLColors.WARNING}{s}{CLColors.ENDC}")

    @staticmethod
    def printOkB(s):
        print(f"{CLColors.OKBLUE}{s}{CLColors.ENDC}")