python = $(shell type -p python3 || echo python)

test:
	python3 -m unittest
