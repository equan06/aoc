
def load_program():
    with open('input_day5.txt') as f:
        return [int(x) for x in f.read().split(',')]

class IntCode: 
    def __init__(this, input, program):
        this.input = input
        this.index = 0
        this.program = program
        this.log = []

    def run_program(this):
        output = 0
        while output == 0:
            output = this.parse()
            # print(this.log)

    def parse(this):
        """
        Parse the instruction at the current index and return output, if any.
        """    
        index = this.index
        program = this.program
        # apparently opcodes without modes exist, so this parsing doesnt work anymore. yay!
        instruction = str(program[index])
        opcode, modes = int(instruction[-2:]), instruction[:-2][::-1]
        modes = [int(x) for x in modes]
        while len(modes) < 3:
            modes.append(0)

        this.log.append(opcode)
        if opcode == 99:
            return -1
        try:
            # breakup into fxns?
            a = program[index + 1] if modes[0] else program[program[index + 1]]
            if opcode == 1:
                b = program[index + 2] if modes[0] else program[program[index + 2]]
                program[index + 3] = a + b
                this.index += 4
            elif opcode == 2:
                b = program[index + 2] if modes[0] else program[program[index + 2]]
                program[index + 3] = a * b
                this.index += 4
            elif opcode == 3:
                program[program[index + 1]] = this.input
                this.index += 2
            elif opcode == 4:
                out = program[program[index + 1]]
                this.index += 2
                return out
            return 0
        except:
            return -1

if __name__ == '__main__':
    program = load_program()
    cmp = IntCode(1, program)
    cmp.run_program()
