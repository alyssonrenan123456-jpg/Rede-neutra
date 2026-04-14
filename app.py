from flask import Flask, request, render_template_string
import unicodedata

app = Flask(__name__)

# ================= REDES =================
REDES = [
    "LOGIN", "SEVEN", "RF", "PLUGNET", "BKUP", "SULTECH",
    "AC5G", "HP", "AT PLUS", "3SNET", "BLUVELLOX", "INFIX",
    "BLOOM", "BLUFIBRA", "DFS", "HCMRF", "USER", "AXTEL", "NEWBIG",
    "VIACLOUD", "VERSA", "FIBRAVILLE", "CONECT", "STARLYNK", "SPEEDNET",
    "TRIUNFO", "MEGALINK", "FRASANET", "EMOTION", "M&M", "4NET",
    "MUNDODIGITAL", "MIXCONECT", "REDESUL", "MASTERINFO", "LT", "FULLNET"
]

# ================= INTERIOR =================
REDES_INTERIOR = {
    "LOGIN": ["Fraiburgo", "Pinheiro Preto", "Salto Veloso", "Tangará", "Videira"],
    "SEVEN": ["Videira"],
    "RF": ["Fraiburgo"],
    "PLUGNET": ["Fraiburgo"],
    "BKUP": ["Caçador", "Fraiburgo", "Iomerê", "Pinheiro Preto", "Tangará", "Videira"],
    "SULTECH": ["Pouso Redondo", "Rio do Sul", "Petrolândia", "Ituporanga"],
    "BLUVELLOX": ["Blumenau", "Indaial"],
    "INFIX": ["Ascurra"],
    "BLOOM": ["Blumenau"],
    "BLUFIBRA": ["Blumenau", "Indaial"],
    "LT": ["Caçador"],
    "FULLNET": ["Rio do Sul"]
}

# ================= LITORAL =================
REDES_LITORAL = [
    "SPEEDNET", "TRIUNFO", "MEGALINK", "FRASANET",
    "EMOTION", "M&M", "4NET", "MUNDODIGITAL",
    "MIXCONECT", "REDESUL", "MASTERINFO",
    "CONECT", "STARLYNK", "VERSA",
    "VIACLOUD", "AXTEL", "NEWBIG", "USER",
    "HCMRF", "DFS"
]

LITORAL = [
    "Araquari", "Balneário Barra do Sul", "Balneário Piçarras",
    "Barra Velha", "Navegantes", "Penha",
    "São Francisco do Sul", "Itapoá", "Garuva",
    "Brusque", "Camboriú", "Luiz Alves",
    "Massaranduba", "Guaramirim", "Jaraguá do Sul",
    "Joinville", "Schroeder", "Rio dos Cedros"
]

# ================= TODAS CIDADES =================
CIDADES = {
    "Fraiburgo": "fbg", "Pinheiro Preto": "ppr", "Salto Veloso": "svs",
    "Tangará": "tan", "Videira": "vda", "Caçador": "cdr",
    "Iomerê": "iom", "Pouso Redondo": "prd", "Rio do Sul": "rsl",
    "Petrolândia": "ptl", "Ituporanga": "itu",
    "Blumenau": "blu", "Indaial": "idl", "Ascurra": "asc",
    "Araquari": "arq", "Balneário Barra do Sul": "bbs",
    "Balneário Piçarras": "bpi", "Barra Velha": "bve",
    "Navegantes": "nav", "Penha": "pen",
    "São Francisco do Sul": "sfs", "Itapoá": "itp",
    "Garuva": "gva", "Brusque": "brq", "Camboriú": "cmb",
    "Luiz Alves": "las", "Massaranduba": "mas",
    "Guaramirim": "grm", "Jaraguá do Sul": "jas",
    "Joinville": "jve", "Schroeder": "sch",
    "Rio dos Cedros": "rdc"
}

# ================= JUNTA TUDO =================
REDES_CIDADES = {}
REDES_CIDADES.update(REDES_INTERIOR)

for rede in REDES_LITORAL:
    REDES_CIDADES[rede] = LITORAL

# ================= FUNÇÃO =================
def limpar(txt):
    txt = unicodedata.normalize("NFD", txt)
    return txt.encode("ascii", "ignore").decode("utf-8")

# ================= HTML =================
HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Gerador de Login</title>

<style>
.result span {
    color: #ffffff;
    font-weight: bold;
}
* {
    box-sizing: border-box;
}

