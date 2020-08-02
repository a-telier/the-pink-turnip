
//datepicker
// document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('.datepicker');
//     var instances = M.Datepicker.init(elems, options);
//   });

$(document).ready(function(){
    $('.datepicker').datepicker();
});

  //selector
//   document.addEventListener('DOMContentLoaded', function() {
//     var elems = document.querySelectorAll('select');
//     var instances = M.FormSelect.init(elems, options);
//   });

$(document).ready(function(){
    $('select').formSelect();
});