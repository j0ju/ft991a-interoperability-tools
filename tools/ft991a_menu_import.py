#!/usr/bin/env python3

# this should reflect 031
SPEED = 38400
# this should reflect setting no 032, not yet
WAIT  = 1000

# EX031 cannot be restored by CAT commands.
# EX087 cannot be changed.

import serial;
from sys import stdin as STDIN;

ser = serial.Serial('/dev/ttyUSB0', SPEED, timeout = float(WAIT)/float(SPEED) )

for line in STDIN:
  cmd = bytearray(line.strip())

  if cmd[0:1] == '#':
    # comment
    continue

  if cmd[0:2] != 'EX':
    print 'E: "%s" is not a menu settings command, ignoring' % ( cmd )
    continue

  ser.write(cmd + b';')

  while ser.out_waiting > 0:
    pass

  #print cmd + ';'

  rs = b'';
  rs = ser.read(2)
  if rs != '':
    print rs
    print 'E: error applying "%s", ignoring' % ( cmd )

