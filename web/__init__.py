from flask import Flask, render_template, Response

import json
from jinja2 import Environment, FileSystemLoader, PackageLoader
from pathlib import Path

HERE      = Path(__file__).parent
TEMPLATES = HERE / "templates"
CALS      = HERE / "ics"

env = Environment(loader=FileSystemLoader(TEMPLATES))
env.filters["jsonify"] = json.dumps

locations = [ str(xlsx.stem) for xlsx in Path(CALS).glob("*.ics") ]

app = Flask(
  "getijden",
  template_folder= HERE / "templates",
  static_folder= HERE / "templates/static",
  static_url_path=""
)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():
  template = env.get_template("index.html")
  return template.render(locations=locations)

@app.route("/api/ical/<location>")
def cal(location):
  cal = CALS / f"{location}.ics"
  return Response(cal.read_text(), mimetype="text/calendar")
