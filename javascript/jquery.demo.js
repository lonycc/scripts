// $.extend()扩展jQuery
$.extend({
    sayHello: function(name) {
        console.log('Hello, ' + (name ? name : 'Dude') + '!');
    }
});
$.sayHello();
$.sayHello('tony');

// $.fn向jQuery添加方法
$.fn.myPlugin = function(options) {
    var defaults = {
        'color': 'red',
        'fontSize': '12px'
    };
    var settings = $.extend({}, defaults, options);
    this.css({
        'color': settings.color,
        'fontSize': settings.fontSize
    });
    return this.each(function() {
        $(this).append($(this).attr('href'));
    }); //加了return则支持链式调用
};
$('a').myPlugin({ 'color': '#ab2312', 'fontSize': '12px' });


// 完整例子
;
(function($, window, document, undefined) {
    //定义Beautifier的构造函数
    var Beautifier = function(ele, opt) {
        this.$element = ele,
            this.defaults = {
                'color': 'red',
                'fontSize': '12px',
                'textDecoration': 'none'
            },
            this.options = $.extend({}, this.defaults, opt)
    }
    //定义Beautifier的方法
    Beautifier.prototype = {
        beautify: function() {
            return this.$element.css({
                'color': this.options.color,
                'fontSize': this.options.fontSize,
                'textDecoration': this.options.textDecoration
            });
        }
    }
    //在插件中使用Beautifier对象
    $.fn.myPlugin = function(options) {
        //创建Beautifier的实体
        var beautifier = new Beautifier(this, options);
        //调用其方法
        return beautifier.beautify();
    }
})(jQuery, window, document);
