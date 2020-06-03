all:
	g++ client.cpp -g -o client.exe -pthread -std=c++11
	g++ server.cpp -g -o server.exe -pthread -std=c++11

s:
	./server.exe

c:
	./client.exe

clean:
	rm *.exe