function ThemeChanger()
{
    alert('teste');
    toggler = document.getElementById('toggler').style.left 
    if(toggler == "0%"){
        localStorage.setItem("theme", "dark")
        toggler = "50%"
    }else{
        localStorage.setItem("theme", "white")
        toggler = "0%"
    }

}