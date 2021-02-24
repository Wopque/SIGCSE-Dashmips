from dashmips import preprocess, run

for _ in range(1):  # This is where you can iterate through all student's programs
    # Run function takes a callback * run condition * (evaluates each step of a student's program)
    f = open("sample.mips").read()
    student_program = preprocess(f)

    # Ensures that a student's program is not longer than 500 instructions
    assert len(student_program.source) < 500

    def check_runnable(p):
        # This is where to set a condition to test students' programs
        assert p.registers["$k0"] == 0
        assert p.registers["$k1"] == 0

        return p.exited

    run(student_program, check_runnable(student_program))
