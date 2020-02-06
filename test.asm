.org  0900h
      LD HL,0910
      LD A,(HL)
      CP FF
      JR Z,090D
      OUT (05),A
      INC HL
      JR,0903
      HALT
      JR,0900

