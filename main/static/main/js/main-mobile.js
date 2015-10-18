/**
 * Created by Stepan on 05.10.15.
 */

var MobileSite = (function() {

	var $menu = $('.menu-open');

	function menuHandler() {
		if ($menu.hasClass('opened')) {
			$menu.removeClass('opened');
		} else {
			$menu.addClass('opened');
		}
	}

	function init() {
		$menu.on('click', menuHandler);
	}

	return {
		init: init
	};
}());

$(document).ready(function(){
	MobileSite.init();
});
