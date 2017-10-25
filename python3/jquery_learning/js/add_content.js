$(document).ready(function () {

    $('#btn1').click(function () {
        // $('#p1').append('<a href="http://www.baidu.com">append</a>');
        $('#p1').prepend('<a href="http://www.baidu.com">prepend</a>');
    });

    $('#btn2').click(function () {
        // $('#p1').append('<a href="http://www.baidu.com">append</a>');
        // $('#p2').after('123');
        $('#p2').before('123');

    });

        $('#btn3').click(function () {
            appendElement();
    });
});

function appendElement() {
    /*
    html,jquery,dom
    */
    var text1 = '<p>html</p>';
    var text2 = $('<p></p>').text('jquery');
    var text3 = document.createElement('p').innerHTML = 'dom';
    $('#p2').append(text1,text2,text3);
}