const globalEsborrar = document.getElementById("global_esborrar");
const llistaEsborrar = document.querySelectorAll('.esborra_llibre');
const form_llibres = document.getElementById("form_llibres");

for (const llibre of llistaEsborrar)  {
    llibre.addEventListener("click", function() {
        let algunMarcat = Array.from(llistaEsborrar).some((c) => {return c.checked})
        console.log(algunMarcat);
        globalEsborrar.checked = algunMarcat ? true : false;
    });
}

globalEsborrar.addEventListener("click", function() {
    if (this.checked) {
        llistaEsborrar.forEach((c) => {c.checked = true;})
    } else {
        llistaEsborrar.forEach((c) => {c.checked = false;})
    }
});

document.getElementById("global_esborrar_action").addEventListener("click", function(event) {
    if (confirm("Segur que vol esborrar aquests llibres?")){
		form_llibres.action = this.getAttribute('data-action');
        form_llibres.submit();
	} else {
        event.preventDefault();
    }
});

const llistatPrestecs = document.getElementsByClassName("btn-prestec");
const prestecModal = new bootstrap.Modal('#usuarisPrestec');

for (llibrePrestec of llistatPrestecs) {
    llibrePrestec.addEventListener("click", function() {
        let idLlibre = this.getAttribute("data-llibre");
        let titolLlibre = this.getAttribute("data-titol");
        document.getElementById("llibrePrestat").innerHTML = titolLlibre;
        document.getElementById("idLlibre").value = idLlibre;
        document.getElementById("usuarisPrestec").getAttribute("data-llibre").value = idLlibre;
        prestecModal.show();
    });
}

document.getElementById("prestar-llibre").addEventListener("click", function() {
    document.getElementById("form_prestec").submit();
});

function checkTitol () {
    return document.getElementById("titol").value != '' ? true : false;
};

function checkForm () {
    document.getElementById("afegir_llibre").addEventListener("submit", function(event) {
        if (!checkTitol()) {
            alert("Titol no pot quedar buit");
            event.preventDefault();
            return;
        }
        console.log(this.action);
    });
}

checkForm();

