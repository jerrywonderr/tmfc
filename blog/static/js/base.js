$(document).ready(function(){
    $(function(){
        let current = $("#main_nav").attr("data-current");
        let nav_items = $("#main_nav").find("li");
        if(current){
            $(nav_items).each(function(){
                if($(this).hasClass(current)){
                    $(".nav-current").removeClass("nav-current");
                    $(this).addClass("nav-current");
                    return false;
                }
            });
            $(".nav-current").click(function(e){
                e.preventDefault(); //Simply to deactivate current page from nav
            });
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
    $(".main-headr > a").click(function(){
        console.log(this);
        let ofset = $(this).attr("data-offset");
        console.log(ofset);
        let offset = $("#content").offset()
        $("main").offset({top: 1, left:offset.left})
    })
});

