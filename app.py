from flask import Flask, render_template, request
from database import init_db, guardar_grup, carregar_grup
# Creem aplicació
app = Flask(__name__)
init_db()
# Definim endpoint y el tipus de peticions que s'accepten
@app.route("/", methods=["GET", "POST"])
def index():
	# Gestionem 
	if request.method == "POST":
		noms_text = request.form.get("noms")
		if noms_text:
			grup = [nom.strip() for nom in noms_text.split(",")]
			guardar_grup(grup)
	grup = carregar_grup()
	return render_template("index.html", grup=grup)
# Le decimos a la app como desplegarse, por donde escuchar las peticiones
if __name__ == "__main__":
	app.run(host="0.0.0.0", port=80, debug=False)
