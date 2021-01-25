on('body', 'click', '#survey_btn', function() {
  form = this.parentElement;
  pk = form.getAttribute("data-pk");
  form_data = new FormData(form);
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/appeal/vote/" + pk + "/", true );
  link.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    window.location = "/appeal/a" + pk + "/";
  }};
  link.send(form_data);
});
