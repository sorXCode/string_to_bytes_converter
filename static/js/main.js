$("#str_to_hex").change(function() {
    if (!this.checked){
        bytesInputMode()
    }
    else {
        textInputMode()
    }
}
)

$("#close").click( function(){
    $(".alert-message").hide();
}
)

function textInputMode(){
    $("#encoding").parent().show()
    $("#add_prefix").parent().show()
    $("#text").prop("required", true)
    $("#result").prop("required", false)
    $('button[type="submit"]').text("Convert Text to Bytes")
}

function bytesInputMode(){
    $("#encoding").parent().hide()
    $("#add_prefix").parent().hide()
    $("#text").prop("required", false)
    $("#result").prop("required", true)
    $('button[type="submit"]').text("Convert Bytes to Text")
}

$(function() {
    textInputMode()
})