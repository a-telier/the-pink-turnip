//  NAV BAR
$(document).ready(function() {
    $('.sidenav').sidenav();
    $('.dropdown-trigger').dropdown({ hover: false });
    $('select').formSelect();
  });

//  AUTORESIZING
//  ingredients
    $('#ingredients').val('New Text');
    M.textareaAutoResize($('#ingredients'));
//  instructions
    $('#instructions').val('New Text');
    M.textareaAutoResize($('#instructions'));

// PASSWORD
function showPassword() {
    var myInput = document.getElementById("myInput");
    if (input.type === "password") {
        input.type = "text";
    } else {
        input.type = "password";
    }
}