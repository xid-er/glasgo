$(document).ready(function (){
  $('#div_id_university').hide();
  $('option').click(function (){
      var selected = this.text;
      if (selected == "Employed"){
        $('#div_id_company').show();
        $('#div_id_university').hide();
      }
      else if(selected == "Student"){
        $('#div_id_company').hide();
        $('#div_id_university').show();
      } else {
        $('#div_id_company').hide();
        $('#div_id_university').hide();
      }
  });
  $(function() {
    $('#toggle-event').change(function() {
      $('#console-event').html('Toggle: ' + $(this).prop('checked'))
    })
  });
});
