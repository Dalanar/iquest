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

	// Костыль, убираем текущий день, чтоб пользователь кликнул и
	// увидел диалог
	function removeCurrentDate() {
		$datepicker
			.find('.ui-datepicker-current-day')
			.removeClass('ui-datepicker-current-day');
	}

	function selectQuestHandler(){
		$datepicker.datepicker('option', 'minDate', 0);
		if (!isMobile) {
			$datepicker.datepicker("setDate", null);
			removeCurrentDate();
		}
        $('.select-quest .order-quest.current').removeClass('current');
        $(this).addClass('current');
        $('[name=quest]').val($(this).data("id"));
        $('[name=time]').val("");
        var confirmTime = $('.confirm .time').parents('span');
        if (!confirmTime.hasClass('hidden')) {
            confirmTime.addClass('hidden');
        }
        $('.confirm .quest-name').text($(this).text());
		if (isMobile) {
			renderTimeCost();
		}
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
        var time = $(this).find('.time').text();
        $('[name=time]').val(time);
        var cost = $(this).find('.cost').text();
        $('[name=cost]').val(cost);
        $('.confirm .time').text(time).closest('.hidden').removeClass('hidden');
        $('.order-time-menu').dialog('close');
    }

	/**
	 * Рендер времени - цены для мобилок
	 */
	function renderTimeCost() {
		var date = $datepicker.datepicker({ dateFormat: 'yy-mm-dd' }).val();
		var date_arr = $.map(date.split('-'), function(el){
			return parseInt(el);
		});
		var $col1 = $('.time-cost .col1').empty();
		var $col2 = $('.time-cost .col2').empty();
		var currentQuest = $('.order-quest.current').data('id');
		$.each(
			getTimesFromSchedule(date_arr, currentQuest),
			function(index, value) {
				var text =
					'<label class="row">' +
						'<div class="time" >' + value.time + '</div> ' +
						'<div class="cost">' + value.cost + '</div>' +
						'<input type="radio" name="cost-radio"/>' +
					'</label>';
				if (index % 2 == 0) {
					$col1.append(text);
				} else {
					$col2.append(text);
				}
			}
		);
		addDisabledTimes(date);
		$('.time-cost .row').click(clickTimeCostHandler);
	}

	/**
	 * Цена-время в диалоге для десктопов
	 */
	function setupTimeCostDialog() {
		$('.order-time-menu').dialog({
			autoOpen: false,
			title: 'Выберите время',
			width: 183,
			modal: true,
			open: function() {
				var date =
					$("#datepicker").datepicker({ dateFormat: 'yy-mm-dd' }).val();
				var date_arr = $.map(date.split('-'), function(el){
					return parseInt(el);
				});
				var $choiceTime = $('.order-time-menu .choice-time').empty();
				var currentQuest = $('.order-quest.current').data('id');
				currentQuest--;
				$.each(
					getTimesFromSchedule(
						date_arr,
						currentQuest
					),
					function(index, value) {
						$choiceTime.append(
							'<div class="row">' +
								'<div class="time" >' + value.time + '</div>' +
								'<div class="cost">' + value.cost + '</div>' +
							'</div>'
						);
					}
				);
				addDisabledTimes(date);
				$('.time-money .row').click(clickTimeCostHandler);
			},
			close: function() {
				$('.time-money .choice-time .row').removeClass('disabled');
			}
		});
	}

	function addDisabledTimes(date) {
		for (var i = 0; i < orders.length; i++) {
			if (
				orders[i].fields.date == date &&
				orders[i].fields.quest ==
					$('.select-quest .order-quest.current').data("id")
			) {
				$('.time-money .choice-time .row .time, .time-cost .row .time').each(function(){
					if ($(this).text() == orders[i].fields.time) {
						$(this).closest('.row')
							.addClass('disabled')
							.find('input')
							.prop('disabled', true);
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
            if ($(this).is('[name=email]') && !validateEmail(value)) {
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
	}

    function validateEmail(email) {
        var re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
    }

	var init = function(option1, option2, isMobileOpt) {
		orders = option1;
		schedule = option2;
		isMobile = isMobileOpt;
		$datepicker = $("#datepicker");
		$.datepicker.setDefaults($.extend($.datepicker.regional["ru"]));
		var datepickerData = {
			dateFormat: "yy-mm-dd",
			minDate: 0,
			maxDate: "+29d",
			onSelect: function (date, inst) {
				var text = inst.selectedDay + " " +
					genitive[inst.selectedMonth] + " " + inst.selectedYear;
				if (isMobile) {
					renderTimeCost();
				} else {
					$('.order-time-menu').dialog("open");
				}
				$('[name=date]').val(
					inst.selectedYear + "-" + (inst.selectedMonth + 1) +
						"-" + inst.selectedDay
				);
				$('.confirm .date')
					.text(text)
					.closest('.hidden')
					.removeClass('hidden');
			}
		};
		if (isMobile) {
			datepickerData.dayNamesMin =
				['вc', 'пн', 'вт', 'ср', 'чт', 'пт', 'сб'];
			datepickerData.nextText = "Later";
		}
		$datepicker.datepicker(datepickerData);
		$(".select-quest .order-quest").on('click', selectQuestHandler);
		$('.select-quest .order-quest.current').trigger('click');
		if (isMobile) {
			$('.ui-datepicker-current-day .ui-state-active').trigger('click');
		} else {
        	removeCurrentDate();
			setupTimeCostDialog();
		}
		$('#book').on('click', orderHandler);
	};

	return {
		init: init
	};
})();