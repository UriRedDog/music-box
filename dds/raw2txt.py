import struct

f = open( 'attack.raw', 'rb' ); cont = f.read(); f.close()

i = 0
for value in cont:
    print '%s,' % struct.unpack( 'b', value )[ 0 ],
    i += 1
    if i % 16 == 0:
        print
