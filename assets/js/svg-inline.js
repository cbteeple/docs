/*$(document).ready(readyFn);


function readyFn(jQuery) {

    // Replace SVG images with inline
    jQuery('img').filter(function () {
        return this.src.match(/.*\.svg$/);
    }).each(function () {
        var $img = jQuery(this);
        var imgID = $img.attr('id');
        var imgClass = $img.attr('class');
        var imgURL = $img.attr('src');


        jQuery.get(imgURL, function (data) {
            // Get the SVG tag, ignore the rest
            var $svg = jQuery(data).find('svg');

            // Add replaced image's ID to the new SVG
            if (typeof imgID !== 'undefined') {
                $svg = $svg.attr('id', imgID);
            }
            // Add replaced image's classes to the new SVG
            if (typeof imgClass !== 'undefined') {
                $svg = $svg.attr('class', imgClass + ' replaced-svg');
            }

            removeStyles($svg)

            // Remove any invalid XML tags as per http://validator.w3.org
            $svg = $svg.removeAttr('xmlns:a');

            // Replace image with new SVG
            $img.replaceWith($svg);

        }, 'xml');

    });

    nav_bar();

}


function removeStyles(el) {
    el.removeAttr('style');

    jQuery(el).find('g').each(function () {
        var $g = jQuery(this).find('g');
        $g.removeAttr('style');
    });

}

*/



*  Replace all SVG images with inline SVG *
$(\'img.svg\').each(function(){
    var $img = $(this);
    var imgID = $img.attr(\'id\');
    var imgClass = $img.attr(\'class\');
    var imgURL = $img.attr(\'src\');

    $.get(imgURL, function(data) {
         Get the SVG tag, ignore the rest
        var $svg = $(data).find(\'svg\');
         Add replaced image\'s ID to the new SVG
        if (typeof imgID !== \'undefined\') {
            $svg = $svg.attr(\'id\', imgID);
        }
         Add replaced image\'s classes to the new SVG
        if (typeof imgClass !== \'undefined\') {
            $svg = $svg.attr(\'class\', imgClass+\' replaced-svg\');
        }
         Remove any invalid XML tags as per http:validator.w3.org
        $svg = $svg.removeAttr(\'xmlns:a\');
         Replace image with new SVG
        $img.replaceWith($svg);
    });
});