from pyscript import document  # type: ignore

def somar(event):
    primeiro_termo = float(document.querySelector("#primeiro_termo").value)
    segundo_termo = float(document.querySelector("#segundo_termo").value)
    soma = primeiro_termo + segundo_termo
    document.querySelector("#saida").innerText = f"{soma}"