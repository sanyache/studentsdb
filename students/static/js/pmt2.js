function initGroupSelector(){
    $('#group-selector select').change(function(event){
      var group = $(this).val();
      if (group) {
        $.cookie('current_group', group, {'path': '/', 'expires': 365});
      } else {
        $.removeCookie('current_group', {'path': '/'});
      }
      location.reload(true);
      return true;
    });
}

function initDateFields(){
    $('input.dateinput').datetimepicker({
        'format': 'YYYY-MM-DD'
    });
}

function initEditStudentPage() {
  $('a.student-edit-form-link').click(function(event){
    var link = $(this);
    $.ajax({
      'url': link.attr('href'),
      'dataType': 'html',
      'type': 'get',
      'success': function(data, status, xhr){
        // check if we got successfull response from the server
        if (status != 'success') {
          alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
          return false;
        }
        // update modal window with arrived content from the server
        var modal = $('#myModal'),
          html = $(data), form = html.find('#content-column form');
        modal.find('.modal-title').html(html.find('#content-column h2').text());
        modal.find('.modal-body').html(form);

        // init our edit form
        //initEditStudentForm(form, modal);

        // setup and show modal window finally
        modal.modal({
          'keyboard': false,
          'backdrop': false,
          'show': true
        });
      },
      'error': function(){
          alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
          return false;
      }
    });

    return false;
  });
}



function initEditStudentForm(form, modal) {
  // attach datepicker
  initDateFields();

  // close modal window on Cancel button click
  form.find('input[name="cancel_button"]').click(function(event){
    modal.modal('hide');
    return false;
  });

  // make form work in AJAX mode
  form.ajaxForm({
    'dataType': 'html',
    'error': function(){
      alert('Помилка на сервері. Спробуйте будь-ласка пізніше.');
      return false;
    },
    'success': function(data, status, xhr) {
      var html = $(data), newform = html.find('#content-column form');

      // copy alert to modal window
      modal.find('.modal-body').html(html.find('.alert'));

      // copy form to modal if we found it in server response
      if (newform.length > 0) {
        modal.find('.modal-body').append(newform);

        // initialize form fields and buttons
        initEditStudentForm(newform, modal);
      } else {
        // if no form, it means success and we need to reload page
        // to get updated students list;
        // reload after 2 seconds, so that user can read
        // success message
        setTimeout(function(){location.reload(true);}, 500);
      }
    },
    'beforeSend': function(data, status, xhr) {
				//$('input', 'textarea').attr('readonly','true');
				modal.find('.modal-body').html('<div class="progress"><div class="progress-bar" role="progressbar"
        aria-valuenow="70" aria-valuemin="0" aria-valuemax="100" style="width:70%">70%</div></div>');
    }
  });
}
    return false;
  });
}
