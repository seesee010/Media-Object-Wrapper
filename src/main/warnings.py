# This class provides Warn messages. 

class Warnings:
    def movError(msg: str, filename: str) -> None:
        if (filename != None):
            print(f"[ERROR]: {msg} (?: {filename} )");
        else:
            print(f"[ERROR]: {msg}");

    def movWarn(msg: str, filename: str) -> None:
        if (filename != None):
            print(f"[WARNING]: {msg} (?: {filename} )");
        else:
            print(f"[WARNING]: {msg}");
