function check_password(){
    if(document.getElementById("password").value != document.getElementById("password_").value){
        alert("Divergência nas senhas, digite novamente C:");
    }else{
        document.getElementById("submit").click();
    }
}