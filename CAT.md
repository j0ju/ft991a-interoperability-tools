# CAT commands

Here you can find the official docs for FT-991a CAT commands

 * [CAT manual - FT-991A_CAT_OM_ENG_1711-D.pdf](https://www.yaesu.com/downloadFile.cfm?FileID=13370&FileCatID=158&FileName=FT%2D991A%5FCAT%5FOM%5FENG%5F1711%2DD.pdf&FileContentType=application%2Fpdf)

## partly documented

 * MT
 * MW

This is not used by [ADMS991A from RT Systems](https://www.rtsystemsinc.com/ADMS-991A-Programming-Software-Only-for-the-Yaesu-FT-991FT-991A_p_92.html) for programming the FT-991/FT-991a.

## undocumented

### SPID

Those have been found in gossip used by [ADMS991A from RT Systems}](https://www.rtsystemsinc.com/ADMS-991A-Programming-Software-Only-for-the-Yaesu-FT-991FT-991A_p_92.html) while programming the FT-991/FT-991a.

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
