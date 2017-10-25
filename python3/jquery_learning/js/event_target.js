$(document).ready(function () {
    $("body").bind("click",bodyHandler);
    $("div").bind("click",divHandler)
});
function bodyHandler(event) {
    // alert("123");
    console.log(event);

}

function divHandler(event) {
    console.log(event);
    //阻止父容器事件冒泡
    // event.stopPropagation();
    //阻止所有父容器冒泡
    // event.stopImmediatePropagation();
}

function console_log(string) {
    console.log(string);
}