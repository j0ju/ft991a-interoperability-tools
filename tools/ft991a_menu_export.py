#!/usr/bin/env python3

import serial;

ser = serial.Serial('/dev/ttyUSB0', 38400)

for k in range(1,154):
  cmd = b'EX%03i;' % (k)

  if k in (31, 87):
    continue

  ser.write(cmd)
  rs = b''
  ch = b''
  while ch != ';':
    rs = rs + ch
    ch = ser.read()

  print rs;
