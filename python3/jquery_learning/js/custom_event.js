var btn_click;
$(document).ready(function () {
    btn_click = $("#btn_clickme");
    btn_click.click(function () {
        var e = $.Event("MyEvent");
        btn_click.trigger(e);
    });

    btn_click.bind('MyEvent', function (event) {
        console.log(event);
    })
});


    
