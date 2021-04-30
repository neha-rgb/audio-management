$(function () {

    /* Functions */
  
    var loadForm = function () {
      var btn = $(this);
      $.ajax({
        url: btn.attr("data-url"),
        type: 'get',
        dataType: 'json',
        beforeSend: function () {
          $("#modal-song").modal("show");
        },
        success: function (data) {
          $("#modal-song .modal-content").html(data.html_form);
        }
      });
    };

    $("#songlist").on("click", ".btnSong", loadForm);

});