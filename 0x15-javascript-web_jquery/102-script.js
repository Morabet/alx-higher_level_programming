window.onload = function () {
  $('#btn_translate').click(function () {
    const language = $('#language_code').val();
    $.get(
      'https://hellosalut.stefanbohacek.dev/?lang=' + language,
      function (data) {
        $('#hello').html(data.hello);
      }
    );
  });
};
