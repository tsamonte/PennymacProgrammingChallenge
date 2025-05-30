VENV = venv

# Generated venv will have a different structure depending on the operating system
# Windows (checks if environment variable that only exists in Windows is present)
ifdef OS
	BIN = $(VENV)/Scripts
	RM = rmdir /s /q
# Linux
else
	ifeq ($(shell uname), Linux)
		BIN = $(VENV)/bin
		RM = rm -rf
	endif
endif

PYTHON = $(BIN)/python
ACTIVATE = $(BIN)/activate

$(ACTIVATE):
	python -m venv $(VENV)

run: $(ACTIVATE)
	$(PYTHON) src/main.py

run-alt: $(ACTIVATE)
	$(PYTHON) src/main.py alt

clean:
	$(RM) $(VENV)

all: $(ACTIVATE) run clean