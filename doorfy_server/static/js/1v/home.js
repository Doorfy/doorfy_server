$(function(){
	function isEmail(strEmail) {
	    if (strEmail.search(/^\w+((-\w+)|(\.\w+))*\@[A-Za-z0-9]+((\.|-)[A-Za-z0-9]+)*\.[A-Za-z0-9]+$/) != -1) {
	        return true;   
	    } else {
	        return false;  
	    }   	
	}
	// 邀请相关
	if(!PAGE_CONFIG['authenticated']) {
	    $('#enter').bind('click', function(){
	        $('#invite-form .control-group').show();
	        $('#invite-form .help-inline').hide();
	        $('#invite-form .control-group').removeClass('error');
	        $('#invite-email').attr('disabled',false);
	        $('#invite-button').attr('disabled',false);
	        $('#invite-message').hide();
	        $('#invite-modal').modal({
	            keyboard: false
	        });
	        var inviteEmail = $('#invite-email');
	        inviteEmail.val('');
	    });
	}
    
    $('#invite-email').bind('keypress', function(ev) {
   		if(ev.charCode == 13) {
   			$('#invite-button').click();
   		 	ev.preventDefault();
   		}
    });
    
    $('#invite-button').bind('click',function(){
        var inviteEmail = $('#invite-email');
        if(inviteEmail.val().length > 0 && isEmail(inviteEmail.val())){
            $.ajax({
                url: "/account/invitation/",
                data: $('#invite-form').serialize(),
                cache: false,
                type: 'POST',
                success: function(serverData) {
                    var result = $.parseJSON(serverData);
                    if(result.code >= 0) {
                        // 正确
                        $('#invite-message').removeClass().addClass('alert alert-success').text('我们会尽快发送邀请链接!').show();
                        $('#invite-button').attr('disabled','disabled').text('申请');
                        $('#invite-form .control-group').hide();
                    } else if(result.code == -1) {
                        $('#invite-message').removeClass().addClass('alert alert-info').text('邮箱已经邀请过了.').show();
                        $('#invite-form .control-group').show();
                        $('#invite-form .help-inline').hide();
                        $('#invite-form .control-group').removeClass('error');
                        $('#invite-email').attr('disabled',false);
                        $('#invite-button').attr('disabled',false).text('申请');
                    } else if(result.code == -2){
                        $('#invite-message').removeClass().addClass('alert alert-error').text('邮箱填写错误').show();
                        $('#invite-email').attr('disabled',false);
                        $('#invite-button').attr('disabled',false).text('申请');
                    }
                }
            });
            $(this).attr('disabled','disabled').text('申请中...');
            inviteEmail.attr('disabled','disabled');
            $('#invite-form .control-group').removeClass('error');
            $('#invite-form .help-inline').hide();
            $('#invite-message').hide();
        } else {
            $('#invite-form .control-group').addClass('error');
            $('#invite-form .help-inline').text('邮箱格式错误').show();
        }
    });
});

$(function(){
	// 注册相关
	if(PAGE_CONFIG['register']) {
		$('#register-modal').modal({
            keyboard: false
        });
		$('#register-username').val(PAGE_CONFIG['username']).attr('disabled','disabled');
	}
	
	$('#register-button').bind('click', function(){
		var check = true;
		if($('#register-password1').val().length == 0) {
			$('#register-pwd-group').addClass('error');
			$('#register-pwd-group .help-inline').text('密码不能为空!').show();
			check = false;
		} else {
			$('#register-pwd-group').removeClass('error');
			$('#register-pwd-group .help-inline').hide();
		}
		if(!check){
			$(this).attr('disabled',false).text('新用户注册');
			return;
		} else {
			$('#register-message').hide();
			$(this).attr('disabled','disabled').text('注册中...');
		}
		$.ajax({
            url: "/account/register/",
            data: $('#register-form').serialize(),
            cache: false,
            type: 'POST',
            success: function(serverData) {
                var result = $.parseJSON(serverData);
                var codeArr = result.code;
                for(var i = 0; i < codeArr.length; i++) {
                	$('#register-email-group').removeClass('error');
            		$('#register-pwd-group').removeClass('error');
            		if(codeArr[i] >= 0) {
            			window.location = '/family/list/';
            		}
            		if(codeArr[i] == -1) {
            			$('#register-message').text('邮箱已经注册!').show();
                		$('#register-email-group').addClass('error');
                	} else {
                		$('#register-message').hide();
                	}
            		if(codeArr[i] == -2) {
                		$('#register-email-group').addClass('error');
                	}
                	if(codeArr[i] == -3) {
                		$('#register-pwd-group').addClass('error');
                	}
                }
            }
        });
	});
});