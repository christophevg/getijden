from flask import Flask, render_template, Response

import json
from jinja2 import Environment, FileSystemLoader, PackageLoader
from pathlib import Path

HERE      = Path(__file__).parent
TEMPLATES = HERE / "templates"
STATIC    = TEMPLATES / "static"
CALS      = HERE / "ics"

env = Environment(loader=FileSystemLoader(TEMPLATES))
env.filters["jsonify"] = lambda x: json.dumps(x, indent=2)

locations = sorted([ str(xlsx.stem) for xlsx in Path(CALS).glob("*.ics") ])
calendars = {
  "webcal" : {
    "label": "Apple Calendar, Outlook, ... (Webcal)",
    "href": "webcal://",
    "blank": False
  },
  "google" : {
    "label": "Google Calendar",
    "href": "https://calendar.google.com/calendar/r?cid=webcal://",
    "blank": True
  },
  "microsoft" : {
    "label": "Microsoft 365",
    "href": "https://outlook.office.com/calendar/0/addfromweb?url=webcal://",
    "blank": True
  },
  "ics" : {
    "label": "iCal",
    "href": "//",
    "blank": False
  }
}

app = Flask(
  "getijden",
  template_folder= TEMPLATES,
  static_folder= STATIC,
  static_url_path=""
)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():
  template = env.get_template("index.html")
  return template.render(locations=locations, calendars=calendars)

@app.route("/api/ical/<location>")
def cal(location):
  cal = CALS / f"{location}.ics"
  return Response(cal.read_text(), mimetype="text/calendar")
