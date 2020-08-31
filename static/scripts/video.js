

on('body', 'click', '.comment', function() {
  form = this.parentElement.parentElement.parentElement;
  send_comment(form, form.parentElement.previousElementSibling, '/movies/post-comment/');
});

on('body', 'click', '.reply_comment', function() {
  form = this.parentElement.parentElement.parentElement.parentElement;
  block = form.parentElement.parentElement.querySelector(".stream_reply_comments");
  send_comment(form, block, '/movies/reply-comment/')
  form.parentElement.style.display = "none";
  block.classList.add("replies_open");
});

on('body', 'click', '.u_reply_parent_comment', function() {
  form = this.parentElement.parentElement.parentElement.parentElement;
  block = form.parentElement.parentElement.parentElement.parentElement.parentElement.parentElement;
  send_comment(form, block.parentElement, '/movies/reply-comment/')
  form.parentElement.style.display = "none";
  block.classList.add("replies_open");
});

on('body', 'click', '.like', function() {
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  send_like(item, "/movies/user_like/" + pk + "/");
});
on('body', 'click', '.dislike', function() {
  item = this.parentElement.parentElement.parentElement.parentElement;
  pk = item.getAttribute("data-pk");
  send_dislike(item, "/movies/dislike/" + pk + "/");
});

on('body', 'click', '.like2', function() {
  _this = this;
  item = _this.parentElement;
  comment_pk = item.getAttribute("data-pk");
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  send_like(item, "/movies/comment_like/" + comment_pk + "/");
});
on('body', 'click', '.dislike2', function() {
  _this = this;
  item = _this.parentElement;
  comment_pk = item.getAttribute("data-pk");
  pk = document.body.querySelector(".pk_saver").getAttribute("data-pk");
  send_dislike(item, "/movies/comment_dislike/" + comment_pk + "/");
});

on('body', 'click', '.comment_delete', function() {
  comment_delete(this, "/movies/delete_comment/", "comment_abort_remove")
})

on('body', 'click', '.comment_abort_remove', function() {
  comment_abort_delete(this, "/movies/abort_delete_comment/")
});
