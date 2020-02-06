# tec-SPEECH
TEC-1 speech module using SP0256A-AL2 design by Craig Hart. 
PCB redesigned by Ben Grimmett

TE 15-26
## SPEECH MODULE CIRCUIT 

![](https://github.com/SteveJustin1963/tec-SPEECH/blob/master/dia-0.png)

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
The five pauses are worthy of a separate mention. You must always pause after a word, to make the SPO stop talking. Use a PA1 or a PA2. Use PA3 or PA4 between sentances. Refer to the following table for when to use PA1, PA2, and PA3 DURING words. PA1 Before BB, DD, GG and JH. PA2 Before some BB, DD, GG and JH. PA3 before PP, TT, KK, and CH.  
A repeating allophone is one which can be spoken twice and flow along. i.e. EY EY produces 'AY pause AY', while FF FF produces one long 'Ffff'. Only 10 of these 64 allophones are repeatable like this. They are: IH EH AE UH AO AX AA FF TH & SS. Use these allophones in preferance to long timed syllables like SH in SHirt, WE in tWEnty, or SH in leaSH. 

## CONSTRUCTION
Although a simple project, care should be taken to ensure that a good job is done, so do not rush. Lay all the parts out in front of you on a piece of paper or cardboard (Not the High - Low shagpile of the living room!) and check to see that you have been supplied with everything. Begin by inserting the resistors. Solder them in and cut their leads short. Next insert the Capacitors, observing polarity with the Electrolytics. Insert and solder the trimpot, then finally the transistor. Turn the trimpot fully towards the SPO - this is full volume and should be set here until testing is complete. Check to see that you have a BC557 and insert it according to the 'D' on the overlay. Lastly insert the two IC sockets and plug the chips in, being careful to orientate pin one with the mark on the PC and avoid touching the pins of the SP0256A. 

![](https://github.com/SteveJustin1963/tec-SPEECH/blob/master/dia-2.png)
![](https://github.com/SteveJustin1963/tec-SPEECH/blob/master/dia-3.png)
![](https://github.com/SteveJustin1963/tec-SPEECH/blob/master/dia-4.png)

Strip 6 wires from the ribbon cable, then connect the remaining 8 between the data lines and the DIP header. Connect power with the last two strands. Follow the diagram and you can't go wrong. Separate 4 of the remaining wires into individual lengths and solder into the 4 remaining holes on the module. Attach a matrix pin connector to the other end of each wire for connection to the TEC. Heatshrink each connector with the tubing supplied. A note on heatshrinking• Don't skip this section because you think it's a waste of time or too hard to do. Heatshrinking the connectors strengthens them and the wire is much less likely to break off. If you always melt the wire when shrinking over a candle, then try using the BARREL not the tip of your soldering iron. This gives you a better controlled heat source and a neat job can be done onthose small connections. The last two lengths of wire connect to the speaker. Wire these up and the board is complete. Now for connection to the TEC. You will need to have your crystal oscillator inserted. If you do not currently own a crystal oscillator, you must purchase one with a 3.58MHz crystal. If you haVe a different frequency crystal fitted, it must be around 3.2 - 4.0MHz otherwise the sound will be too high or low pitched. A 2MHz or 8MHz crystal will not suffice. Insert a PC pin in port 5 pad, a second pin in the board for the WAIT line, and a third pin in the board for the RESET line. Most users will already have done so, but if not, see the wiring diagram for the three pin locations. The other pin you will have to connect as best you can. To tap the 3.5MHz signal, DO NOT connect to pin 6 of the Z80. This is because the crystal's frequency is divided by two before reaching the TEC board. Instead, solder a PC pin onto pin 8 of the 74LSO4 on the crystal oscillator PC. This is the 3.5MHz clock output. 

## TESTING
Plug everything together and power up. If your TEC locks up or the unit makes strange sounds, remove power and go to the section on troubleshooting. Your TEC should start up as normal, with the unit deadly quiet. Enter the TEST PROGRAM and you should be greeted with a message. Listen carefully and let your hearing adjust to the metallic pitch. If all you can hear is junk, check your program, then if still no go, proceed to the troubleshooting section. If the test program produces recognisable output, try the other examples and then try making up a few words of your own. You will soon find that you can say just about any word, once you get the right allophones. There can be hours of fun even getting it to correctly pronounce your name. "Paul" is easy enough, but what about "Vouzopolous"? or even common words like "construction" and "calculator"? With such a versatile unit, the sky's the limit. 

## IF IT DOESN'T WORK
If your speech unit does not work, DON'T PANIC. Firstly, check your wiring. Most errors are in wiring, causing the TEC to lock up. Look for obvious faults like shorts, dry joints, components of wrong value or orientation. Check that your chips are inserted correctly - pin one of each chip faces AWAY from the off-board wires. If you bought your parts from all over the place, make sure you get a SP0256A-AL2 device. Other suffix numbers are not acceptable. Check that the trimpot is turned all the way towards the SP0256A - full volume. You can temporarily short between the collector and the emitter of the BC557, to turn the amplifier on fully. This should produce a lot of hiss, and touching pin 3 of the LM386 should produce a buzzing sound. Check that you have +5v on each chip, and that the SPO's reset pin (pins 2 and 25) are normally HIGH, and that they follow the reset pin of the Z80 (pin 26). If all you get is garbage then you probably have the data lines wired around the wrong way. Check against the wiring diagram, and have a friend check it as well. Look for pins bent up under the SPO and not connecting with  the IC socket. Check the program through and make sure that you are sending it the correct data. If you are totally lost, give us a call. Sometimes we can solve a problem straight away, and most times within a few minutes. If all else fails, we offer a repair service. Costs are: Basic repair $ 7.00 SP0256A replacement $15.00 Postage $ 3.00 If your SP0256A-AL2 is damaged, you will be charged extra due to its high replacement cost. 

## MODIFICATIONS
If you don't intend to fit a crystal oscillator to your TEC, you can put a crystal on the speech board. Simply fit the crystal across pins 27 and 28 of the SP0256A. Then fit a 2'7p between pin 27 and ground, and a 27p between pin 28 and ground. This enables the SPO's internal oscillator. We did not include this on the basic board because we wanted to keep the price as low as possible, in order to counter balance the cost of the SP0256A. We reasoned that most people will change over to JMON, therefore purchasing a crystal oscillator anyway. If you find that you are using long silent periods between words, you may find that you can hear an annoying click from the speaker as the LM386 gets switched. This is because the 10u capacitor is too low in value. Increase this capacitor to 22u or 47u and the problem should go away. If you need to make the output louder, change the 4u7 between pins 1 and 8 of the LM386 to 10u. This increases the gain of the LM386 to 200.  

## ALLOPHONE REFERENCE TABLE 
NUMBER ALLOPHONE DURATION SAMPLE

> 00 PA1 10 ms PAUSE
> 01 PA2 30 ms PAUSE
02 PA3 50 ms PAUSE
03 PA4 100 ms PAUSE
04 PM 200 ms PAUSE
05 OY 420 ms Boy
06 AY 260 ms Sky
07 EH* 70 ms End
08 KK3 120 ms Comb
09 PP 210 ms Pow
OA JH 140 ms Dodge
OB NN1 140 ms Thin
OC IH* 70 ms Sit
OD TT2 140 ms To
OE RR1 170 ms Rural
OF AX* 70 ms Succeed
10 MM 180 ms Milk
11 TT1 100 ms Part
12 DHI 290 ms They
13 IY 250 ms See
14 EY 280 ms Beige
15 DD1 70 ms Could
16 UW1 100 ms To
17 AO* 100 ms Aught
18 AA* 100 ms Hot
19 YY2 180 ms Yes
IA AE 120 ms Hat
1B 111-11 130 ms He
1C BBI 80 ms Business
ID TH* 180 ms Thin
lE UH* 100 ms Book
1F UW2 260 ms Food
20 AW 370 ms Out
21 DD2. 160 ms Do
22 GG3 140 ms Wig
23 VV 190 ms Vest
24 GG1 80 ms Got
25 SH 160 ms Ship
26 71-1 190 ms Azure
27 RR2 120 ms Brain
28 FF* 150 ms Food
29 KK2 190 ms Sky
2A KK1 160 ms Can't
2B ZZ 210 ms Zoo
2C NG 220 ms Anchor
2D LL 110 ms Lake
2E WW 180 ms Wool
2F XR 360 ms Repair
30 WH 200 ms Whig
31 YY1 130 ms Yes
32 CH 190 ms Church
33 ER1 160 ms Fir
34 ER2 300 ms Fir
35 OW 240 ms Beau
36 DH2 240 ms They
37 SS* 90 ms Vest
38 NN2 190 ms No
39 HH2 180 ms Hoe 
