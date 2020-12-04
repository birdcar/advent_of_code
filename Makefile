# .PHONY defines parts of the makefile that are not dependant on any specific file
# This is most often used to store functions
.PHONY = help test

# Defines the default target that `make` will to try to make, or in the case of a phony target, execute the specified commands
# This target is executed whenever we just type `make`
.DEFAULT_GOAL = help

# The @ makes sure that the command itself isn't echoed in the terminal
help:
	@echo "---------ADVENT OF CODE 2020---------"
	@echo ""
	@echo "To check your answers, run 'make test'"
	@echo ""
	@echo "-------------------------------------"

test:
	@python -m unittest --verbose

deps:
	pip-compile --output-file=requirements.txt requirements.in

setup:
	python -m venv .venv
	pip install -r requirements.txt
