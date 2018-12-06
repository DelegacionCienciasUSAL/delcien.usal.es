$(document).foundation();
$(document).ready(function(){
    $(window).scroll(function(){
        if ($(window).width()>=768){
            if ($(document).scrollTop()>=192){
                $('header nav#principal').addClass('flotante');
            }else{
                $('header nav#principal').removeClass('flotante');
            }
        }else{
            if ($(document).scrollTop()>=120){
                $('header nav#principal').addClass('flotante');
            }else{
                $('header nav#principal').removeClass('flotante');
            }
        }   
    })
});