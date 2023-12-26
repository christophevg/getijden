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
