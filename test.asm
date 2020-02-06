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

