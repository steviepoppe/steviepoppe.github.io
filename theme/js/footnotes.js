var sups = document.getElementsByTagName('sup');
var footnotehtml = [];
for(var i=0; i<sups.length; i++) {
    var sup = sups[i];
    if(sup['id'] && sup['id'].substr(0,3) == 'fnr') {
        var footnr = sup['id'].substr(3);
        var footnote = document.getElementById('fn'+footnr);
        if(!footnote) continue;
        footnotehtml[i] = footnote.innerHTML;
        sup.setAttribute('footnoteindex',i);
        sup.onmouseover = function(event) {
            var footnotepopup = document.getElementById('footnotepopup');
            if(footnotepopup) footnotepopup.parentNode.removeChild(footnotepopup);
            var index = parseInt(this.getAttribute('footnoteindex'));
            var popup = document.createElement('div');
            popup.innerHTML = footnotehtml[index];
            popup.id = 'footnotepopup';
            popup.style.position = 'absolute';
            popup.style.left = (event.pageX - 125) + 'px';
            popup.style.top = (event.pageY + 25) + 'px';
            popup.style.width = '250px';
            popup.style.textAlign = 'left';
            popup.style.backgroundColor = '#4a525a';
            popup.style.border = '1px solid #636363';
            popup.style.padding = '10px';
            
            document.body.appendChild(popup);
        };
        sup.onmouseout = function(event) {
            var footnotepopup = document.getElementById('footnotepopup');
            if(footnotepopup) footnotepopup.parentNode.removeChild(footnotepopup);
        };
    }
}