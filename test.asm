.org  0900h       
      LD HL,0910  ;HL = Points to start of table
      LD A,(HL)   ;Get next Allophone
      CP FF       ;End of table ?
      JR Z,090D   ;Yes, HALT
      OUT (05),A  ;Speak allophone
      INC HL      ;Next allophone
      JR,0903     ;Say next...
      HALT        ;EOT, stop until key pressed
      JR,0900     ;Key pressed, say again
                  ;Your allophones are entered from 0910 onwards
                  ;
                  ;this says 'TALKING COMPUTER'
                  ;0910 OD 17 17 02 2A OC 2C 04
                  ;0918 04 2A OF 10 00 31 16 OD
                  ;0920 33 04 04 FF
                  ;
                  ;Here is another greeting message. The TEC introduces itself here!
                  ;0910 1B 07 2D 35 00 36 07 2F
                  ;0918 04 06 00 1A 10 00 12 13
                  ;0920 00 OD 13 03 13 03 37 13
                  ;0928 03 08 18 10 09 31 16 11
                  ;0930 33 04 04 04 38 20 00 30
                  ;0938 OC 1D37 09 13 32 04 FF
                  ;
                  ;
                  
