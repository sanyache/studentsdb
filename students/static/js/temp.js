function initEditStudentPage(){
    $('a.student-edit-form-link').click(function(event){
        var link = $(this);
        $.ajax({
            'url': link.attr('href'),
            'dataType': 'html',
            'type': 'get',
            'success': function(data, status, xhr){
                if (status != 'success'){
                    alert('Помилка на сервері.Спробуйте пізніше');
                    return false;
                }

            var modal = $('#myModal'),
                html = $(data), form = html.find('#content-column form');
            modal.find('.modal-title').html(html.find('#content-column h2').text());
            modal.find('.modal-body').html(form);
            initEditStudentForm(form, modal);
            modal.modal('show');
            },
            'error': function(){
                alert('Помилка на сервері');
                return false;
            }
        });

        return false;
    });
}

function initEditStudentForm(form, modal){
    initDateFields();
    form.find('input[name="cancel_button"]').click(function(event){
        modal.modal('hide');
        return false;
    });

    form.ajaxForm({
        'dataType': 'html',
        'error': function(){
            alert('Помилка на сервері');
            return false;
        },
        'success': function(data, status, xhr){
            var html = $(data);
            var  newform = html.find('#content-column form');
            modal.find('.modal-body').html(html.find('.alert'));
            if (newform.length > 0){
                modal.find('.modal-body').append(newform);
                //initEditStudentForm(newform, modal);
            } else {

                setTimeout(function(){location.reload(true);}, 500);
            }
         }

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
    }

  });
}