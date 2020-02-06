# tec-SPEECH
TEC-1 speech module using SP0256A-AL2 design by Craig Hart. 
PCB redesigned by Ben Grimmett

TE 15-26
## SPEECH MODULE CIRCUIT 
Since the dawn of time, Colin has been fascinated by electronic speech synthesis, so it was with immense joy that
we discovered the SP0256A-AL2 speech chip. This chip is a universal speech unit that can be made to speak almost any English word. The price was cheap and the interface was minimal, it was just too good to pass up! So I took took up the project and this is the result.
The module is interfaced to the TEC, and the TEC controls what is said. The only requirement is that you have a crystal oscillator, as the module requires a 3.58MHz clock signal from the unit. Demonstration programs have been included for testing and simple word sequencing, and these programs will show how the unit is accessed. This is the ideal companion project to go with the I/O board, and a robot created out of the two projects will cause a real stir if it speaks a comment in response to what it is sensing in its environment. The module is connected via an 8 way ribbon cable and 4 flying leads. The ribbon cable picks up D0-D5, and the 5v supply. The other 4 leads connect to STROBE 05, WAIT, RESET, and CLK. Note that only the lower six bits of the data bus are used by the speech chip. The reasons for this will be explained later. 

## OPERATION
The operation of the unit is straight forward, but it is important to understand its operation so that you can use it once you have built it. The SP0256AAL2 is made to speak by sending it a series of ALLOPHONES. An allophone is the smallest individual sound that the
unit can speak. Words and sentences are formed by outputting a series of allophones, one after the other. Each allophone is assigned a number and this number is loaded into the chip via the TEC data bus, then the ALD line is pulled low (by strobe line 05). The SPO now commences to speak the allophone and indicates so by pulling the WAIT line low, halting the TEC until the module is ready for more data. The BC557 is turned on hard by this and the LM386 amplifier is switched on. Sound is clocked out of the unit at a rate determined by the CLOCK line. For normal speech this is 3.58MHz. Sound is filtered by an R-C network, to make the sound more "human like" and amplified by the LM386. 

## PARTS LIST
All resistors 1/4W 5%
* 1 - 1k Brown Black Red
* 1 - 82k Grey Red Orange
* 1 - 10k trimpot.
* 1 - 47n greencap.
* 2 - 100n monoblock.
* 2 - 4u7 electrolytic.
* 1 - 10u electrolytic.
* 1 - 100u electrolytic.
* 1 - BC557 transistor.
* 1 - LM386 amplifier IC.
* 1 - SP0256A-AL2 Speech IC.
* 1 - 8 pin IC socket.
* 1 - 28 pin IC socket.
* 1 - 8 ohm speaker.
* 4 - PC pins.
* 4 - PC pin connectors.
* 1 - 20 cm length 14 way ribbon cable.
* 1 - 24 pin DIP header.
* 1 - 10 cm length 2mm heatshrink tubing. 
* 1- 'SPEECH MODULE' PC board. 

When speech output ceases, the wait line goes HIGH, and the TEC is able to continue processing. In doing so, the BC557 is switched off and thus the LM386's power supply is switched off. The reason for doing this is due to the high input impedance of the chip; it is prone to picking up stray noise. The most common noise source is the scanning of the LED displays! This results in an uncomfortable buzz when the unit is not speaking and by switching the power to the amplifier this has been eliminated. 

## THE ALLOPHONE SET
The SPO has little intelligence about what you want it to speak. You cannot simply feed it a word, and have it say the correct pronunciation in every case. (Although other chips do have this capability) Instead you, the programmer, must translate each word into the appropriate allophone(s) for that word. There are 64 individual allophones, and each sounds different. In these 64 allophones, there are 5 pauses of various lengths, corresponding to word and sentence breaks. By consulting the Allophone reference table you can look up what you think the right sequence is then play around with different pronunciations of the same basic letter, until you reach the best sounding word. It can be a tedious process, but many common words have been pie calculated and a list appears at the end of the article, along with the table of individual allophones. Take a sample word : ALARM. Sound out the word slowly, letter by letter. Now look for a matching sound in the list. Write down your guess and progress through the word. Where you have two or more choices, pick the allophone of the appropriate length. For alarm, I chose AA LL AR MM, or 18 2D 3B 10. Add a pause to the end and the terminating byte 04 FF. Plug the data into the test program at 0910 and run it. It sounds a little cut-off in the first 'a', so try a longer 'A' i.e. AX (OF) and try again. Enter OF at 0910 and run the program again. Sounds better now doesn't it! By following this method, you should be able to come up with any word within  a short space of time. Remember, the secret is to sound each letter and syllable out and then search for the best allophone of the group. The sample word provided gives you a context in which the allophone is used. This is useful when deciding between TT1 and TT2 etc. We also discovered that it was much easier to produce an understandable word if you used the slang way of saying it. The speech module always produces the same type of sound for any givenallophone, so if you stick to spelling only, then the words always come out very strange. If you use slang then you will find that the resulting word is much easier to understand. A perfect example of this came up when we first started work on the project. We bought our first sample chip from Tandy. It came with a list of words and full specification data. When the project was working, we started trying some given examples, and although the examples were recognizable, they were not very clear. Then Ross said to try the slang pronunciation. Voila! perfect. The words which were before just average became clearer and much more recognizable. 

![](https://github.com/SteveJustin1963/tec-SPEECH/blob/master/dia-1.png)

## PAUSES AND REPEATING ALLOPHONES
The five pauses are worthy of a separate mention. You must always pause after a word, to make the SPO stop talking. Use a PA1 or a PA2. Use PA3 or PA4 between sentances. Refer to the following table for when to use PA1, PA2, and PA3 DURING words. PA1 Before BB, DD, GG and JH. PA2 Before some BB, DD, GG and JH. PA3 before PP, TT, KK, and CH.  A repeating allophone is one which can be spoken twice and flow along. i.e. EY EY produces 'AY pause AY', while FF FF produces one long 'Ffff'. Only 10 of these 64 allophones are repeatable like this. They are: IH EH AE UH AO AX AA FF TH & SS. Use these allophones in preferance to long timed syllables like SH in SHirt, WE in tWEnty, or SH in leaSH. 

## CONSTRUCTION
Although a simple project, care should be taken to ensure that a good job is done, so do not rush. Lay all the parts out in front of you on a piece of paper or cardboard (Not the High - Low shagpile of the living room!) and check to see that you have been supplied with everything. Begin by inserting the resistors. Solder them in and cut their leads short. Next insert the Capacitors, observing polarity with the Electrolytics. Insert and solder the trimpot, then finally the transistor. Turn the trimpot fully towards the SPO - this is full volume and should be set here until testing is complete. Check to see that you have a BC557 and insert it according to the 'D' on the overlay. Lastly insert the two IC sockets and plug the chips in, being careful to orientate pin one with the mark on the PC and avoid touching the pins of the SP0256A. 

![](https://github.com/SteveJustin1963/tec-SPEECH/blob/master/dia-2.png)
![](https://github.com/SteveJustin1963/tec-SPEECH/blob/master/dia-3.png)

