$(document).ready(function () {
    // $('#btn_click').click(function () {
    //     alert('123');
    // });

    //绑定事件
    $('#btn_click').bind("click", clickHandler1);
    $('#btn_click').bind("click", clickHandler2);

    //解除绑定
    $('#btn_click').unbind("click", clickHandler1);

    function clickHandler1(e) {
        console.log("clickHandler1");
    }

    function clickHandler2(e) {
        console.log("clickHandler2");
    }
});