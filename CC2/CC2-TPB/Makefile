MAINFILE = sujetB
PACKAGE = SujetB
MYNAME = JohnDoe

ifndef ANTLR4
$(error variable ANTLR4 is not set)
endif

$(PACKAGE)Listener.py $(PACKAGE)Lexer.py $(PACKAGE)Lexer.tokens $(PACKAGE)Parser.py $(PACKAGE).tokens: $(PACKAGE).g4
	$(ANTLR4) $< -Dlanguage=Python3

main-deps: $(PACKAGE)Lexer.py $(PACKAGE)Parser.py

#use pytest !!

run: $(MAINFILE).py main-deps
	python3 $< --verbose

TESTFILE=testfiles/ex0.txt

tests: test_grammar.py main-deps
	python3 -m pytest -v $< 


tar: clean
	cd ..; tar cvfz $(MYNAME)-CC2.tgz CC2-ex/ --transform 's/CC2-ex/$(MYNAME)-CC2/'


clean:
	rm -rf *~ $(PACKAGE)*.py $(PACKAGE)*.pyc *.tokens  __pycache* .cache *.interp .pytest_cache/ testfiles/*~  
