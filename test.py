import pgntofen

converter = pgntofen.PgnToFen()
file = "./test/Carlsen.pgn"

stats = converter.pgnFile(file)

output = open("fenstring.txt", "w")

#for fen in (stats['succeeded'][0][1]):
#    output.write(fen)
#    output.write('\n')


items = stats['succeeded'][0][1]

for x in range(0, len(items), 3):
    output.write(items[x]);
    output.write('\n')

output.close()


