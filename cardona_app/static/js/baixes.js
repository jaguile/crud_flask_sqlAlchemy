
const globalAlta   = document.getElementById("global_alta");
const llistaAlta   = document.querySelectorAll('.alta_usuari');
const form_usuaris  = document.getElementById("form_usuaris");

for (const usuari of llistaAlta)  {
    usuari.addEventListener("click", function() {
        let algunMarcat = Array.from(llistaAlta).some((c) => {return c.checked})
        console.log(algunMarcat);
        globalAlta.checked = algunMarcat ? true : false;
    });
}

globalAlta.addEventListener("click", function() {
    if (this.checked) {
        llistaAlta.forEach((c) => {c.checked = true;})
    } else {
        llistaAlta.forEach((c) => {c.checked = false;})
    }
});

document.getElementById("global_alta_action").addEventListener("click", function(event) {
    if (confirm("Segur que vol donar d'alta aquests usuaris?")){
		form_usuaris.action = this.getAttribute('data-action');
        form_usuaris.submit();
	} else {
        event.preventDefault();
    }
});

