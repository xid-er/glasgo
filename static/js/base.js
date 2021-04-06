$(document).ready(function (){
  $('#div_id_university').hide();
  $('#div_id_post_text').hide();
  $('#div_id_post_pic').hide();
  $('#div_id_post_link').hide();

  // Placeholder for picture upload buttons
  $('.custom-file label').each(function(){
    var label_for = $(this).attr('for');
    if (label_for == 'id_picture'){
      $(this).html('Profile Picture');
    }
    else if (label_for == 'id_post_pic'){
      $(this).html('Post Picture');
    }
  });

  // Registration employment
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

  // Post adding type
  $('.custom-control-input').click(function (){
      var selected = this.value;
      if (selected == 'TXT'){
        $('#div_id_post_text').show();
        $('#div_id_post_pic').hide();
        $('#div_id_post_link').hide();
      }
      else if(selected == "IMG"){
        $('#div_id_post_text').hide();
        $('#div_id_post_pic').show();
        $('#div_id_post_link').hide();
      } else if(selected == 'URL'){
        $('#div_id_post_text').hide();
        $('#div_id_post_pic').hide();
        $('#div_id_post_link').show();
      }
  });

  // Post filtering
  $('.cat').click(function(){
    if (! $(this).find('div').hasClass('off')){
      var type = this.id;
      $('.post').each(function(){
        if ($(this).hasClass(type)){
          $(this).hide();
        }
      })
    }
    else {
      var type = this.id;
      $('.post').each(function(){
        if ($(this).hasClass(type)){
          $(this).show();
        }
      })
    }
  });

  // Post sorting
  $('.btn-group-toggle').click(function (){
    // TODO
  });
});

function sortByTop(a, b){

}

function sortByRecent(a, b){

}
