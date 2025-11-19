import requests

def pesquisar_duckduckgo(termo):
    url = "https://api.duckduckgo.com/"
    params = {
        "q": termo,
        "format": "json",
        "no_redirect": 1,
        "no_html": 1
    }

    resposta = requests.get(url, params=params)
    if resposta.status_code == 200:
        dados = resposta.json()
        print("Resumo:", dados.get("Abstract", "Nenhum resumo encontrado."))
        print("Link:", dados.get("AbstractURL", "Nenhum link encontrado."))
    else:
        print("Erro na requisição:", resposta.status_code)

# Exemplo de uso
pesquisar_duckduckgo("Robot Framework")
