$(document).ready(function (){
  $('.dropdown-item').click(function (){
      var selected = this.text;
      if (selected == "Employed"){
        //document.writeln("Employed!");
        $('#occupation_details').attr('placeholder', 'Place of Employment');
        $('.hidden').show();
      }
      else if(selected == "Student"){
        $('#occupation_details').attr('placeholder', 'University');
        $('.hidden').show();
      } else {
        $('.hidden').hide();
      }
      $('.dropdown-toggle').html(this.text);
  });
});
