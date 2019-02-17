make:
	@openssl des -d -in .ifl/cp -out core.py -pass pass:$(key)
	@python3 core.py
	@rm -f core.py

compile:
	@g++ .cp/main.cpp
	@openssl des -in a.out -out .ifl/cf -pass pass:$(key)
	@rm -f a.out

decrypt:
	@openssl des -d -in .cp/indexing.h.enc -out .cp/indexing.h -pass pass:$(key)
	@openssl des -d -in .cp/read_write.h.enc -out .cp/read_write.h -pass pass:$(key)
	@openssl des -d -in .cp/main.cpp.enc -out .cp/main.cpp -pass pass:$(key)
	@openssl des -d -in .cp/search.h.enc -out .cp/search.h -pass pass:$(key)
	@openssl des -d -in .ifl/cp -out core.py -pass pass:$(key)

encrypt:
	@openssl des -out .cp/indexing.h.enc -in .cp/indexing.h -pass pass:$(key)
	@openssl des -out .cp/read_write.h.enc -in .cp/read_write.h -pass pass:$(key)
	@openssl des -out .cp/main.cpp.enc -in .cp/main.cpp -pass pass:$(key)
	@openssl des -out .cp/search.h.enc -in .cp/search.h -pass pass:$(key)
	@openssl des -out .ifl/cp -in core.py -pass pass:$(key)
	@rm -f .cp/indexing.h
	@rm -f .cp/read_write.h
	@rm -f .cp/main.cpp
	@rm -f .cp/search.h
	@rm -f core.py
