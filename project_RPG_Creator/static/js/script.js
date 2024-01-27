function check_password()
{
    if(document.getElementById("password").value != document.getElementById("password_").value){
        alert("Divergência nas senhas, digite novamente C:");
    }else{
        document.getElementById("submit").click();
    }
}
const themeToggle = document.getElementById('themeToggle');
const root = document.documentElement;

themeToggle.addEventListener('change', function() {
    if (this.checked) {
        root.style.setProperty('--color-background', '#111');
        root.style.setProperty('--color-diff', '#4F4F4F');
        root.style.setProperty('--color-text', 'white');
        localStorage.setItem("theme","dark")
    } else {
        root.style.setProperty('--color-background', 'white');
        root.style.setProperty('--color-diff', 'grey');
        root.style.setProperty('--color-text', '#111');
        localStorage.setItem("theme","white")
    }
});

function displaylist(task)
{
    list = document.querySelector('.list')
    list.style.transition = ".5s";
    if(task == 'open'){
        setTimeout(function() {
            list.style.top = "8%";
            list.style.zIndex = "1";
        }, 50);
    }else if(task == 'close'){
        setTimeout(function() {
            list.style.top = "1%";
            list.style.zIndex = "-1";
        }, 50); 
    }
}

function Theme() {
    if (localStorage.getItem("theme")) {
        if (localStorage.getItem("theme") !== "white") {
            root.style.setProperty('--color-background', '#111');
            root.style.setProperty('--color-diff', '#4F4F4F');
            root.style.setProperty('--color-text', 'white');
            localStorage.setItem("theme","dark")
        }else{
            root.style.setProperty('--color-background', 'white');
            root.style.setProperty('--color-diff', 'grey');
            root.style.setProperty('--color-text', '#111');
            localStorage.setItem("theme","white")
        }
    }
}

Theme();
