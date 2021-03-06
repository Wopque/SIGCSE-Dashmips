#
# THIS IS A SAMPLE OF HOW TO GRADE STUDENT WORK USING PYTHON & DASHMIPS
#

from dashmips.preprocessor import preprocess
from dashmips.run import run

for _ in range(1):  # This is where you can iterate through all student's programs
    # Run function takes a callback * run condition * (evaluates each step of a student's program)
    f = open("test_memory_visualizer.mips")
    student_program = preprocess(f)

    # Ensures that a student's program is not longer than 500 instructions
    assert len(student_program.source) < 500

    def check_runnable(p):
        # This is where to set a condition to test students' programs
        assert p.registers["$k0"] == 0
        assert p.registers["$k1"] == 0
        if not p.exited:
            l = p.source[p.registers["pc"]]
            print(f"{l.filename.split('/')[-1]}:{l.lineno} - {l.line}")

        return not p.exited

    run(student_program, check_runnable)
