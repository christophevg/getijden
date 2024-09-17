LEVEL=taw

SRCS=xlsx-*
TRG=ics

all: $(TRG)

$(TRG): $(SRCS)
	python getijden.py $^

clean:
	rm -rf $(TRG)

requirements.txt:
	@cat $@ | cut -d"=" -f1 | xargs pip uninstall -y
	pip install -U pip
	pip install -r requirements.base.txt
	pip freeze > $@

.PHONY: requirements.txt

web:
	gunicorn -w 1 --threads 8 web:app

.PHONY: web
	