$(document).ready(function(){

    "use strict";

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
    $(".suggestions").on("click", function(){
        let title = $(this).attr("data-title");
        window.location.href = (`/article/${title}`);
    });
    $(".continue-btn").on("click", function(){
        // Just to remove the view from behind the header
        let offset = $('main').position().top;
        let headerHeight = $(".main-nav").outerHeight();
        $("html, body").animate({scrollTop: offset - headerHeight}, 'slow');
    });
    $(() => {
        const pageURL = location.href;
        if (pageURL.includes('content')) {
            // Just to remove the view from behind the header
            let offset = $('main').position().top;
            let headerHeight = $(".main-nav").outerHeight();
            $("html, body").animate({scrollTop: offset - headerHeight}, 'slow');
        }
    });

    $('.delete-btn').on('click', async (ev) => {
        try {
            let url = $(ev.target).attr('data-href');
            const response = await fetch(url, {
                method: 'DELETE',
                headers: {
                    'X-CSRFToken': Cookies.get('csrftoken')
                }
            });
            if (response.ok) {
                location.reload();
            }
        } catch (err) {
            console.log(err);
        }
        
    });
});

