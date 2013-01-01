$(function() {

	$('#id_captcha_1').attr('tabindex', '4');

	var $registerWrapper = $('#register .register-input-wrapper');
	var $registerButton = $('#register-submit')

	if ($('#register-form .board-error').length > 0) {
		$registerWrapper.css('display', 'block');
		$registerButton.removeClass('btn-submit-disabled');
	}
	$('#id_username').bind('focus', function() {
		$registerWrapper.fadeIn('fast');
		$registerButton.removeClass('btn-submit-disabled');
	});
	$('#id_password1').bind('focus', function() {
		$registerWrapper.fadeIn('fast');
		$registerButton.removeClass('btn-submit-disabled');
	});

	$registerButton.click(function() {
		if ($registerWrapper.css('display') == 'none') {
			return false;
		}
	});

});
