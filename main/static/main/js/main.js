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
        maxDate: "+1M",
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
            var date = $("#datepicker").datepicker('getDate');
            var dayOfWeek = date.getUTCDay();
            var $choiceTime = $('.order-time-menu .choice-time').empty();
            $.each(schedule[dayOfWeek], function(index, value) {
                $choiceTime.append('<div class="row"><div class="time" >' + value.time + '</div><div class="cost">' + value.cost + '</div></div>');
            });
            date = $("#datepicker").datepicker({ dateFormat: 'dd-mm-yy' }).val();
            for (var i = 0; i < orders.length; i++) {
                if (
                    orders[i].fields.date == date &&
                        orders[i].fields.quest == $('.select-quest .order-quest.current').data("id")
                    ) {
                    $('.time-money .choice-time .row .time').each(function(){
                        if ($(this).text() == orders[i].fields.time) {
                            $(this).closest('.row').addClass('disabled');
                        }
                    });
                }
            }
            $('.time-money .row').click(clickTimeCostHandler);
        },
        close: function() {
            $('.time-money .choice-time .row').removeClass('disabled');
        }
    });

    function clickTimeCostHandler() {
        if ($(this).hasClass('disabled')) {
            return;
        }
        var time = $(this).find('.time').text();
        $('[name=time]').val(time);
        var cost = $(this).find('.cost').text();
        $('[name=cost]').val(cost);
        $('.confirm .time').text(time).closest('.hidden').removeClass('hidden');
        $('.order-time-menu').dialog('close');
    }

    $(".select-quest .order-quest").click(function(){
        $('.select-quest .order-quest.current').removeClass('current');
        $(this).addClass('current');
        $('[name=quest]').val($(this).data("id"));
        $('[name=time]').val("");
        var confirmTime = $('.confirm .time').parents('span');
        if (!confirmTime.hasClass('hidden')) {
            confirmTime.addClass('hidden');
        }
        $('.confirm .quest-name').text($(this).text());
    });

    $('#book').click(function(event){
        event.preventDefault();
        event.stopPropagation();
        var error = null;
        $('#quest-order-form input').each(function(){
            if ($.trim($(this).val()) == "") {
                error = "Пожалуйста, заполните все поля";
                return;
            }
            var value = $(this).val();
            if (
                $(this).is('[name=name]') &&
                    (
                        value.length < 3 ||
                        !/^[а-яёА-ЯЁ0-9 ]+$/.test(value)
                    )
            ) {
                error = 'Некоректно заполнено имя';
                return;
            }
            if (
                $(this).is('[name=phone]') &&
                    (
                        value.length < 5 ||
                        !/^[0-9\+\- ]+$/.test(value)
                    )
            ) {
                error = 'Некоректно заполнен телефон';
                return;
            }
            if (
                $(this).is('[name=email]') && !validateEmail(value)
            ) {
                error = 'Некоректно заполнен email';
                return;
            }
        });
        if (error) {
            alert(error);
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

    function validateEmail(email) {
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
    }
    init();
});