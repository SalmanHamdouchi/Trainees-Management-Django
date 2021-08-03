function openModal() {
    var overlay = document.getElementById("overlay");
    document.getElementById("overflowContent").style.overflow = "auto";
    overlay.style.zIndex = "0";
    overlay.style.backgroundColor = "";
    overlay.style.top = "";
    overlay.style.bottom = "";
    overlay.style.left = "";
    overlay.style.right = "";
    var modal = document.getElementById("modal");
    if (modal.style.display == "") {
        modal.style.display = "block";
        document.getElementById("overflowContent").style.overflow = "hidden";
        overlay.style.zIndex = "99";
        overlay.style.backgroundColor = "#00000052";
        overlay.style.top = "0";
        overlay.style.bottom = "0";
        overlay.style.left = "0";
        overlay.style.right = "0";
    } else {
        modal.style.display = "";
    }
}