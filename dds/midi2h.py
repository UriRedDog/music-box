import midi

m = midi.MidiFile()
m.open( 'IWantADog.mid' )
m.read()
m.close()

data = []
lowest = 255
highest = 0
for line in str( m ).split( '\n' ):
    if 'NOTE_ON' in line:
        fields = line.split( ', ' )
        time = fields[ 1 ][ 2 : ].zfill( 5 ) # To get numerical sorting.  Otherwise it would be lexical.
        pitch = int( fields[ 4 ][ 6 : ] ) + 12 # Shift one octave up.
        data.append( '%s %s' % ( time, pitch ) )
        if pitch < lowest:
            lowest = pitch
        if pitch > highest:
            highest = pitch
data.sort()

print 'Events:', len( data )
print 'Pitch range:', lowest, highest
for entry in data:
    time, pitch = entry.split()
    print '    %s, %s,' % ( int( time ), int( pitch ) ) # Get rid of silly octal notation.
