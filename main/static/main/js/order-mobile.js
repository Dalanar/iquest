/**
 * Created by Stepan on 12.10.15.
 */
var Order = (function(){
	var orders,
		schedule,
		isMobile,
		$datepicker;

	var genitive = [
        "января", "февраля", "марта", "апреля", "мая", "июня", "июля",
        "августа", "сентября", "октября", "ноября", "декабря"
    ];

	function selectQuestHandler(){
		datepickerInit();

        $('.select-quest .item.current').removeClass('current');
        $(this).addClass('current');
        $('[name=quest]').val($(this).data("id"));
        $('[name=time]').val("");
        $('.confirm .quest-name').text($(this).text());
		$datepicker.find('.ui-datepicker-current-day .ui-state-active').trigger('click');
    }

	function getTimesFromSchedule(date, quest) {
		for (var i = 0; i < schedule.length; i++) {
			if (
				schedule[i][2] == date[2] &&
				schedule[i][1] == date[1] &&
				schedule[i][0] == date[0]
			) {
				return schedule[i][4][quest];
			}
		}
	}

	function clickTimeCostHandler() {
        if ($(this).hasClass('disabled')) {
            return;
        }
		$('.time-cost .current').removeClass('current');
		$(this).addClass('current');
        var time = $(this).find('.time').text();
        $('[name=time]').val(time);
        var cost = $(this).find('.cost').text();
        $('[name=cost]').val(cost);

        $('.confirm .quest-time').text(time);
        $('.confirm .quest-cost').text(cost);
    }

	/**
	 * Рендер времени - цены для мобилок
	 */
	function renderTimeCost() {
		var date = $datepicker.datepicker({ dateFormat: 'yy-mm-dd' }).val();
		var date_arr = $.map(date.split('-'), function(el){
			return parseInt(el);
		});
		var $timeCostMenu = $('.time-cost .order-menu-content').empty();
		var currentQuest = $('.select-quest .item.current').data('id');
		$.each(
			getTimesFromSchedule(date_arr, currentQuest),
			function(index, value) {
				var text =
					'<div class="item">' +
						'<div class="time" >' + value.time + '</div>' +
						' - ' +
						'<div class="cost">' + value.cost + '</div>' +
					'</div>';
				$timeCostMenu.append(text);
			}
		);
		addDisabledTimes(date);
		$('.time-cost .item').click(clickTimeCostHandler);
	}

	function addDisabledTimes(date) {
		for (var i = 0; i < orders.length; i++) {
			if (
				orders[i].fields.date == date &&
				orders[i].fields.quest ==
					$('.select-quest .item.current').data("id")
			) {
				$('.time-cost .item').each(function(){
					if ($(this).find('.time').text() == orders[i].fields.time) {
						$(this).addClass('disabled');
					}
				});
			}
		}
	}

	function orderHandler(event) {
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
	}

	var datepickerInit = function() {
		$datepicker = $("#datepicker");
		$.datepicker.setDefaults($.extend($.datepicker.regional["ru"]));
		var datepickerData = {
			dateFormat: "yy-mm-dd",
			minDate: 0,
			maxDate: "+29d",
			onSelect: function (date, inst) {
				var text = inst.selectedDay + " " +
					genitive[inst.selectedMonth] + " " + inst.selectedYear;
				renderTimeCost();
				var strDate = inst.selectedYear + "-" + (inst.selectedMonth + 1) +
						"-" + inst.selectedDay;
				$('[name=date]').val(strDate);
				$('.confirm .quest-date').text(text);
				$('.confirm').find('.quest-time, .quest-cost').text('');
				$('[name=time]').val("");
        		$('[name=cost]').val("");
			}
		};
		datepickerData.dayNamesMin =
			['вc', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб'];
		datepickerData.nextText = "Later";
		$datepicker.datepicker(datepickerData);
	};

	function inputsKeypressHandler(event) {
		var $target = $(event.target);
		if ($target.val() != "") {
			$target.addClass("filled");
		} else {
			$target.removeClass("filled");
		}
	}

	var init = function(option1, option2, isMobileOpt) {
		orders = option1;
		schedule = option2;
		isMobile = isMobileOpt;
		$(".select-quest .order-menu-content .item").on('click', selectQuestHandler);
		$('#book').on('click', orderHandler);
		$('[name=name], [name=phone]').on('keypress', inputsKeypressHandler);
	};

	return {
		init: init
	};
})();