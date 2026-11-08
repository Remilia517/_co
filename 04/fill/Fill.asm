// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Repeatedly paints the entire screen black while a key is pressed,
// and white while no key is pressed.

(LOOP)
    // Read the keyboard and choose the screen color.
    @KBD
    D=M
    @BLACK
    D;JNE

(WHITE)
    @COLOR
    M=0
    @PAINT
    0;JMP

(BLACK)
    @COLOR
    M=-1

(PAINT)
    // Start at SCREEN and paint all 8192 screen words.
    @SCREEN
    D=A
    @ADDRESS
    M=D

    @8192
    D=A
    @COUNT
    M=D

(PIXEL)
    @COLOR
    D=M
    @ADDRESS
    A=M
    M=D

    @ADDRESS
    M=M+1

    @COUNT
    MD=M-1
    @PIXEL
    D;JGT

    // Check the keyboard again so the screen follows key state.
    @LOOP
    0;JMP
