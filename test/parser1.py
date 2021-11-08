import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--foo', action='store_true')
parser.add_argument('bar')

opt = parser.parse_known_args(['--foo', '--badger', 'BAR', 'spam'])
print(opt)

# opt2 = parser.parse_args(['--foo', '--badger', 'BAR', 'spam'])
opt2 = parser.parse_args(['--foo', 'BAR2'])
print(opt2)
