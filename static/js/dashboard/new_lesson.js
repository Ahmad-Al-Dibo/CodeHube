
import DEBUG from "../config.js";

document.addEventListener("DOMContentLoaded", function () {
    if (window.location.hash === "#newCourse") {
        // hier gebeurt "iets"

        if (DEBUG){
        console.log("newCourse fragment gedetecteerd.");
        console.log("To stop debuging, set `DEBUG = false` in config.js");
        };

        // document.getElementById("new-course-form").style.display = "block";
    }
});

