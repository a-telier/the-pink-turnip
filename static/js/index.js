
//ADDRECIPE template/form
//DATEPICKER --> not used anymore, using .now function instead
    // document.addEventListener('DOMContentLoaded', function() {
    //     var elems = document.querySelectorAll('.datepicker');
    //     var instances = M.Datepicker.init(elems, options);
    // });
    //   $(document).ready(function(){
    //     $('.datepicker').datepicker();
    //   });
    // $(document).ready(function () {
    //     $(".datepicker").pickadate({
    //         format: "dd/mm/yyyy",
    //         setDefaultDate: true
    //     });
    // });

// from Code Institute - As of 20th June, 2019
// there is an issue with the current version of Materialize and Chrome version 73 onwards
    // document.getElementById("matfix").addEventListener("click", function(e) {
    //     e.stopPropagation();
    // });

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