function gerarSenha() {
    let tamanho = document.getElementById("tamanho").value;
    let maiusculas = document.getElementById("maiusculas").checked;
    let minusculas = document.getElementById("minusculas").checked;
    let numeros = document.getElementById("numeros").checked;
    let especiais = document.getElementById("especiais").checked;

    let dados = {
        tamanho: tamanho,
        maiusculas: maiusculas,
        minusculas: minusculas,
        numeros: numeros,
        especiais: especiais
    };

    fetch('/gerar_senha', {
        method: 'POST',
        body: JSON.stringify(dados),
        headers: {
            'Content-Type': 'application/json'
        }
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById("senhaGerada").textContent = data.senha;
    })
    .catch(error => console.error('Erro:', error));
}
