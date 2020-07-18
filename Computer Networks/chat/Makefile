all:
	g++ -g -c classChannel.cpp
	g++ -g -c serverMultithread.cpp
	g++ -g -o server.exe classChannel.o serverMultithread.o -lpthread -std=c++11
	g++ -g clientMultithread.cpp -o client.exe -pthread -std=c++11
	rm *.o

s:
	./server.exe

c:
	./client.exe

clean:
	rm *.exe *.o