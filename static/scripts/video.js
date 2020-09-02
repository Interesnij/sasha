on('body', 'click', '.show_replies', function() {
  this.nextElementSibling.classList.toggle("replies_open")
})

on('body', 'click', '.reply_form_open', function() {
  div = this.nextElementSibling;
  input = div.querySelector(".text-comment");
  user = this.parentElement.querySelector(".commenter").innerHTML;
  input.value = user.replace(/\s+/g, ' ').trim() + ', ';
  div.style.display = "block";
  input.focus();
})

on('body', 'click', '.toggle_show_menu', function() {
  this.nextElementSibling.classList.toggle("show")
})

  on('body', 'click', '#message_send', function() {
    if (!document.body.querySelector("#id_name").value){
      document.body.querySelector("#id_name").style.border = "1px #FF0000 solid";
      toast_error("Введите имя!")}
    else if (!document.body.querySelector("#id_email").value){
      document.body.querySelector("#id_email").style.border = "1px #FF0000 solid";
      toast_error("Введите почту для ответа!")}
    else if (!document.body.querySelector("#id_message").value){
      document.body.querySelector("#id_message").style.border = "1px #FF0000 solid";
      toast_error("Введите сообщение!")}
    form = this.parentElement.parentElement;
    form_data = new FormData(form);
    link = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject( 'Microsoft.XMLHTTP' );
    link.open( 'POST', "/about/send_message/", true );
    link.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
    link.onreadystatechange = function () {
    if ( link.readyState == 4 && link.status == 200 ) {
      form.querySelector("#id_name").value="";
      form.querySelector("#id_email").value="";
      form.querySelector("#id_message").value="";
      toast_success("Письмо отправлено!")
      }};
    link.send(form_data);
  });


on('body', 'click', '.comment', function() {
  form = this.parentElement;
  send_comment(form, form.parentElement.parentElement.previousElementSibling.querySelector(".stream_comments"), '/movies/post-comment/');
});

on('body', 'click', '.reply_comment', function() {
  form = this.parentElement.parentElement.parentElement.parentElement;
  block = form.parentElement.parentElement.querySelector(".stream_reply_comments");
  send_comment(form, block, '/movies/reply-comment/')
  form.parentElement.style.display = "none";
  block.classList.add("replies_open");
});

on('body', 'click', '.reply_parent_comment', function() {
  form = this.parentElement.parentElement.parentElement.parentElement;
  block = form.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
  send_comment(form, block.parentElement, '/movies/reply-comment/')
  form.parentElement.style.display = "none";
  block.classList.add("replies_open");
});

on('body', 'click', '.v_like', function() {
  item = this.parentElement;
  pk = item.getAttribute("data-pk");
  send_like(item, "/movies/like/" + pk + "/");
});
on('body', 'click', '.v_dislike', function() {
  item = this.parentElement;
  pk = item.getAttribute("data-pk");
  send_dislike(item, "/movies/dislike/" + pk + "/");
});

on('body', 'click', '.like2', function() {
  _this = this;
  item = _this.parentElement;
  comment_pk = item.getAttribute("data-pk");
  send_like(item, "/movies/comment_like/" + comment_pk + "/");
});
on('body', 'click', '.dislike2', function() {
  _this = this;
  item = _this.parentElement;
  comment_pk = item.getAttribute("data-pk");
  send_dislike(item, "/movies/comment_dislike/" + comment_pk + "/");
});

on('body', 'click', '.comment_delete', function() {
  comment_delete(this, "/movies/delete_comment/", "comment_abort_remove")
})

on('body', 'click', '.comment_abort_remove', function() {
  comment_abort_delete(this, "/movies/abort_delete_comment/")
});
