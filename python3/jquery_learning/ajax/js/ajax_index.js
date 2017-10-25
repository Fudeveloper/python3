$(document).ready(function () {
    $('#btn').click(function () {
        $('#result').text("请求数据中....");

        $.get("http://192.168.17.128:8001/get_test/", {p1: $("#namevalue").val()}, function (data) {
            alert('loading')
            $('#result').text(data)
        }).error(function () {
            alert('访问错误');
        })
    })
});