$(document).ready(function () {
    $('#btn1').click(function () {
        $('p').hide(1000);
    });

    $('#btn2').click(function () {
        $('p').show(1000);
    });

    $('#toggle').click(function () {
        $('p').toggle(1000);
    });
});