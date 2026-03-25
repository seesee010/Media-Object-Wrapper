# Copyright (c) 2026 KittyKat-yt. 
# see Third-Party-License/ for more informations

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
