from enum import Enum

class MachHeader:
    def __init__(self, magic, cputype, cpusubtype, filetype, ncmds, sizeofcmds, flags):
        self.magic = magic
        self.cputype = cputype #Eventually CPUType.<appropriate value>
        self.cpusubtype = cpusubtype
        self.filetype = filetype
        self.ncmds = ncmds
        self.sizeofcmds = sizeofcmds
        self.flags = flags

    def __str__(self):
        return "Magic: {0}, CPU Type: {1}, CPU Subtype: {2}, Filetype: {3}, ncmds: {4}, sizeofcmds: {5}, flags: {6}".format(
                str(self.magic), str(self.cputype), str(self.cpusubtype), str(self.filetype), str(self.ncmds),
                str(self.sizeofcmds), str(self.flags))

    class CPUType(Enum):
        #Listed at: http://llvm.org/docs/doxygen/html/Support_2MachO_8h_source.html
        CPU_TYPE_ANY       = -1
        CPU_TYPE_X86       = 7
        CPU_TYPE_I386      = CPU_TYPE_X86
        CPU_TYPE_X86_64    = CPU_TYPE_X86 | 0x01000000
        CPU_TYPE_MIPS      = 8
        CPU_TYPE_MC98000   = 10
        CPU_TYPE_ARM       = 12
        CPU_TYPE_ARM64     = CPU_TYPE_ARM | 0x01000000
        CPU_TYPE_SPARC     = 14
        CPU_TYPE_POWERPC   = 18
        CPU_TYPE_POWERPC64 = CPU_TYPE_POWERPC | 0x01000000

class MachoFile:
    def __init__(self, header): #more to come
        self.header = header
