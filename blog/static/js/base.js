$(document).ready(function(){
    $(function(){
        let current = $("#main_nav").attr("data-current");
        let page_list = ["about", "contact", "collections", "dashboard"];
        let nav_items = $("#main_nav").find("li");
        if(current){
            for(nav_item of nav_items){
                if($(nav_item).hasClass(current)){
                    $(".nav-current").removeClass("nav-current");
                    $(nav_item).addClass("navcurrent");
                }
            }
        }
    });

    $(".menu-btn").click(function(){
        let fd = $(".main-nav nav").parent();
        fd.toggleClass("d-none").toggleClass("col-12");
    });
    $(".back-btn").click(function(){
        window.history.back()
    });
    $(".read_next a").on("mouseenter", function(){
        $(this).parent().parent().find(".text-center").addClass("hovered_post");
    });
    $(".read_next a").on("mouseout", function(){
        $(this).parent().parent().find(".text-center").removeClass("hovered_post");
    });
    $(".main-header > a").click(function(){
        console.log(this);
        let offset = $(this).attr("data-offset");
        console.log(offset);
        $(this).css("margin-bottom", "1000px !important");
    })
});

