// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// R0 and R1 are non-negative values. R0 and R1 are preserved.

    @R2
    M=0
    @R1
    D=M
    @R13
    M=D

(LOOP)
    @R13
    D=M
    @END
    D;JEQ

    @R0
    D=M
    @R2
    M=D+M

    @R13
    M=M-1
    @LOOP
    0;JMP

(END)
    @END
    0;JMP
