function loadMore(e) {
  const commentPage = document.getElementById('comment_page');
  const state = commentPage.classList.contains('extendComments');
  console.log('test');
  console.log(commentPage);
  if(state) {
    commentPage.classList.remove('extendComments');
    e.innerText = 'Show More';
  } else {
    commentPage.classList.add('extendComments');
    e.innerText = 'Show Less';
  }
}
