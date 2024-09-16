from flask import Flask, render_template, Response

from pathlib import Path


HERE = Path(__file__).parent
CALS = HERE / "ics-getijtabellen-taw-2024"

app = Flask(
  "getijden",
  template_folder= HERE / "templates",
  static_folder= HERE / "templates/static",
  static_url_path=""
)

app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.route("/")
def home():
  return render_template("index.html", title="Getijden")

@app.route("/api/cal/<location>")
def cal(location):
  cal = CALS / f"{location}2024-getijtabel-mTAW.ics"
  return Response(cal.read_text(), mimetype="text/calendar")
