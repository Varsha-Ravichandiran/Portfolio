python=/usr/bin/env python

all: clean build

build:
	mkdir -p static
	mkdir -p public
	$(python) manage.py collectstatic --noinput
	$(python) manage.py distill-local public --force

clean:
	rm -rf public
	rm -rf static
