const $ = window.$;
$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data, err) {
  $('DIV#hello').text(data.hello);
});
