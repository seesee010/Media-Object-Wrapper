import os
import struct
import shutil

from warnings import warnings

warn = warnings()

def littleNum(v: int, length: int) -> bytes:
    return v.to_bytes(length, "little", signed=False)

def bigNum(v: int, length: int) -> bytes:
    return v.to_bytes(length, "big", signed=False)

def getFileName(path: str) -> str:
    return os.path.split(path)[1]

class MOW:
    def __init__(self) -> None:
        self.files = []

    def addFile(self, path: str) -> None:
        if os.path.exists(path):
            self.files.append(path)
        else:
            warn.warn(f"{path} does not exist")

    def removeFiles(self) -> None:
        self.files.clear()

    def combineFiles(self, fileName: str) -> None:

        # is that filename?
        fileName += ".mow"
        with open(fileName, "wb") as fileOut:
            fileOut.write(b"Mow")
            fileOut.write(littleNum(0x1ba5, 2))

            for file in self.files:
                with open(file, "rb") as fileData:
                    name = getFileName(file)
                    length = os.path.getsize(file)

                    # 1 byte:  file name length
                    # x bytes: file name
                    # 4 bytes: file size
                    # y bytes: file content

                    fileOut.write(littleNum(len(name) & 0xff, 1))
                    fileOut.write(name.encode("utf-8"))

                    # chunk to 4 bytes
                    fileOut.write(littleNum(length & 0xffff_ffff, 4))
                    fileOut.write(fileData.read())

            fileOut.write(littleNum(0x00, 1))

    def separateFiles(self, path: str) -> None:
        with open(path, "rb") as fileIn:
            marker, magicNumber = struct.unpack("<3sH", fileIn.read(6))
            if not ((marker == b"Mow") and (magicNumber == 0x1ba5)):
                warn.error(f"{path} is not a .mow file")
                return

            outPath = f"{os.path.splitext(getFileName(path))[0]}/"
            if os.path.exists(outPath):
                shutil.rmtree(outPath)
            os.makedirs(outPath)

            while 1:
                fileNameLen = struct.unpack("", fileIn.read(1))[0]
                if fileNameLen == 0x00:
                    break
                fileName, fileLen = struct.unpack(f"<{fileNameLen}sI", fileIn.read(fileNameLen + 4))
                fileName = fileName.decode("utf-8")
                with open(outPath + fileName, "xb") as fileOut:
                    fileOut.write(fileIn.read(fileLen))
