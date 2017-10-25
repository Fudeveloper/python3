var btn1;
var p;
var username;
var btn2;
var a_link;
$(document).ready(function () {
    btn1 = $('#btn1');
    btn2 = $('#btn2');
    p = $('#test');
    username = $('#username');
    a_link = $('#a1');
    btn1.click(function () {
        alert(username.val());
    });

    btn2.click(function () {
        alert(a_link.attr('id'));
    })

});

function console_log(string) {
    console.log(string);
}