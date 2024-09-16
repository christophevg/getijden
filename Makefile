YEAR?=2024

NAME=getijtabellen-taw-$(YEAR)
SRC=xlsx-$(NAME)
TRG=ics-$(NAME)
URL="https://www.agentschapmdk.be/nl/publicaties?category=nautische-publicatie"

all: $(TRG)

$(TRG): $(SRC)
	python getijden.py $<

$(SRC): $(SRC).zip
	unzip -d $@ $<

$(SRC).zip:
	@echo "🛑 please download $@ from $(URL) first..."
	@exit 1

requirements.txt:
	@cat $@ | cut -d"=" -f1 | xargs pip uninstall -y
	pip install -U pip
	pip install -r requirements.base.txt
	pip freeze > $@

.PHONY: requirements.txt

run:
	gunicorn -w 1 --threads 16 web:app
