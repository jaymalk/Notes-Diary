

decrypt:
	openssl des -d -in .cp/indexing.h.enc -out .cp/indexing.h -pass pass:$(key)
	openssl des -d -in .cp/read_write.h.enc -out .cp/read_write.h -pass pass:$(key)
	openssl des -d -in .cp/main.cpp.enc -out .cp/main.cpp -pass pass:$(key)
	openssl des -d -in .cp/search.h.enc -out .cp/search.h -pass pass:$(key)

encrypt:
	openssl des -out .cp/indexing.h.enc -in .cp/indexing.h -pass pass:$(key)
	rm -f .cp/indexing.h
	openssl des -out .cp/read_write.h.enc -in .cp/read_write.h -pass pass:$(key)
	rm -f .cp/read_write.h
	openssl des -out .cp/main.cpp.enc -in .cp/main.cpp -pass pass:$(key)
	rm -f .cp/main.cpp
	openssl des -out .cp/search.h.enc -in .cp/search.h -pass pass:$(key)
	rm -f .cp/search.h
