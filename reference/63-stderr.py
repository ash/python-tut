import sys

print('printing to STDOUT')
print('print to file STDERR', file=sys.stderr)
sys.stderr.write('via write to STDERR\n')
