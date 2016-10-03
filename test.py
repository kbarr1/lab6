
from songfile import Song

with open ("unique_tracks.txt", encoding="utf-8") as file:
	my_dict = {}
	lista = []
	for line in file:
		line = line.split('<SEP>')
		song = Song(line[0], line[1], line[2], line[3] )
		
		lista.append(song)

		my_dict[line[2]] = []
		my_dict[line[2]].append(line[0])
		my_dict[line[2]].append(line[1])
		my_dict[line[2]].append(line[3])



#lat1 = lista[0]
#print(lat1)
print(lista[1])
print(my_dict["Joseph Locke"])