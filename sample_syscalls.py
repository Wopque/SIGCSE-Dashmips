#
# THIS IS A SAMPLE OF HOW TO BUILD CUSTOM DASHMIPS SYSCALLS
#

"""Syscalls related to printing."""
from . import mips_syscall
from ..models import MipsProgram
from ..utils import intify, bytesify
from struct import Struct
from sys import stdout


def print_unbuffered(s: str):
    """Print string unbuffered."""
    stdout.write(s)
    stdout.flush()


@mips_syscall(4)
def print_string(program: MipsProgram):
    """Print string. $a0 = address of null-terminated string to print."""
    address = program.registers["$a0"]
    string = program.memory.read_str(address)
    print_unbuffered(string)


@mips_syscall(11)
def print_char(program: MipsProgram):
    """Print character. $a0 = character to print."""
    character = chr(program.registers["$a0"] & 0xFF)
    if ord(" ") <= ord(character) <= ord("~") or character in ("\n", "\t", "\r"):
        # is printable
        print_unbuffered(character)


@mips_syscall(1)
def print_int(program: MipsProgram):
    """Print Int in Dec. $a0 = integer to print."""
    stdout.write(str(program.registers["$a0"]))
    stdout.flush()
