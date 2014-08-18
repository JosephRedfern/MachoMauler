import struct
import sys
from structures import MachHeader, MachoFile


class MachoParse:
    def __init__(self, binary):
        header = self.parse_header(binary[:28]) #len(header) == 28bytes
        self.macho = MachoFile(header)
        print self.macho.header

    def parse_header(self, header):
        magic, cputype, cpusubtype, filetype, ncmds, sizeofcmds, flags = struct.unpack("IiiIIII", header)
        return MachHeader(magic, cputype, cpusubtype, filetype, ncmds, sizeofcmds, flags)

def main():
    #TODO: use argparse

    if len(sys.argv) > 1: 
        data = file(sys.argv[1]).read()
        MachoParse(data)
    else:
        print "[-] Please specify a filename"


if __name__ == "__main__":
    print "[*] Welcome to MachoMauler, parsing the gumph now"
    main()
