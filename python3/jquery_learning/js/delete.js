$(document).ready(function () {
    $('#btn1').click(function () {
        // $('div').empty();//删除子级元素
        $('div').remove(); //删除子级元素包括自己
    });
});