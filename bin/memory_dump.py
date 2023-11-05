#!/usr/bin/env python3

import serial;

ser = serial.Serial('/dev/ttyUSB0', 38400)

for k in range(0,128):
  cmd = b'SPR' + b''.join(map( chr, [ 00, 00, k ])) + ';'
  print cmd;

  ser.write(cmd)
  rs = ser.read(8)

  print ord(rs[3])
  print ord(rs[4])
  print ord(rs[5])
