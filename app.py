import argparse

parser = argparse.ArgumentParser()
parser.add_argument('huhu')
parser.add_argument('hoho')

args = parser.parse_args()
huhu = args.huhu
hoho = args.hoho

print(huhu, hoho, flush=True)
