all: test

test:
	python3 -m doctest findpassword.py

clean:
	rm -rf __pycache__