$(document).ready(function () {

//========CSRF TOKEN=======================================
var csrftoken = $('meta[name=csrf-token]').attr('content')

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!/^(GET|HEAD|OPTIONS|TRACE)$/i.test(settings.type)) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken)
        }
    }
})
//==========================================================
//================submitting form===========================

  $("#loginForm").submit(function (event) {
    let status = document.getElementById("status");
    status.innerHTML = "";
    var formData = {
      email: $("#email").val(),
      password: $("#password").val(),
    };

    $.ajax({
      type: "POST",
      url: "/user/login",
      data: formData,
      success: function(response) {
        window.open(window.location.origin, "_self");
     },
    error: function(jqXHR, textStatus, errorThrown, data) {
    status.innerHTML = "";
    let errorMessage = JSON.parse(jqXHR.responseText).error;
    status.innerHTML = errorMessage;
  }
    }),

    event.preventDefault();
  });
//  ==================================================
  $("#registerForm").submit(function (event) {
    let status = document.getElementById("status");
    status.innerHTML = "";
    var formData = {
      username: $("#username").val(),
      email: $("#email").val(),
      password: $("#password").val(),
    };

    $.ajax({
      type: "POST",
      url: "/user/register",
      data: formData,
      success: function(response) {
        window.open(window.location.origin + '/user/login', "_self");
     },
    error: function(jqXHR, textStatus, errorThrown, data) {
    status.innerHTML = "";
    let errorMessage = JSON.parse(jqXHR.responseText).error;
    status.innerHTML = errorMessage;
  }
    }),

    event.preventDefault();
  });
});
