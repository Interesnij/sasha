
on('body', 'click', '.blog_comment', function() {
  form = this.parentElement;
  send_comment(form, form.parentElement.parentElement.previousElementSibling.querySelector(".stream_comments"), '/blog/post-comment/');
});

on('body', 'click', '.blog_reply_comment', function() {
  form = this.parentElement.parentElement.parentElement.parentElement;
  block = form.parentElement.parentElement.parentElement;
  send_comment(form, block, '/blog/reply-comment/')
  form.parentElement.style.display = "none";
  block.classList.add("replies_open");
});

on('body', 'click', '.blog_reply_parent_comment', function() {
  form = this.parentElement.parentElement.parentElement.parentElement;
  block = form.parentElement.parentElement.parentElement.parentElement.parentElement;
  send_comment(form, block.parentElement, '/blog/reply-comment/')
  form.parentElement.style.display = "none";
  block.classList.add("replies_open");
});

on('body', 'click', '.b_like', function() {
  item = this.parentElement;
  pk = item.getAttribute("data-pk");
  send_like(item, "/blog/like/" + pk + "/");
});
on('body', 'click', '.b_dislike', function() {
  item = this.parentElement;
  pk = item.getAttribute("data-pk");
  send_dislike(item, "/blog/dislike/" + pk + "/");
});

on('body', 'click', '.blog_like2', function() {
  _this = this;
  item = _this.parentElement;
  comment_pk = item.getAttribute("data-pk");
  send_like(item, "/blog/comment_like/" + comment_pk + "/");
});
on('body', 'click', '.blog_dislike2', function() {
  _this = this;
  item = _this.parentElement;
  comment_pk = item.getAttribute("data-pk");
  send_dislike(item, "/blog/comment_dislike/" + comment_pk + "/");
});

on('body', 'click', '.blog_comment_delete', function() {
  comment_delete(this, "/blog/delete_comment/", "blog_comment_abort_remove")
})

on('body', 'click', '.blog_comment_abort_remove', function() {
  comment_abort_delete(this, "/blog/abort_delete_comment/")
});
