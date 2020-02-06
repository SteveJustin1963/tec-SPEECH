# tec-SPEECH
TEC-1 speech module using SP0256A-AL2 design by Craig Hart. 

PCB redesigned by Ben Grimmett

# SPEECH MODULE CIRCUIT 
Since the dawn of time, Colin has been
fascinated by electronic speech synthesis, so it was with immense joy that
we discovered the SP0256A-AL2
speech chip. This chip is a universal
speech unit that can be made to speak
almost any English word. The price was
cheap and the interface was minimal, it
was just too good to pass up! So I took
took up the project and this is the result.
The module is interfaced to the TEC,
and the TEC controls what is said. The
only requirement is that you have a crystal oscillator, as the module requires a
3.58MHz clock signal from the unit.
Demonstration programs have been included for testing and simple word sequencing, and these programs will show
how the unit is accessed.
This is the ideal companion project to
go with the I/O board, and a robot
created out of the two projects will
cause a real stir if it speaks a comment
in response to what it is sensing in its
environment.
The module is connected via an 8 way
ribbon cable and 4 flying leads. The
ribbon cable picks up D0-D5, and the 5v
supply. The other 4 leads connect to
STROBE 05, WAIT, RESET, and CLK.
Note that only the lower six bits of the
data bus are used by the speech chip.

