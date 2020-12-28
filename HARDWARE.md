# Hardware documentation dump

## MCU/CPU

From the header of the [firmware updating tool](https://www.yaesu.com/downloadFile.cfm?FileID=16503&FileCatID=42&FileName=FT%2D991A%5FFirmware%5Fupdate%5F202006.zip&FileContentType=application%2Fx%2Dzip%2Dcompressed)
it looks like a R5F61653RN50FPV CPU from Renesas.
Unfortunatly as of the time writing the datasheet is not found on the Renesas webpage [alternative location](https://pdf1.alldatasheet.com/datasheet-pdf/view/249700/RENESAS/R5F61653RN50FPV.html)

```
; ******************************************
; ** [FILENAME]     AH067_V0204.SFL       **
; ** [DATE]         2020/03/04            **
; ** [CPU]          R5F61653RN50FPV       **
; ** [PRODUCT NAME] FT-991A               **
; ** [FIRM Version] V0204                 **
; ** [R code]       YR                    **
; ** [CHECK SUM]    03702228(00000-5FFFF) **
; ******************************************
```

The MCU datasheet tells us the the MCU has 4 operating modes. (starting from page 27)
 * normal mode (max 64kb overall)
 * middle mode (64kb program area, 16MB data area)
 * advanced mode (16MB program aread, 4GB data)
 * maximum mode (program area, data area 4GB)

Q: which is is used in the FT991a?
Guess: Advanced mode, as
 * the firmware header looks like 24bit addressing and
 * the `SPRabc;` CAT command seems to expect 24bit in abc.

Q: How about segmentation?
Guess: flat

Starting on page 33 the startup of the MCU is described.

## Memory layout

... to be done ...

Guess: Flash memory located at 0x000000, at least 6MB large. And we need an entrypoint vector in 0x000000, according to the boot up.

Q: Where is some RAM located?

