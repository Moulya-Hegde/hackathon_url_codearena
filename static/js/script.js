function playsound() {
  var aud = new Audio("./wrong.mp3");
  aud.play();
}

function effect(dec,acc) { 
    $(".progress").removeClass("hidden")
  if (dec==="good") {
    $(".text").html("<p>SAFE URL, GO AHEAD AND BROWSE &#x1F60A;  !!!!</p>");
    $(".acc").html(`<p>Accuracy: ${acc}`)
    $("body").addClass("pressed-r");
    setTimeout(() => {
      $("body").removeClass("pressed-r");  
    }, 1000);
  } else {
    $(".text").html("<p>UNSAFE URL, BE AWARE  &#x1F620;!!!!</p>");
    $(".acc").html(`<p>Accuracy: ${acc}`)
    $("body").addClass("pressed-w");
    setTimeout(() => {
      $("body").removeClass("pressed-w");
    }, 1000);
  }
}


function fetchData() {
    return new Promise((resolve, reject) => {
        // Simulating an async operation
        setTimeout(() => {
            resolve('Data fetched successfully');
        }, 20000);
    });
}


$("button").click(function (event) {
  event.preventDefault();
  $(".progress").addClass("hidden");
  var url = $("#in").val();
  $.ajax({
    type: "POST",
    url: "/",
    data: { 'url': url },
    success: function (response) {
    
      effect(response.message,response.is_valid)
      
    },
    error: function (error) {
      console.log(error);
    },
  });
});

$("input").on("keydown", function (event) {
    
  if (event.key === "Enter") {
    $(".progress").addClass("hidden");
    var url = $("#in").val();
  $.ajax({
    type: "POST",
    url: "/",
    data: { 'url': url },
    success: function (response) {
      effect(response.message,response.is_valid)
    },
    error: function (error) {
      console.log(error);
    },
  });
  }
});