body {
    margin: 0;
    font-family: Arial, sans-serif;
    background: linear-gradient(135deg, #0f2027, #203a43, #000);
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}

/* CONTAINER */
.container {
    width: 100%;
    max-width: 420px;
    background: rgba(0,0,0,0.85);
    padding: 30px;
    border-radius: 16px;
    box-shadow: 0 0 25px rgba(0,255,136,0.25);
    border: 1px solid #00ff88;
}

/* TÍTULO */
h2 {
    text-align: center;
    color: #00ff88;
    margin-bottom: 25px;
}

/* CAMPOS */
.form-group {
    margin-bottom: 15px;
}

input, select {
    width: 100%;
    padding: 14px;
    border-radius: 10px;
    border: 1px solid #00ff88;
    background: #050505;
    color: #7CFF7C;
    font-size: 14px;
    outline: none;
}

input:focus, select:focus {
    border-color: #00ffaa;
    box-shadow: 0 0 8px rgba(0,255,170,0.5);
}

/* BOTÃO */
button {
    width: 100%;
    padding: 14px;
    border-radius: 10px;
    border: none;
    background: linear-gradient(90deg, #00ff88, #00cc66);
    color: #000;
    font-weight: bold;
    cursor: pointer;
    transition: 0.2s;
    font-size: 15px;
}

button:hover {
    transform: scale(1.02);
    background: linear-gradient(90deg, #00cc66, #00ff88);
}

/* RESULTADO */
.result {
    margin-top: 20px;
    padding: 15px;
    background: #021;
    border-radius: 10px;
    border-left: 4px solid #00ff88;
}

.result strong {
    color: #00ff88;
}

.copy-btn {
    margin-top: 8px;
    padding: 8px;
    font-size: 12px;
    background: #00ff88;
    border-radius: 6px;
    border: none;
    cursor: pointer;
}

/* RESPONSIVO */
@media(max-width: 480px) {
    .container {
        margin: 10px;
    }
}
</style>
</head>

<body>

<div class="container">

<h2>Gerador de Login</h2>

<form method="post">

<div class="form-group">
<input name="nome" placeholder="Nome completo" required>
</div>

<div class="form-group">
<select name="rede" onchange="atualizarCidades()" required>
<option value="">Selecione a rede</option>
{% for r in redes %}
<option value="{{ r }}">{{ r }}</option>
{% endfor %}
</select>
</div>

<div class="form-group">
<select name="cidade" id="cidade" required>
<option value="">Selecione a cidade</option>
</select>
</div>

<button type="submit">Gerar Login</button>

</form>

{% if resultado %}
<div class="result">

<strong>LOGIN:</strong><br>
<span id="login">{{ login }}</span><br>
<button class="copy-btn" onclick="copiar('login')">Copiar</button>

<br><br>

<strong>SENHA:</strong><br>
<span id="senha">{{ senha }}</span><br>
<button class="copy-btn" onclick="copiar('senha')">Copiar</button>

</div>
{% endif %}

</div>

<script>
const redesCidades = {{ redes_cidades | safe }};
const cidadesSiglas = {{ cidades | safe }};

function atualizarCidades() {
    const rede = document.querySelector('[name="rede"]').value;
    const cidadeSelect = document.getElementById("cidade");

    cidadeSelect.innerHTML = '<option value="">Selecione a cidade</option>';

    if (redesCidades[rede]) {
        redesCidades[rede].forEach(cidade => {
            let option = document.createElement("option");
            option.value = cidadesSiglas[cidade];
            option.text = cidade;
            cidadeSelect.appendChild(option);
        });
    }
}

function copiar(id) {
    const texto = document.getElementById(id).innerText;

    const textarea = document.createElement("textarea");
    textarea.value = texto;
    document.body.appendChild(textarea);

    textarea.select();
    document.execCommand("copy");

    document.body.removeChild(textarea);

    alert("Copiado com sucesso!");
}
</script>

</body>
</html>
"""
"""
"""

# ================= ROTA =================
@app.route("/", methods=["GET", "POST"])
def index():
    resultado = False
    login = ""
    senha = ""

    if request.method == "POST":
        nome = limpar(request.form.get("nome", "")).strip()
        cidade = request.form.get("cidade")
        rede = request.form.get("rede")

        partes = nome.split()

        if len(partes) >= 2:
            login = f"{partes[0]}.{partes[-1]}.{cidade}.{rede}".lower()
            senha = "-".join(partes).upper()
            resultado = True

    return render_template_string(
        HTML,
        redes=REDES,
        cidades=CIDADES,
        redes_cidades=REDES_CIDADES,
        resultado=resultado,
        login=login,
        senha=senha
    )

# ================= START =================
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1550)
