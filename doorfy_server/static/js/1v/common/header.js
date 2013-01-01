$(function() {
	var $loginWrapper = $('#login-form .login-input-wrapper')
	if($('#login-form .board-error').length > 0){
		$loginWrapper.css('display','inline');
	}
	
	$('#login-submit').click(function() {
		
		if ($loginWrapper.css('display') === 'none') {
			$loginWrapper.fadeIn('fast');
			$('#login-username').focus();
			return false;
		}		
	});
});