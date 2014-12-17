/**
 * Created by Stepan on 06.12.14.
 */
$(document).ready(function(){
    var genitive = [
        "января", "февраля", "марта", "апреля", "мая", "июня", "июля",
        "августа", "сентября", "октября", "ноября", "декабря"
    ];

    //  Скрипты для карт
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

    // Скрипты для брони
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
        dateFormat: "yy-mm-dd",
        minDate: 0,
        maxDate: "+1M +10D",
        onSelect: function (date, inst) {
            var text = inst.selectedDay + " " + genitive[inst.selectedMonth] + " " + inst.selectedYear;
            $('.order-time-menu').dialog("open");
            $('[name=date]').val(inst.selectedYear+"-"+(inst.selectedMonth+1)+"-"+inst.selectedDay);
            $('.confirm .date').text(text).closest('.hidden').removeClass('hidden');
        }
    });

    $('.order-time-menu').dialog({
        autoOpen: false,
        title: 'Выберите время',
        width: 183,
        modal: true,
        open: function() {
            var date = $("#datepicker").datepicker({ dateFormat: 'dd-mm-yy' }).val();
            for (var i = 0; i < orders.length; i++) {
                if (
                    orders[i].fields.date == date &&
                        orders[i].fields.quest == $('.select-quest .order-quest.current').data("id")
                    ) {
                    $('.time-money .choice-time .row [data-time]').each(function(){
                        if ($(this).data('time') == orders[i].fields.time) {
                            $(this).closest('.row').addClass('disabled');
                        }
                    });
                }
            }
        },
        close: function() {
            $('.time-money .choice-time .row').removeClass('disabled');
        }
    });

    $('.time-money .row').click(function(){
        if ($(this).hasClass('disabled')) {
            return;
        }
        var $time = $(this).find('div:first');
        $('[name=time]').val($time.data('time'));
        $('.order-time-menu').dialog('close');
        $('.confirm .time').text($time.text()).closest('.hidden').removeClass('hidden');
    });

    $(".select-quest .order-quest").click(function(){
        $('.select-quest .order-quest.current').removeClass('current');
        $(this).addClass('current');
        $('[name=quest]').val($(this).data("id"));
        $('[name=time]').val("");
        var confirmTime = $('.confirm .time').closest('span');
        if (!confirmTime.hasClass('hidden')) {
            $('.confirm .time').closest('span').addClass('hidden');
        }
        $('.confirm .quest-name').text($(this).text());
    });

    $('#book').click(function(event){
        event.preventDefault();
        event.stopPropagation();
        var isEmpty = false;
        $('#quest-order-form input').each(function(){
            if ($.trim($(this).val()) == "") {
                isEmpty = true;
            }
        });
        if (isEmpty) {
            alert("Пожалуйста, заполните все поля");
            return;
        }
        $('#quest-order-form').ajaxSubmit({
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

    function init() {
        $('.select-quest .order-quest.current').trigger('click');
        $("#datepicker").find('.ui-datepicker-current-day').removeClass("ui-datepicker-current-day");
    }
    init();
});