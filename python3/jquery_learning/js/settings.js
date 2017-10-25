var p1;
var btn1;
var p2;
$(document).ready(function () {
    p1 = $('#p1');
    btn1 = $('#btn1');
    p2 = $('#p2');

    btn1.click(function () {
        p1.text('123');
    })

    $('#btn2').click(function () {
        p2.html('<a href="http://www.baidu.com">啦啦啦</a>')
    });


    $('#btn3').click(function () {
        $('#input1').val('change');
    })

    $('#btn4').click(function () {
        $('#p4').attr({
            "style":"background-color: #000000",
            "title":"change"
        })
    });
});