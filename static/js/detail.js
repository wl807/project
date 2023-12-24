// document.querySelector(".moreAnswer").addEventListener("click", (e) => {
//   e.preventDefault();
//   const commentSection = document.querySelector(".commentSection");
//   if (commentSection.style.display === "none") {
//     commentSection.style.display = "block";
//   } else {
//     commentSection.style.display = "none";
//   }
//   console.log("답변의 댓글이 클릭됨");
// });

const moreAnswer = document.querySelectorAll(".more-answer-comment");
moreAnswer.forEach((more) => {
  more.addEventListener("click", (e) => {
    e.preventDefault();

    // 답변의 댓글 클릭 시 안 보이던 comment 영역 보여주기
    const eventTarget = e.target; //대상 찾기

    // 이벤트 대상의 부모찾기
    const eventParentTarget = eventTarget.closest(".d-flex");
    console.log(eventParentTarget);

    // 이벤트 대상의 부모 다음 요소 찾기
    const comment = eventParentTarget.nextElementSibling;
    console.log(comment);

    if (comment != null) {
      if (comment.style.display == "block") {
        comment.style.display = "none";
      } else {
        comment.style.display = "block";
      }
    }
  });
});
