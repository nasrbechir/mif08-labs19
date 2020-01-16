PACKAGE = MiniC
MAINFILE = Main
#change with your own name:
MYNAME = JohnDoe
DIR = $(shell basename $(PWD))
PYTEST_OPTS = 

TESTFILE?=ex/test00.c

ifndef ANTLR4
abort:
	$(error variable ANTLR4 is not set)
endif

all: run

MiniCLexer.py MiniCParser.py: $(PACKAGE).g4
	$(ANTLR4) $< -Dlanguage=Python3 -visitor -no-listener

main-deps: MiniCLexer.py MiniCParser.py MiniCInterpretVisitor.py MiniCTypingVisitor.py

run: $(MAINFILE).py main-deps
	python3  $< $(TESTFILE)

# tests all files in ex/test*.c
tests: test_interpreter.py main-deps
	python3 -m pytest $(PYTEST_OPTS) -v --failed-first $< \
	        --cov=$(PWD) --cov-report=term --cov-report=html 

tar: clean
	cd ..; tar cvfz $(DIR)-$(MYNAME).tgz $(DIR) --transform 's/$(DIR)/$(DIR)-$(MYNAME)/'
	@echo "Created ../$(DIR)-$(MYNAME).tgz"

clean:
	rm -rf *~ $(PACKAGE)Parser.py $(PACKAGE)Lexer.py $(PACKAGE)Visitor.py *.pyc *.tokens  __pycache* ex/*~ .cache* ex-types/*~ *.interp *.diff log*.txt
