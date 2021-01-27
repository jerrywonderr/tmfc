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
    $(".suggestions").on("mouseenter", function(){
        $(this).find(".hovered-post").removeClass("d-none")
    });
    $(".suggestions").on("mouseleave", function(){
        $(this).find(".hovered-post").addClass("d-none");
    });
    $(".suggestions").click(function(){
        let title = $(this).attr("data-title");
        window.location.href = (`/article/${title}`);
    });
    $(".main-headr > a").click(function(){
        console.log(this);
        let ofset = $(this).attr("data-offset");
        console.log(ofset);
        let offset = $("#content").offset()
        $("main").offset({top: 1, left:offset.left})
    })
});

