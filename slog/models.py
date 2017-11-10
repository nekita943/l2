from django.db import models
from users.models import DoctorProfile


class Log(models.Model):
    TYPES = (
        (0, 'Другое'),

        (1, 'Справочник: добавлена пробирка'),
        (2, 'Справочник: изменена пробирка'),
        (3, 'Справочник: добавлен анализ'),
        (4, 'Справочник: изменен анализ'),
        (20, 'Справочник: добавлено отношение пробирки к фракции'),
        (19, 'Справочник: скрытие/показ анализа'),
        (5, 'Справочник: добавлена группа направления'),
        (6, 'Справочник: изменена группа направления'),

        (21, 'Направления: созданы направления'),
        (5000, 'Направления: просмотр истории направления'),

        (9, 'Взятие материала: пробирка взята'),
        (10, 'Взятие материала: напечатан акт приёма-передачи'),

        (11, 'Приём материала: материал принят'),
        (12, 'Приём материала: материал не принят'),
        (4000, 'Приём материала: замечание приёма было очищено'),
        (25, 'Приём материала: печать журнала приема'),

        (13, 'Ввод результатов: результат сохранен'),
        (14, 'Ввод результатов: результат подтвержден'),
        (15, 'Ввод результатов: результаты для направления напечатаны'),
        (24, 'Ввод результатов: подтверждение сброшено'),
        (26, 'Ввод результатов: присвоение УЕТов'),
        (28, 'Ввод результатов: печать журнала-таблицы'),

        (16, 'Администрирование: создан пользователь'),
        (17, 'Администрирование: создано подразделение'),

        (18, 'Пользователи: вход пользователя'),

        (27, 'Поиск: поиск'),

        (22, 'API: результат сохранен'),
        (23, 'API: пробирка не найдена'),

        (100, 'Статистика: statistic_xls'),

        (998, 'Подозрительное действие: печать результатов другого врача и/или отделения и/или лаборатории'),
        (999, 'Подозрительное действие: печать результатов другого отделения'),

        (1000, 'Выписки: загрузка выписки'),
        (1001, 'Выписки: поиск'),

        (2000, 'Импорт пациентов: добавление Individual в базу'),
        (2000, 'Импорт пациентов: добавление карты пациента в базу'),

        (3001, 'РМИС: повторная отправка направлений'),
        (3000, 'РМИС: повторная отправка результатов'),
    )
    key = models.CharField(max_length=2047)
    type = models.IntegerField(choices=TYPES)
    body = models.TextField()
    user = models.ForeignKey(DoctorProfile)
    time = models.DateTimeField(auto_now=True)

    @staticmethod
    def get_client_ip(request):
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
