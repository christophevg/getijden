# Getijden in ICS

> getijden importeerbaar in je calendar software

## Rationale

Ik zocht een calendar-compatibele versie van de getijden nabij Zeebrugge, en na vijf minuten was ik het zoeken beu 😇

## TLDR;

Deze repo bevat een ICS versie van de getijden zoals ze gepubliceerd worden door het [Agentschap Maritieme Dienstverlening en Kust](https://www.agentschapmdk.be/nl/publicaties?category=nautische-publicaties). Daar vind je ZIP bestanden met Excel bestanden met de getijden voor een heel jaar. De software in deze repo verwerkt deze Excel bestanden tot [ICS bestanden](ics-getijdentabellen-taw-2024) dat je kan importeren in je calendar software.

👉 [Getijden nabij Zeebrugge 2024](ics-getijdentabellen-taw-2024/zeebrugge2024-getijtabel-mTAW.ics)

## Zelf de software gebruiken

stap 1: clone deze repo

```console
% git clone https://github.com/christophevg/getijden
% cd getijden
```

stap 2: installeer de nodige modules (bij voorkeur in een virtuele omgeving, zoals hier met `pyenv`)

```console
% pyenv virtualenv getijden
% pyenv local getijden
(getijden) % pip install -r requirements.txt
```

stap 3: download het ZIP bestand van [Agentschap Maritieme Dienstverlening en Kust](https://www.agentschapmdk.be/nl/publicaties?category=nautische-publicaties): e.g. [(ZIP) Getijtabellen TAW 2024](https://www.agentschapmdk.be/nl/bijlage/9b98b44a-3f4c-4ad5-8ca2-35f427631cf2/xlsx-getijtabellen-taw-2024)

```console
(getijden) % curl -o xlsx-getijtabellen-taw-2024.zip https://www.agentschapmdk.be/nl/bijlage/9b98b44a-3f4c-4ad5-8ca2-35f427631cf2/xlsx-getijtabellen-taw-2024
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
100 1006k  100 1006k    0     0  2707k      0 --:--:-- --:--:-- --:--:-- 2758k
(getijden) % unzip -d xlsx-getijtabellen-taw-2024 xlsx-getijtabellen-taw-2024.zip 
Archive:  xlsx-getijtabellen-taw-2024.zip
  inflating: xlsx-getijtabellen-taw-2024/antwerpen2024-getijtabel-mTAW.xlsx  
  inflating: xlsx-getijtabellen-taw-2024/blankenberge2024-getijtabel-mTAW.xlsx  
  inflating: xlsx-getijtabellen-taw-2024/nieuwpoort2024-getijtabel-mTAW.xlsx  
  inflating: xlsx-getijtabellen-taw-2024/oostende2024-getijtabel-mTAW.xlsx  
  inflating: xlsx-getijtabellen-taw-2024/prosperpolder2024-getijtabel-mTAW.xlsx  
  inflating: xlsx-getijtabellen-taw-2024/vlissingen2024-getijtabel-mTAW.xlsx  
  inflating: xlsx-getijtabellen-taw-2024/wintam2024-getijtabel-mTAW.xlsx  
  inflating: xlsx-getijtabellen-taw-2024/zeebrugge2024-getijtabel-mTAW.xlsx 
```

step 4: voer het script uit en geef het de naam van de uitgepakte

```console
(getijden) % python getijden.py xlsx-getijtabellen-taw-2024
👉 generating iCal files for xlsx-getijtabellen-taw-2024 into ics-getijtabellen-taw-2024
👷‍♂️ converting xlsx-getijtabellen-taw-2024/vlissingen2024-getijtabel-mTAW.xlsx
👷‍♂️ converting xlsx-getijtabellen-taw-2024/wintam2024-getijtabel-mTAW.xlsx
👷‍♂️ converting xlsx-getijtabellen-taw-2024/oostende2024-getijtabel-mTAW.xlsx
👷‍♂️ converting xlsx-getijtabellen-taw-2024/antwerpen2024-getijtabel-mTAW.xlsx
👷‍♂️ converting xlsx-getijtabellen-taw-2024/prosperpolder2024-getijtabel-mTAW.xlsx
👷‍♂️ converting xlsx-getijtabellen-taw-2024/nieuwpoort2024-getijtabel-mTAW.xlsx
👷‍♂️ converting xlsx-getijtabellen-taw-2024/zeebrugge2024-getijtabel-mTAW.xlsx
👷‍♂️ converting xlsx-getijtabellen-taw-2024/blankenberge2024-getijtabel-mTAW.xlsx
(getijden) % ls ics-getijtabellen-taw-2024
antwerpen2024-getijtabel-mTAW.ics     prosperpolder2024-getijtabel-mTAW.ics
blankenberge2024-getijtabel-mTAW.ics  vlissingen2024-getijtabel-mTAW.ics
nieuwpoort2024-getijtabel-mTAW.ics    wintam2024-getijtabel-mTAW.ics
oostende2024-getijtabel-mTAW.ics      zeebrugge2024-getijtabel-mTAW.ics
```

