$("#upload-label").change(function () {
    $("#file-name").text(this.files[0].name);
});
