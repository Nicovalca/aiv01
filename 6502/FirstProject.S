.org $8000
.define player_pos $01
.define player_col $02

init:    
    LDA #$E7
    STA player_pos
    LDA #$07
    STA player_col
    JSR drawship   
    LDA #$00 
    JMP loop
    
loop:
    JSR input
    JSR wait_abit
    JMP loop

drawship:    
    LDA player_col    ; drawing head of the ship
    LDX player_pos
    STA $0200,X  
    TXA
    ADC #$10
    TAX   
    LDA player_col    ; drawing body of the ship
    STA $0200,X
    INX
    STA $0200,X
    DEX
    DEX
    STA $0200,X
    RTS

input:
    LDA $4000
    AND #$08
    BNE on_right_move

    LDA $4000
    AND #$04
    BNE on_left_move
    RTS

block_move:
    CLC
    RTS

on_right_move:
    LDA player_pos        
    ADC #$12           
    BCS block_move      
    INC player_pos       
    JSR clear_screen
    JSR drawship    
    RTS

on_left_move:
    LDA player_pos    
    TAX
    DEX
    DEX
    BCS block_move     
    DEC player_pos         
    JSR clear_screen   
    JSR drawship    
    RTS

clear_screen:    
    LDX #$00    
    JSR clear_loop
    RTS

clear_loop:        
    LDA #$00
    STA $0200,X
    INX
    BEQ block_move
    JMP clear_loop

wait_abit:
    LDA #$00
    INX
    BEQ block_move
    JMP wait_abit

interrupt:     
    RTI  

nonmaskable: 
    RTI

.goto $FFFA
.dw nonmaskable
.dw init
.dw interrupt