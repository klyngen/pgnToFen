import pgntofen

converter = pgntofen.PgnToFen()
file = "./test/Carlsen.pgn"

stats = converter.pgnFile(file)

output = open("fenstring.txt", "w")

for fen in (stats['succeeded'][0][1]):
    output.write(fen)
    output.write('\n')

output.close()


