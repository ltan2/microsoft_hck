/*
File name: write.js
Description: This file supports educators.html and volunteers.html. Interacts with the server.
*/
document.getElementById("signinbtn").addEventListener("click", function(){
  event.preventDefault();
  signin();
});

function signin()
{
    var input = $('#email').val() + ',' + $('#password').val();
    var queryString = (input != null || input != "") ? "?input=" + input: "";
    $.ajax(
                {
                    url: "/" + queryString,
                    contentType: "application/x-www-form-urlencoded",
                    dataType: "text",
                    type: "POST",

                    beforeSend: function(){

                    },
                    success: function (data) {
                        console.log(data);
                        if(data == "yes")
                        {
                            window.location.href = "texteditor.html";
                        }
                    },
                    complete: function () {

                    },
                    error: function (jqXHR, textStatus, errorThrown) {
                    console.log(errorThrown);
                    }

            }
            );

}