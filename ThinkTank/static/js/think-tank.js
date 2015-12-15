$(document).ready(function () {
	$("#login-error").val("");
	$("#login-button").on("click", function () {
		var data = JSON.stringify({
			email: $("input[name=email]").val(),
			password: $("input[name=password]").val()
		});
		$.ajax({
			url: "/api/auth",
			type: "POST",
			data: data,
			contentType: "application/json; charset=utf-8",
			dataType: "json"
		})
		.success(function (results) {
			$.cookie("token", results["token"]);
			$("#login-form").submit();
		})
		.fail(function (error) {
			$("#login-error").text(JSON.parse(error.responseText).message);
			console.log(error);
		});
	});
});
