setInterval(function() {
    document.getElementById("circles").src = "/static/main/circles.png?" + new Date().valueOf();
    console.log("sec")
}, 4000);