$(document).ready(function () {
    //异步加载html片段
    $('body').load("box.htm", function (a,status,c) {
        console.log(status);
        if (status=="error"){
            $('body').text('片段加载失败');
        }
        else{
            $('body').append('片段加载成功');
        }
    })

//    异步加载js文件
    $.getScript('../js/testJs.js').complete(function () {
        hello();
    })
});