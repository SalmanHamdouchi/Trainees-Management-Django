var tabs = document.getElementsByClassName("panel");
var maxHeight1 = document.getElementById("perso").offsetHeight;
var maxHeight2 = document.getElementById("pass").offsetHeight;
for (var i = 0; i < tabs.length; i++)
    tabs[i].style.height = 0;

function showTab(panelIndex) {
    for (var i = 0; i < tabs.length; i++)
        tabs[i].style.height = 0;
    document.getElementById("perso-btn").style.borderLeft = "";
    document.getElementById("pass-btn").style.borderLeft = "";
    document.getElementById("pass-btn").style.backgroundColor = "";
    document.getElementById("perso-btn").style.backgroundColor = "";
    document.getElementById("perso-btn").style.color = "#484e6f";
    document.getElementById("pass-btn").style.color = "#484e6f";
    if (tabs[panelIndex].style.display == "") {
        for (var i = 0; i < tabs.length; i++) {
            tabs[i].classList.remove("showPanel");
        }
        tabs[panelIndex].classList.add("showPanel");
        if (panelIndex == 0) {
            document.getElementById("perso").style.height = maxHeight1 + "px";
            document.getElementById("perso-btn").style.borderLeft = "2px solid #5d78ff";
            document.getElementById("perso-btn").style.backgroundColor = "#f2f2f2";
            document.getElementById("perso-btn").style.color = "#1c35b3";
        } else if (panelIndex == 1) {
            $('html, body').animate({
                scrollTop: $('#pass').offset().top
            }, 500);
            document.getElementById("pass").style.height = maxHeight2 + "px";
            document.getElementById("pass-btn").style.borderLeft = "2px solid #5d78ff";
            document.getElementById("pass-btn").style.backgroundColor = "#f2f2f2";
            document.getElementById("pass-btn").style.color = "#1c35b3";
        }
    }
}

showTab(0);
