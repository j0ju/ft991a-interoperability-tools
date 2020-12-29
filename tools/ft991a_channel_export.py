#!/usr/bin/env python3

import serial;

ser = serial.Serial('/dev/ttyUSB0', 38400)

# 60m channels and VFO
channel_list = [
  b'VFO',
  b'U50',
  b'U51',
  b'U52',
  b'U53',
  b'U54',
  b'U55',
  b'U56',
  b'U57',
  b'U58',
  b'U59',
  b'U60',
]

# combine those with a random guess
for k in range(0,150):
  channel_list.append(b'%03i' % k)


# read out channels
for k in channel_list:
  cmd = b'MT%s;' % (k)

  ser.write(cmd)
  rs = b''
  ch = b''
  while ch != ';':
    rs = rs + ch
    ch = ser.read()

  if rs == "?":
    continue

  print b'%s: %s' % (k, rs[5:])
