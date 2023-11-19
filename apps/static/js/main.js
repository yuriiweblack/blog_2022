
//document.window("Hello")
//let text=152
//alert("What do you need?")

function togglePassword() {
       const passwordField = document.getElementById("password");
      if (passwordField.type === "password") {
          passwordField.type = "text";
      } else {
          passwordField.type = "password";
      }
    }

togglePassword()


//  window.addEventListener("load", function(){
//    var checkbox  = document.getElementById('{{form.check.id}}');
//    var x = document.getElementById('{{form.password.id}}');
//    checkbox.addEventListener('change', function() {
//        if(this.checked) {
//            x.type = 'text';
//        } else {
//            x.type = 'password';
//        }
//    });
//});
