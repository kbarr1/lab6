
from songfile import Song

import timeit

def readfile(filename):

	with open (filename, encoding="utf-8") as file:

		my_dict = {}
		lista = []
		ok = 0
		for line in file:
			line = line.split('<SEP>')
			song = Song(line[0], line[1], line[2], line[3].strip() )
		
			lista.append(song)

			my_dict[line[2]] = []
			my_dict[line[2]].append(line[0])
			my_dict[line[2]].append(line[1])
			my_dict[line[2]].append(line[3])

			ok = ok+1
			if ok == 100:
				return lista, my_dict
	return lista, my_dict






def linsok(listan, nyckel): # kod från frl 3
	for x in listan:
		if x.artist == nyckel:
			return True
	return False

def binsok(listan, nyckel): # kod från frl 3
	v = 0
	h = len(listan) - 1
	found = False

	while v <= h and not found:
		mitten = (v + h) //2 
		x = listan[mitten]
		if x.artist == nyckel:
			found = True
		else:
			if nyckel < x.artist:
				h = mitten -1
			else:
				v = mitten + 1
	return found

def bubblesort(listan): # kod från kursbok
	print("hello")
	x = len(listan) - 1
	hej = 0
	for element in range(x, 0, -1): # hur många element i listan
		for i in range(element): # för varje element i listan av element

			if listan[i+1] < listan[i]: # objekt och < kallart på __lt__
				temp = listan[i]
				listan[i] = listan[i+1]
				listan[i+1] = temp
		print(hej)
		hej = hej + 1

def quicksort(data):
	sista = len(data) - 1
	qsort(data, 0, sista)

def qsort(data, i, j):
	pivotindex = (i+j)//2
	data[pivotindex], data[j] = data[j], data[pivotindex]
	k = partitionera(data, i-1, j, data[j])
	data[k], data[j] = data[j], data[k]
	if k-i > 1:
		qsort(data, i, k-1)
	if j-k > 1:
		qsort(data, k+1, j)

def partitionera(data, v, h, pivot):
	while True:
		v = v + 1
		while data[v] < pivot:
			v = v + 1
		h = h - 1
		while h != 0 and data[h] > pivot:
			h = h - 1
		data[v], data[h] = data[h], data[v]
		if v >= h: 
			break
	data[v], data[h] = data[h], data[v]
	return v






def main():

	filename = "unique_tracks.txt"

	lista, dictionary = readfile(filename)

	print(lista[1])
	print(dictionary["Joseph Locke"])
    
	n = len(lista)
	print("Antal element =", n)

	sista = lista[n-1]
	testartist = sista.artist

	linjtid = timeit.timeit(stmt = lambda: linsok(lista, testartist), number = 10000)
	print("Linjärsökningen tog", round(linjtid, 4) , "sekunder")

	bintid = timeit.timeit( stmt = lambda: binsok(lista, testartist), number = 10000)
	print("Binärsökningen tog", round(bintid, 4) , "sekunder")

	print([hej.artist for hej in lista])

	quicktid = timeit.timeit( stmt = lambda: quicksort(lista), number = 10000)
	print("Quicksorten tog", round(quicktid, 4) , "sekunder")

	print([hej.artist for hej in lista])



main()


