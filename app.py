app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
from flask import Flask, request, render_template_string
import unicodedata

app = Flask(__name__)

REDES = [
    "LOGIN", "SEVEN", "RF", "PLUGNET", "BKUP", "SULTECH",
    "AC5G", "HP", "AT PLUS", "3SNET", "BLUVELLOX", "INFIX",
    "BLOOM", "BLUFIBRA", "DFS", "HCMRF", "USER", "AXTEL", "NEWBIG",
    "VIACLOUD", "VERSA", "FIBRAVILLE", "CONECT", "STARLYNK", "SPEEDNET",
    "TRIUNFO", "MEGALINK", "FRASANET", "EMOTION", "M&M", "4NET",
    "MUNDODIGITAL", "MIXCONECT", "REDESUL", "MASTERINFO", "LT", "FULLNET"
]

CIDADES = {
    "Brunópolis": "bnu",
    "Campos Novos": "cnv",
    "Curitibanos": "ctb",
    "Fraiburgo": "fbg",
    "Frei Rogério": "frr",
    "Iomerê": "iom",
    "Monte Carlo": "mca",
    "Pinheiro Preto": "ppr",
    "Videira": "vda",
    "Agronômica": "agr",
    "Aurora": "aur",
    "Ituporanga": "itu",
    "Lontras": "lon",
    "Petrolândia": "ptl",
    "Pouso Redondo": "prd",
    "Rio do Sul": "rsl",
    "Campo Belo do Sul": "cbs",
    "Capão Alto": "cat",
    "Correia Pinto": "cpo",
    "Lages": "lgs",
    "Ponte Alta": "pta",
    "Apiúna": "api",
    "Ascurra": "asc",
    "Blumenau": "blu",
    "Indaial": "idl",
    "Rodeio": "rod",
    "Água Doce": "ace",
    "Catanduvas": "ctv",
    "Herval d'Oeste": "hdo",
    "Ibicaré": "ibc",
    "Ipira": "ipi",
    "Joaçaba": "jba",
    "Luzerna": "lzn",
    "Piratuba": "ptb",
    "Salto Veloso": "svs",
    "Tangará": "tan",
    "Treze Tílias": "tzs",
    "Anita Garibaldi": "ant",
    "Caçador": "cdr",
    "Ponte Alta do Norte": "pan",
    "São Cristóvão do Sul": "sct",
    "Araquari": "arq",
    "Balneário Barra do Sul": "bbs",
    "Brusque": "brq",
    "Camboriú": "cmb",
    "Campo Alegre": "cal",
    "Guaramirim": "grm",
    "Jaraguá do Sul": "jas",
    "Joinville": "jve",
    "Luiz Alves": "las",
    "Massaranduba": "mas",
    "São Francisco do Sul": "sfs",
    "Schroeder": "sch",
    "Erval Velho": "evv",
    "Lacerdópolis": "ldp",
    "Rio dos Cedros": "rdc",
    "Balneário Piçarras": "bpi",
    "Barra Velha": "bve",
    "Navegantes": "nav",
    "Penha": "pen",
    "São João do Itaperiú": "sji",
    "Garuva": "gva",
    "Itapoá": "itp"
}

def limpar(txt):
    txt = unicodedata.normalize("NFD", txt)
    txt = txt.encode("ascii", "ignore").decode("utf-8")
    return txt

HTML = """
<!DOCTYPE html>
<html lang="pt-br">
<head>
<meta charset="UTF-8">
<title>Gerador de Login</title>

<style>
body {
    background: radial-gradient(circle at top, #0f2027, #000);
    color: #7CFF7C;
    font-family: Arial;
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: 100vh;
    margin: 0;
}

.container {
    width: 420px;
    padding: 35px;
    border-radius: 16px;
    background: rgba(0,0,0,0.85);
    border: 1px solid #00ff88;
    box-shadow: 0 0 25px rgba(0,255,136,0.4);
}

h2 {
    text-align: center;
    color: #00ff88;
    margin-bottom: 20px;
}

input, select {
    width: 100%;
    padding: 14px;
    margin-bottom: 14px;
    border-radius: 8px;
    border: 1px solid #00ff88;
    background: #050505;
    color: #7CFF7C;
    box-sizing: border-box;
    display: block;
}

button {
    width: 100%;
    padding: 12px;
    border-radius: 8px;
    border: none;
    background: #00ff88;
    color: #000;
    font-weight: bold;
    cursor: pointer;
    margin-top: 5px;
}

button:hover {
    background: #00cc66;
}

.result {
    margin-top: 20px;
    padding: 15px;
    background: #021;
    border-left: 4px solid #00ff88;
}

.copy-btn {
    margin-top: 6px;
}
</style>
</head>

<body>
<div class="container">

<h2>Gerador de Login</h2>

<form method="post">
<input name="nome" placeholder="Nome completo" required>

<select name="cidade" required>
<option value="">Selecione a cidade</option>
{% for c in cidades %}
<option value="{{ cidades[c] }}">{{ c }}</option>
{% endfor %}
</select>

<select name="rede" required>
<option value="">Selecione a rede</option>
{% for r in redes %}
<option value="{{ r }}">{{ r }}</option>
{% endfor %}
</select>

<button type="submit">Gerar Login & Senha</button>
</form>

{% if resultado %}
<div class="result">

<strong>LOGIN:</strong><br>
<span id="login">{{ login }}</span><br>
<button class="copy-btn" onclick="copiar('login')">📋 Copiar Login</button>

<br><br>

<strong>SENHA:</strong><br>
<span id="senha">{{ senha }}</span><br>
<button class="copy-btn" onclick="copiar('senha')">🔑 Copiar Senha</button>

</div>
{% endif %}

</div>

<script>
function copiar(id) {
    const texto = document.getElementById(id).innerText;

    const textarea = document.createElement("textarea");
    textarea.value = texto;
    document.body.appendChild(textarea);

    textarea.select();
    textarea.setSelectionRange(0, 99999);

    document.execCommand("copy");
    document.body.removeChild(textarea);

    alert("Copiado com sucesso!");
}
</script>

</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():

    resultado = False
    login = ""
    senha = ""

    if request.method == "POST":

        nome = limpar(request.form.get("nome", "")).strip()
        cidade = request.form.get("cidade")
        rede = request.form.get("rede")

        partes = [p for p in nome.split() if p]

        if len(partes) >= 2:
            primeiro = partes[0]
            ultimo = partes[-1]

            login = f"{primeiro}.{ultimo}.{cidade}.{rede}".lower()
            senha = "-".join(partes).upper()

            resultado = True

    return render_template_string(
        HTML,
        cidades=CIDADES,
        redes=REDES,
        resultado=resultado,
        login=login,
        senha=senha
    )

import os

port = int(os.environ.get("PORT", 5000))
app.run(host="0.0.0.0", port=port)
