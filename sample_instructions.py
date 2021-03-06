# 
# THIS IS A SAMPLE OF HOW TO BUILD CUSTOM DASHMIPS INSTRUCTION FUNCTIONS
# 

"""Three Register instructions."""
from typing import Tuple
from re import search

from . import mips_instruction
from ..models import MipsProgram

PATTERN = r"{instr_gap}({register}){args_gap}({register}){args_gap}({register})"


def parse(args: Tuple[str, str, str, str, str]) -> Tuple[str, str, str]:
    """Parser for rd rs rt format instructions."""
    return (args[2], args[3], args[4])


@mips_instruction(PATTERN, parse)
def add(program: MipsProgram, rd: str, rs: str, rt: str):
    """Add Reg[rd] = Reg[rs] + Reg[rt]."""
    program.registers[rd] = program.registers[rs] + program.registers[rt]
