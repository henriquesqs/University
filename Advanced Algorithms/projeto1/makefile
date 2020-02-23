all: progCompressor
progCompressor: compressor.o huffTree.o util.o
	g++ -g -o prog compressor.o huffTree.o util.o
compressor.o: compressor.cpp huffTree.hpp
	g++ -g -o compressor.o compressor.cpp -c
huffTree.o: huffTree.cpp huffTree.hpp
	g++ -g -o huffTree.o huffTree.cpp -c
util.o: util.cpp util.hpp
	g++ -g -o util.o util.cpp -c
clean:
	rm -rf *.o
run:
	./prog