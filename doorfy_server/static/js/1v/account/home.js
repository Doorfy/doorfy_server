/**
 * 尝试Backbone进行复杂页面的开发
 */

$(function() {
    seajs.use('app/mustache/mustache.js', function(mustacheModule) {
        var Mustache = mustacheModule.Mustache;
        var App = {
            Models : {},
            Views : {},
            Collections : {},
            Controllers : {},
            initialize : function() {
                new App.Controllers.Routes();
                Backbone.history.start();
            }
        };

        App.Models.Login = Backbone.Model.extend({
            initialize : function() {
                this.set({
                    "message" : "Hello word !",
                    "name" : "HP"
                });
            },
            validate : function(attrs) {
                if (attrs.end < attrs.start) {
                    return "can't end before it starts";
                }
            }
        });

        App.Models.Register = Backbone.Model.extend({
            initialize : function() {
                this.set({
                    "message" : "Hello word !",
                    "name" : "HP"
                });
            },
        });

        App.Views.Login = Backbone.View.extend({
            el : $("#account-form"),
            initialize : function(options) {
                this.options = options;
                this.model = options.model;
                this.on("change", this.render);
                this.on("reset", this.reset);
                _.bindAll(this, "_onSubmit", "render","reset");
            },
            _onSubmit : function(ev) {
                var _self = this;
                $.ajax({
                    url : '/account/login/',
                    data : $('#login-form').serialize(),
                    type : "POST",
                    beforeSend : function() {
                        //console.log('Before send!');
                    },
                    success : function(data) {
                        $(_self.el).html(Mustache.to_html(data, _self.model.toJSON()));
                        $('#login-submit').bind('click', _self._onSubmit);
                        
                    }
                });
                ev.stopPropagation();
                ev.preventDefault();
            },
            render : function() {
                var _self = this;
                $.get('/account/login/', function(data) {
                    $(_self.el).html(Mustache.to_html(data, _self.model.toJSON()));
                    $('#login-submit').bind('click', _self._onSubmit);
                    $('#login-button').addClass('active');
                });
            },
            reset:function(){
                $('#login-button').removeClass('active');
            }
        });

        App.Views.Register = Backbone.View.extend({
            el : $("#account-form"),
            initialize : function(options) {
                this.options = options;
                this.model = options.model;
                this.on("change", this.render);
                this.on("reset", this.reset);
                _.bindAll(this, "_onSubmit", "render","reset");
            },
            _onSubmit : function(ev) {
                var _self = this;
                $.ajax({
                    url : '/account/register/',
                    data : $('#register-form').serialize(),
                    type : "POST",
                    beforeSend : function() {
                        //console.log('Before send!');
                    },
                    success : function(data) {
                        $(_self.el).html(Mustache.to_html(data, _self.model.toJSON()));
                        $('#register-submit').bind('click', _self._onSubmit);
                    }
                });
                ev.stopPropagation();
                ev.preventDefault();
            },
            render : function() {
                var _self = this;
                $.get('/account/register/', function(data) {
                    $(_self.el).html(Mustache.to_html(data, _self.model.toJSON()));
                    $('#register-submit').bind('click', _self._onSubmit);
                    $('#register-button').addClass('active');
                });
            },
            reset:function(){
                $('#register-button').removeClass('active');
            }
        });

        App.Controllers.Routes = Backbone.Router.extend({
            routes : {
                "!/login" : "login",
                "!/register" : "register",
                "" : "login", // 默认为登陆的状态
            },
            login : function() {
                var loginModel = new App.Models.Login;
                var loginView = new App.Views.Login({
                    model : loginModel
                });
                var registerModel = new App.Models.Register;
                var registerView = new App.Views.Register({
                    model : registerModel
                });
                loginView.trigger("change");
                registerView.trigger("reset");
            },
            register : function() {
                var loginModel = new App.Models.Login;
                var loginView = new App.Views.Login({
                    model : loginModel
                });
                var registerModel = new App.Models.Register;
                var registerView = new App.Views.Register({
                    model : registerModel
                });
                registerView.trigger("change");
                loginView.trigger("reset");
            }
        });
        App.initialize();
    });
});