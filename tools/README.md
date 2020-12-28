# Tools

The helpers below expect
 * the TRX to be connected to `/dev/ttyUSB0`.
 * `pyserial` is installed.

## `ft991a_menu_export.py`

This dumps the settings from the _menu setup_ to STDOUT.
It expects the TRX to be connected to `/dev/ttyUSB0`.

### Example

```
python ft991a_menu_export.py > dump.ft991a
```

This [file](DO1JJB.defaults.ft991a) contains a dump of DO1JJBs config, stripped by some creds.

## `ft991a_menu_import.py`

This executes all CAT commands prefixed with EX, so this can be used to restore the settings from `ft991a_menu_export.py`.

Hint: This can be used to set also only parts of the TRX config, for changing from CW to telephony to DigiModes and vice versa.
Just put the changed EX commands in a file and feed it with this tool to the TRX.

### Example

```
python ft991a_menu_import < dump.ft991a
```

### Limitations

It cannot restore EX031, the speed of the CAT interface. This is rejected by at least FW 2.04.
(It also would high likely break the CAT stream via serial when changing the speed while configuring.)

It cannot set EX087 as this a read only command. See [CAT commands](../CAT.md).

