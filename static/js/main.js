$("#str_to_hex").change(function() {
    if (!this.checked){
        $("#encoding").parent().hide()
        $("#add_prefix").parent().hide()
        $("#text").prop("required", false)
        $("#result").prop("required", true)
    }
    else {
        $("#encoding").parent().show()
        $("#add_prefix").parent().show()
        $("#text").prop("required", true)
        $("#result").prop("required", false)
    }
}
)

$("#close").click( function(){
    console.log("closed");
    $(".alert-message").hide();
}
)

$(function() {
    $("#text").prop("required", true)
    $("#result").prop("required", false)
})