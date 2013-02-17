A series of scripts useful for the parsing and altering of
driving script data, assuming it comes in the form of
"^([0-9\.]+?)([ \t]+)([0-9\.]+?)(\n)$"
The first regex group should be the time in seconds
The second regex group should be the speed in either kph or mph
with a note at the start of the file such as //mph or //kph to specify.
Additional functionalities may be added later.
