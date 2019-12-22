# Installs :

# Decide where to build and install, create directory

	# Also add the following two lines to ~/.bashrc
	export RISCV=/opt/riscv 	# Adapt as needed
	PATH="$RISCV"/bin:"$PATH"

	RISCV_BUILD="$HOME"/riscv-build # Adapt as needed

	sudo mkdir "$RISCV"
	sudo chown "$LOGNAME": "$RISCV"
	mkdir "$RISCV_BUILD"

## RISC-V C and C++ cross-compiler

	sudo apt-get install autoconf automake autotools-dev curl libmpc-dev libmpfr-dev libgmp-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev libexpat-dev

	cd "$RISCV_BUILD"
	git clone --recursive https://github.com/riscv/riscv-gnu-toolchain
	cd riscv-gnu-toolchain
	./configure --prefix="$RISCV"
	make -j 4
	##[Mac OS X] only do instead of make -j 4:
	make 

Quick check:

	riscv64-unknown-elf-gcc --version

Must output:

	riscv64-unknown-elf-gcc (GCC) 8.3.0
	Copyright (C) 2018 Free Software Foundation, Inc.
	This is free software; see the source for copying conditions.  There is NO
	warranty; not even for MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

## Simu (spike) in riscv-tools

	sudo apt-get install autoconf automake autotools-dev curl libmpc-dev libmpfr-dev libgmp-dev libusb-1.0-0-dev gawk build-essential bison flex texinfo gperf libtool patchutils bc zlib1g-dev device-tree-compiler pkg-config libexpat-dev

	cd "$RISCV_BUILD"
	git clone --recursive https://github.com/riscv/riscv-tools.git
	cd riscv-tools/
	./build.sh
	##[Mac OS X] Edit the Makefile.in in risc-isa-sim/ and replace:
	##         $(AR) -rcs -o $$@ $$^
	## by      $(AR) rcs  $$@ $$^

Quick test:

	spike pk

Must output:

	bbl loader
	tell me what ELF to load!


# Alternative 1 : binary installation

A pre-compiled archive is available here:

  https://matthieu-moy.fr/spip/?Pre-compiled-RISC-V-GNU-toolchain-and-spike

This is known to work on Ubuntu 18.04. Use at your own risk anywhere
else.

# Alternative 2 : docker

Docker is a lightweight alternative to virtual machines. An image with
RISC-V tools, LaTeX and Python is given here:

  https://cloud.docker.com/u/mmoy/repository/docker/mmoy/riscv-latex-python

To launch it with the current directory mounted, run:

```
sudo docker run --rm -ti -v $PWD:/home/compil --user $(id -u):$(id -g) -w /home/compil mmoy/riscv-latex-python
```

The current directory on your host machine is mounted in /home/compil,
which is the default working directory. Anything access to files you
perform in this directory will actually be performed on the host
machine. Anything you do outside this directory will be lost when you
exit the docker. A typical use is to run your text editor on the host
machine, and run compilation & tests within Docker.


# Achlinux installation 
If not done already, you can enable compilation on all your CPU cores for Makepkg, in /etc/makepkg.conf change MAKEFLAGS :

	MAKEFLAGS="-j$(nproc)" #You can set "-jxx" with xx the desired number of threads you want
	COMPRESSGZ=(pigz -c -f -n)
	COMPRESSBZ2=(pbzip2 -c -f)
	COMPRESSXZ=(xz -c -z - --threads=0)
	COMPRESSZST=(zstd -c -z -q - --threads=0)

For more infos visit :https://wiki.archlinux.org/index.php/Makepkg#Parallel_compilation

Now you can install from AUR __riscv64-unknown-elf-gcc__ and __riscv64-unknown-elf-newlib__ for the c standard lib.

To install spike :

	pacman -S spike
Then you will need _pk_ from AUR __riscv-pk__

To run spike you need to specify the path of pk and run :

	spike /usr/riscv64-linux-gnu/bin/pk program.riscv
instead of :

	spike pk program.risc

You can create an alias in your bashrc and call

	spike(){
		args=()
		for var in "$@"; do
			if [[ $var == "pk" ]]; then #catch the pk parameter and replace it by its real path
				args+=("/usr/riscv64-linux-gnu/bin/pk")
			else
				args+=($var)
			fi
		done
		/bin/spike $args
		#for a less intrusive script, name the function spike2 and call spike $args at the end
	}
