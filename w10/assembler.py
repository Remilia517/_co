
import sys

COMP = {
    "0": "0101010", "1": "0111111", "-1": "0111010",
    "D": "0001100", "A": "0110000", "!D": "0001101",
    "!A": "0110001", "-D": "0001111", "-A": "0110011",
    "D+1": "0011111", "A+1": "0110111",
    "D-1": "0001110", "A-1": "0110010",
    "D+A": "0000010", "D-A": "0010011",
    "A-D": "0000111", "D&A": "0000000",
    "D|A": "0010101",
    "M": "1110000", "!M": "1110001",
    "-M": "1110011", "M+1": "1110111",
    "M-1": "1110010", "D+M": "1000010",
    "D-M": "1010011", "M-D": "1000111",
    "D&M": "1000000", "D|M": "1010101"
}

DEST = {
    "": "000", "M": "001", "D": "010",
    "MD": "011", "A": "100", "AM": "101",
    "AD": "110", "AMD": "111"
}

JUMP = {
    "": "000", "JGT": "001", "JEQ": "010",
    "JGE": "011", "JLT": "100", "JNE": "101",
    "JLE": "110", "JMP": "111"
}

SYMBOLS = {
    "SP": 0, "LCL": 1, "ARG": 2, "THIS": 3, "THAT": 4
}

for i in range(16):
    SYMBOLS["R" + str(i)] = i

SYMBOLS.update({
    "SCREEN": 16384,
    "KBD": 24576
})

def clean_lines(lines):
    result = []
    for line in lines:
        line = line.split("//")[0].strip()
        if line:
            result.append(line)
    return result

def assemble(filename):
    with open(filename, "r", encoding="utf-8") as f:
        lines = clean_lines(f.readlines())

    labels = {}
    rom_address = 0

    for line in lines:
        if line.startswith("(") and line.endswith(")"):
            labels[line[1:-1]] = rom_address
        else:
            rom_address += 1

    symbols = SYMBOLS.copy()
    symbols.update(labels)

    variable_address = 16
    machine_code = []

    for line in lines:
        if line.startswith("("):
            continue

        if line.startswith("@"):
            symbol = line[1:]

            if symbol.isdigit():
                address = int(symbol)
            else:
                if symbol not in symbols:
                    symbols[symbol] = variable_address
                    variable_address += 1
                address = symbols[symbol]

            machine_code.append(format(address, "016b"))

        else:
            dest = ""
            jump = ""
            comp = line

            if "=" in line:
                dest, comp = line.split("=")

            if ";" in comp:
                comp, jump = comp.split(";")

            code = "111" + COMP[comp] + DEST[dest] + JUMP[jump]
            machine_code.append(code)

    output_file = filename.replace(".asm", ".hack")

    with open(output_file, "w", encoding="utf-8") as f:
        f.write("\n".join(machine_code) + "\n")

    print("組譯完成！")
    print("輸出檔案：", output_file)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("使用方式：python assembler.py xxx.asm")
    else:
        assemble(sys.argv[1])
