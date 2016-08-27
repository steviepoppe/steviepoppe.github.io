// this script requires jQuery
$(document).ready(function() {
    Footnotes.setup();
});

var Footnotes = {
    footnotetimeout: false,
    setup: function() {
        var footnotelinks = $("a[rel='footnote']")


            $("a[rel='footnote']").on('click',Footnotes.footnotescroll);
            $("a[rev='footnote']").on('click',Footnotes.footnotescroll);

        footnotelinks.unbind('mouseover',Footnotes.footnoteover);
        footnotelinks.unbind('mouseout',Footnotes.footnoteoout);
        
        footnotelinks.bind('mouseover',Footnotes.footnoteover);
        footnotelinks.bind('mouseout',Footnotes.footnoteoout);
    },
    footnoteover: function() {
        clearTimeout(Footnotes.footnotetimeout);
        $('#footnotediv').stop();
        $('#footnotediv').remove();
        
        var id = $(this).attr('href').substr(1);
        var position = $(this).offset();
    
        var div = $(document.createElement('div'));
        div.attr('id','footnotediv');
        div.bind('mouseover',Footnotes.divover);
        div.bind('mouseout',Footnotes.footnoteoout);

        var el = document.getElementById(id);
        div.html($(el).html());
        
        $(document.body).append(div);

        var left = position.left;
        if(left + (div.width() + 20)  > $(window).width())
            left = $(window).width() - (div.width() + 20);
        var top = position.top+20;
        if(top + div.height() > $(window).height() + $(window).scrollTop())
            top = position.top - div.height() - 15;
        div.css({
            left:left,
            top:top
        });
    },
    footnoteoout: function() {
        Footnotes.footnotetimeout = setTimeout(function() {
            $('#footnotediv').animate({
                opacity: 0
            }, 600, function() {
                $('#footnotediv').remove();
            });
        },100);
    },
    divover: function() {
        clearTimeout(Footnotes.footnotetimeout);
        $('#footnotediv').stop();
        $('#footnotediv').css({
                opacity: 0.9
        });
    },


    footnotescroll: function(e) {
  var t, a, n, r, o, i;
  if (location.pathname.replace(/^\//, "") === this.pathname.replace(/^\//, "") || location.hostname === this.hostname) {
    if (e.preventDefault(), o = $("nav.navbar").height() + 32, $(this).hasClass("footnote-backref")) 
        return i = "footnote-highlight", n = $(this), t = $('[id="' + n.attr("href").slice(1) + '"]'), 
    a = t.closest("p, ul, ol"), a.addClass(i), a.one("webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend", 
        function() {
      return console.log("hello"), a.removeClass(i)
    }), $("html,body").animate({
      scrollTop: a.offset().top - o
    }, 500), !1;
    if ($(this).hasClass("footnote-ref")) {
      if (r = this.hash.slice(1), n = $('[id="' + r + '"]'), n.length) return $("html,body").animate({
        scrollTop: n.offset().top - o
      }, 500), !1
    } else if (n = $(this.hash), n = n.length ? n : $('[name="' + this.hash.slice(1)(NaN)), n.length) return $("html,body").animate({
      scrollTop: n.offset().top - o
    }, 500), !1
  }
}
}

$(document).ready(function(){


    $('a[href^="#"]:not(a[rel="footnote"]):not(a[rev="footnote"]):not(a[id="backtotop"])').on('click',function (e) {
        e.preventDefault();

        var target = this.hash;
        var $target = $(target);

$('html, body').stop().animate({
     'scrollTop': $target.offset().top
}, 500, 'swing');
    });

        $('a[id="backtotop"]').on('click',function (e) {
        e.preventDefault();

        var target = this.hash;
        var $target = $(target);

$('html, body').stop().animate({ scrollTop: 0 }, 400, 'swing');
    });
});


