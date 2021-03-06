#
# THIS IS A SAMPLE OF HOW TO BUILD CUSTOM DASHMIPS SYSCALLS
#

"""Syscalls related to printing."""
from . import mips_syscall
from ..models import MipsProgram
from ..utils import intify, bytesify
from struct import Struct
from sys import stdout


@mips_syscall(4)
def print_string(program: MipsProgram):
    """Print string. $a0 = address of null-terminated string to print."""
    address = program.registers["$a0"]
    string = program.memory.read_str(address)
    print(string)
