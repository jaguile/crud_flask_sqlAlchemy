
const globalBaixa   = document.getElementById("global_baixa");
const llistaBaixa   = document.querySelectorAll('.baixa_usuari');
const form_usuaris  = document.getElementById("form_usuaris");

for (const usuari of llistaBaixa)  {
    usuari.addEventListener("click", function() {
        let algunMarcat = Array.from(llistaBaixa).some((c) => {return c.checked})
        console.log(algunMarcat);
        globalBaixa.checked = algunMarcat ? true : false;
    });
}

globalBaixa.addEventListener("click", function() {
    if (this.checked) {
        llistaBaixa.forEach((c) => {c.checked = true;})
    } else {
        llistaBaixa.forEach((c) => {c.checked = false;})
    }
});

document.getElementById("global_baixa_action").addEventListener("click", function(event) {
    if (confirm("Segur que vol donar de baixa aquests usuaris?")){
		form_usuaris.action = this.getAttribute('data-action');
        form_usuaris.submit();
	} else {
        event.preventDefault();
    }
});

function checkNom () {
    return document.getElementById("nom").value != '' ? true : false;
};

function checkCognoms () {
    return document.getElementById("cognoms").value != '' ? true : false;
};

function checkForm () {
    document.getElementById("afegir_usuari").addEventListener("submit", function(event) {
        if (!checkTitol() || !checkCognoms()) {
            alert("Usuari ha de tenir nom i cognoms");
            event.preventDefault();
            return;
        }
    });
}

checkForm();

