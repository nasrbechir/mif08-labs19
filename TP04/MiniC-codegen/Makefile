PACKAGE = MiniC
DIR = $(shell basename $(PWD))
MAINFILE = Main
TESTFILE?=tests/step1/test00.c
ASM=$(TESTFILE:%.c=%.s)
OBJ=$(TESTFILE:%.c=%.riscv)
TRACE=$(TESTFILE:%.c=%.trace)
SIMU = spike pk
ASSEMBLER=riscv64-unknown-elf-gcc
MYNAME=AlanTuring
# To change the allocation strategy, use e.g.:
# make ALLOC=all_in_mem run
ALLOC=none
# Example: stop at the first failed test:
#   make PYTEST_OPTS=-x tests
PYTEST_OPTS=

PYTEST_BASE_OPTS=-vv -rs --failed-first --cov=$(PWD) --cov-report=term --cov-report=html

ifndef ANTLR4
$(error variable ANTLR4 is not set)
endif


all: run

antlr: $(PACKAGE).g4 
	$(ANTLR4) $< -Dlanguage=Python3 -visitor -no-listener

.PHONY: run $(ASM)
run: $(ASM)
$(ASM): $(TESTFILE) antlr
	python3 $(MAINFILE).py  --reg-alloc=$(ALLOC) $(TESTFILE)

$(OBJ): $(ASM)
	$(ASSEMBLER) libprint.s $< -o $@

.PHONY: trace $(TRACE)
trace: $(TRACE)
	cat $<
$(TRACE): $(OBJ)
	$(SIMU) $(OBJ) >$@

clean:
	rm -rf *~ $(PACKAGE)Lexer* $(PACKAGE)Parser* *.pyc *.tokens  __pycache* .cache/ *.interp
	rm -f tests/*.s tests/*.dot tests/*.dot.pdf tests/*.riscv
	rm -f testsdataflow/*.s testsdataflow/*.dot
	rm -f testsdataflow/*.dot.pdf testsdataflow/*.riscv
	rm -f tests/step1/*.s tests/step1/*.bin
	rm -f tests/step2/*.s tests/step2/*.bin

# Test for naive allocator (also runs test_expect to check // EXPECTED directives):
tests-naive: antlr
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) ./test_codegen.py -k 'naive or expect'

# Test for all but the smart allocator, i.e. everything that lab4 should pass:
tests-notsmart: antlr
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) ./test_codegen.py -k 'not smart'

# Test just the smart allocation (quicker than tests)
tests-smart: antlr
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) ./test_codegen.py -k 'smart'

# Complete testsuite (should pass for lab5):
tests: antlr
	python3 -m pytest $(PYTEST_BASE_OPTS) $(PYTEST_OPTS) ./test_codegen.py


tar: clean
	cd ..; tar cvfz $(DIR)-$(MYNAME).tgz $(DIR) --transform 's/$(DIR)/$(DIR)-$(MYNAME)/'
	@echo "Created ../$(DIR)-$(MYNAME).tgz"
