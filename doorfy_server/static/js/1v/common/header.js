$(function() {
	function isEmail(strEmail) {
	    if (strEmail.search(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/) != -1) {
	        return true;   
	    } else {
	        return false;  
	    }   	
	}
	
	// 登陆了相关
	$('#login').bind('click', function(){
		$('#login-modal').modal({
            keyboard: false
        });
	});
	
	$('#login-password').bind('keypress', function(ev) {
   		if(ev.charCode == 13) {
   			$('#login-button').click();
   		 	ev.preventDefault();
   		}
    });
	
	$('#login-button').bind('click', function(){
		var check = true;
		if($('#login-username').val().length == 0 || !isEmail($('#login-username').val())) {
			$('#login-username-group').addClass('error');
			$('#login-username-group .help-inline').text('不正确的邮箱!').show();
			check = false;
		} else {
			$('#login-username-group').removeClass('error');
			$('#login-username-group .help-inline').hide();
		}
		if($('#login-password').val().length == 0) {
			$('#login-pwd-group').addClass('error');
			$('#login-pwd-group .help-inline').text('密码不能为空!').show();
			check = false;
		} else {
			$('#login-pwd-group').removeClass('error');
			$('#login-pwd-group .help-inline').hide();
		}
		
		if(!check){
			$(this).attr('disabled',false).text('登陆');
			return;
		} else {
			$('#login-message').hide();
			$(this).attr('disabled','disabled').text('登陆中...');
		}
		$.ajax({
            url: "/account/login/",
            data: $('#login-form').serialize(),
            cache: false,
            type: 'POST',
            success: function(serverData) {
                var result = $.parseJSON(serverData);
                var codeArr = result.code;
                var loginSuccess = false;
                for(var i = 0; i < codeArr.length; i++) {
                	$('#login-username-group').removeClass('error');
            		$('#login-pwd-group').removeClass('error');
            		if(codeArr[i] >= 0) {
            			$('#login-button').text('登陆成功');
            			loginSuccess = true;
            			window.location.reload();
            			break;
            		}
            		if(codeArr[i] == -1) {
            			$('#login-message').text('用户名与密码不匹配!').show();
                		$('#login-pwd-group').addClass('error');
                	} else {
                		$('#login-message').hide();
                	}
            		if(codeArr[i] == -2) {
                		$('#login-username-group').addClass('error');
                	}
                	if(codeArr[i] == -3) {
                		$('#login-pwd-group').addClass('error');
                	}
                }
                if(!loginSuccess) {
                	$('#login-button').attr('disabled',false).text('登陆');
                }
            }
        });
	});
});