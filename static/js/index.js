// owl carousel
$(document).ready(function () {
  var owl = $(".owl-carousel");
  owl.owlCarousel({
    items: 2, // 한번에 보여지는 이미지 수
    loop: true, // 항목들을 무한으로 반복하여 보여줄지 여부
    autoplay: true, // 자동으로 슬라이드 쇼를 시작할지 여부
    autoplayTimeout: 5000, // 다음 이미지로 넘어가는 시간 (단위 : 밀리초)
    autoplayHoverPause: true,
    responsive: {
      0: {
        items: 1,
      },
      770: {
        items: 3,
      },
      1300: {
        items: 3,
      },
    },
    nav: true,
    navText: [
      '<i class="fa fa-angle-left" aria-hidden="true"></i>',
      '<i class="fa fa-angle-right" aria-hidden="true"></i>',
    ],
  });

  // custom btn 생성 시
  $(".customNextBtn").click(function () {
    owl.trigger("next.owl.carousel");
  });

  $(".customPrevBtn").click(function () {
    owl.trigger("prev.owl.carousel", [300]);
  });
});

// pagination
document.querySelector(".pagination").addEventListener("click", (e) => {
  e.preventDefault(); // a 태그 기능 중지

  console.log(e.target.href); // http://127.0.0.1:8000/board/10
  console.log(e.target.getAttribute("href")); // 10

  location.href = `/blog/?page=${e.target.getAttribute("href")}`;
});

// 작성일자 표시 ~일 전전
function getTimeDifference(timestamp) {
  const currentTime = new Date();
  const targetTime = new Date(timestamp);
  const timeDifference = currentTime - targetTime;

  const minutes = Math.floor(timeDifference / (1000 * 60));

  if (minutes < 1) {
    return "방금 전";
  } else if (minutes < 60) {
    return minutes + "분 전";
  } else {
    const hours = Math.floor(minutes / 60);
    if (hours < 24) {
      return hours + "시간 전";
    } else {
      const days = Math.floor(hours / 24);
      return days + "일 전";
    }
  }
}
const timezone = document.querySelectorAll(".time");
// timezone.forEach((time) => {
//   const timestampText = time.textContent;
//   const timestamp = timestampText.replace(/년|월|일|오후/g, "").trim();
//   //   console.log(timestamp);

//   // "2023-12-24T12:34:56"; // 여기에 원하는 타임스탬프를 입력하세요.
//   const timeDifferenceText = getTimeDifference(timestamp);
//   //   console.log(timeDifferenceText);

//   time.innerHTML = timeDifferenceText;
// });
