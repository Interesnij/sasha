on('body', 'click', '#survey_btn', function() {
  form = this.parentElement;
  pk = form.getAttribute("data-pk");
  form_data = new FormData(form);
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'POST', "/appeal/vote/" + pk + "/", true );
  link.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    window.location = "/appeal/" + pk + "/";
  }};
  link.send(form_data);
});

on('body', 'click', '#remove_user_vote', function() {
  pk = this.getAttribute("data-pk");
  link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
  link.open( 'GET', "/appeal/unvote/" + pk + "/", true );
  link.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
  link.onreadystatechange = function () {
  if ( link.readyState == 4 && link.status == 200 ) {
    window.location = "/appeal/" + pk + "/";
  }};
  link.send();
});
