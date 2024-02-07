window.onload = function () {
  $('#btn_translate').on('click', function () {
    const lang = $('#language_code').val();
    const url = 'https://hellosalut.stefanbohacek.dev/?lang=' + lang;

    $.get(url, function (response) {
      $('#hello').text(response.hello);
    });
  });

  // Listen for the "keydown" event on the input field
  $('#language_code').on('keydown', function (event) {
    // Check if the pressed key is the "Enter" key (keyCode 13)
    if (event.keyCode === 13) {
      // Trigger the click event of the button
      $('#btn_translate').click();
    }
  });
};
