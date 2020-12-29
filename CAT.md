# CAT commands

Here you can find the official docs for FT-991a CAT commands

 * [CAT manual - FT-991A_CAT_OM_ENG_1711-D.pdf](https://www.yaesu.com/downloadFile.cfm?FileID=13370&FileCatID=158&FileName=FT%2D991A%5FCAT%5FOM%5FENG%5F1711%2DD.pdf&FileContentType=application%2Fpdf)
 * [Feature request at Chirp](https://chirp.danplanet.com/issues/2531)
 * [Channels defined in flrig](https://sourceforge.net/p/fldigi/flrig/ci/master/tree/src/rigs/FT991A.cxx)

## partly documented

 * MT
 * MW

Both CMDs can be used to read and write memory channels.
The answer to th read command does not fit the description in the CAT Manual. It cannot be replayed without modification.

... tbd ...

You cannot set the RX/TX shift for repeaters, if it is different to the defined shift for the band.
eg. if you define 7.6 Mhz for 70cm but you are using a repeater with 9.4Mhz shift, it cannot be set this way.
ADMS991A can do this.
Q: but how ?

This is not used by [ADMS991A](https://www.rtsystemsinc.com/ADMS-991A-Programming-Software-Only-for-the-Yaesu-FT-991FT-991A_p_92.html) for programming the FT-991/FT-991a although it is the official documented way.

## undocumented

### SPID

Those have been found in gossip used by [ADMS991A](https://www.rtsystemsinc.com/ADMS-991A-Programming-Software-Only-for-the-Yaesu-FT-991FT-991A_p_92.html) while programming the FT-991/FT-991a.

This allows setting the ID (EX087) of the device. This cannot be set via `EX087_____;`

`SPID;` reads out the ID.
Setting of the Radio ID of the TRX is possible by `SPID12345;`. This is used by the GM and Wires-X functions in C4FM mode.

Response is `A;` for ACK when ok.

### SPR

It looks like we can read from memory regions of the MCU.

tbd

Response is `A;` for ACK when ok.

### SPW

It looks like we can write to memory regions of the MCU.

Response is `A;` for ACK when ok.
