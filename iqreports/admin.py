from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from iqreports.models import *
from iqreports.forms import ReportForm
from django.shortcuts import render
from django.db import connection


class ReportAdmin(ModelAdmin):
    """
    Модуль для отчетов в админке
    """

    def count_quest_order(self, map):
        """ Метод для рассчета статистики для бронирования квестов """
        cursor = connection.cursor()
        cursor.execute(
            "SELECT COUNT(*), SUM(mqo.cost) "
            "FROM main_questorder mqo "
            "INNER JOIN main_quest mq ON mq.id = mqo.quest_id "
            "WHERE mqo.date BETWEEN %(startDate)s AND %(endDate)s "
            "AND mq.branch_id = %(branch)s"
            ,
            map
        )
        quest_data = cursor.fetchone()
        result = {}
        result['quest_count'] = quest_data[0]
        result['quest_sum'] = 0 if quest_data[1] is None else quest_data[1]
        return result

    def count_cards(self, map):
        """ Метод для рассчета статистики для подарочных карт"""
        cursor = connection.cursor()
        cursor.execute(
            "SELECT COUNT(*), SUM(IF(gc.status = 4, 1, 0)) "
            "FROM main_giftcard gc "
            "WHERE gc.activated_time BETWEEN %(startDate)s AND %(endDate)s "
            "AND gc.branch_id = %(branch)s"
            ,
            map
        )
        gift_data = cursor.fetchone()
        result = {}
        result['gift_count'] = gift_data[0]
        result['gift_activated_count'] = 0 if gift_data[1] is None else gift_data[1]
        return result

    def count_form(self, data):
        """ Рассчет форм """
        map = {'branch': data['branch'], 'startDate': data['startDate'],
               'endDate': data['endDate']}
        data_order = self.count_quest_order(map)
        data_card = self.count_cards(map)
        data_order.update(data_card)
        return data_order

    def changelist_view(self, request, extra_context=None):
        form = ReportForm()
        counts = False
        if request.method == 'POST':
            form = ReportForm(request.POST)
            if form.is_valid():
                counts = self.count_form(form.data)
        return render(
            request,
            'iqreports/report.html',
            {
                'form': form,
                'counts': counts
            }
        )

    def has_change_permission(self, request, obj=None):
        #obj==None при проверке доступа к списку объектов
        #какой-то конкретный объект нам редактировать не нужно
        return not bool(obj)

    def has_add_permission(self, request):
        #добавлять ничего нам не нужно
        return False

    def has_delete_permission(self, request, obj=None):
        #и удалять...
        return False

admin.site.register(Report, ReportAdmin)