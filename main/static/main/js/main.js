/**
 * Created by Stepan on 06.12.14.
 */
$(document).ready(function(){
    $('#submit-card-form').click(function(event){
        event.preventDefault();
        event.stopPropagation();
        var isEmpty = false;
        $('#card-form input').each(function(){
            if ($.trim($(this).val()) == "") {
                isEmpty = true;
            }
        });
        if (isEmpty) {
            alert("Пожалуйста, заполните все поля");
            return;
        }
        $('#card-form').ajaxSubmit({
            success: function() {
                alert('Ваша заявка принята');
                $('#card-form input').each(function(){
                    $(this).val("");
                });
            },
            error: function() {
                alert('Произошла ошибка');
            }
        });
    });

   	$('.gallery .main-image > a').magnificPopup({
		type: 'image',
		closeOnContentClick: true
	});

    $('.popup-gallery').magnificPopup({
		delegate: 'a',
		type: 'image',
		tLoading: 'Loading image #%curr%...',
		mainClass: 'mfp-img-mobile',
		gallery: {
			enabled: true,
			navigateByImgClick: true,
			preload: [0,1] // Will preload 0 - before current, and 1 after the current image
		}
	});

    $.datepicker.setDefaults($.extend($.datepicker.regional["ru"]));
    $("#datepicker").datepicker({
        minDate: 0,
        maxDate: "+1M +10D",
        onSelect: function (date) {
            $('.order-time-menu').dialog("open");
            $('[name=date]').val(date);
        }
    });
    $("#datepicker").find('.ui-datepicker-current-day').removeClass("ui-datepicker-current-day");

    $('.order-time-menu').dialog({
        autoOpen: false,
        title: 'Выберите время',
        width: 183,
        modal: true
    });

    $('.time-money .row').click(function(){
        var time = $(this).find('div:first').data('time');
        $('[name=time]').val(time);
        $('.order-time-menu').dialog('close');
        checkConfirm();
    });

    $(".select-quest .order-quest").click(function(){
        $('.select-quest .order-quest.current').removeClass('current');
        $(this).addClass('current');
        $('[name=quest]').val($(this).data('id'));
        checkConfirm();
    });

    function checkConfirm() {
        $('.confirm .quest-name').text($('.select-quest .order-quest.current').text())
        $('.confirm .quest-date').text($('[input=date]').val());
        $('.confirm .quest-time').text($('[input=time]').val());
    }
});

checkConfirm();
