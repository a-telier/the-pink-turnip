//  NAV BAR
//  document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.sidenav');
//     var instances = M.Sidenav.init(elems, options);
//   });

  // Or with jQuery

  $(document).ready(function(){
    $('.sidenav').sidenav();
  });

//  FORM
//  SELECTOR
    document.addEventListener('DOMContentLoaded', function() {
        var elems = document.querySelectorAll('select');
        var instances = M.FormSelect.init(elems, options);
    });
    // $(document).ready(function(){
    //     $('select').formSelect();
    // });

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