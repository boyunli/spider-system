$(document).ready(function(){
    $("#login").click(function(){
        var user = $("#username").val();
        var pwd = $("#password").val();
        var pd = {"username":user, "password":pwd};
        $.ajax({
            type:"post",
            url:"/login",
            data:JSON.stringify(pd),
            cache:false,
            success:function(data){
                alert(JSON.parse(data));
            },
            /*error:function(){
                alert("error!");
            },*/
        });
    });
    $("#crawl_submit").click(function(){
        var website = $("#crawl_website").val();
        var keyword = $("#crawl_keyword").val();
        var pd = {"website":website, "keyword":keyword};
        $.ajax({
            type:"get",
            url:"/index/crawler",
            data:JSON.stringify(pd),
            cache:false,
            success:function(data){
                alert(JSON.parse(data));
            },
            /*error:function(){
                alert("error!");
            },*/
        });
    });
});
