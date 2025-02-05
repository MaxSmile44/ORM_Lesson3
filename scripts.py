from random import choice

from datacenter.models import Chastisement
from datacenter.models import Commendation
from datacenter.models import Lesson
from datacenter.models import Mark
from datacenter.models import Schoolkid


def fix_marks(child):
    """Изменить оценки с двоек и троек на пятерки.

    Args:
        child (str): ФИО ученика.

    Returns:
        На сайте меняются оценки.
        Если количество найденных учеников отличается от одного, то выходит соответствующее уведомление.
    """
    try:
        child = Schoolkid.objects.get(full_name__contains = child)
    except Schoolkid.DoesNotExist:
        print('Записей не найдено')
        return
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено больше одной записи')
        return
    new_point = Mark.objects.filter(schoolkid = child, points__in=[2,3])
    new_point.update(points = 5)
    return


def remove_chastisements(child):
    """Удалить записи с замечанием от учителя ученику.

    Args:
        child (str): ФИО ученика.

    Returns:
        На сайте удаляются все записи с замечаниями ученика.
        Если количество найденных учеников отличается от одного, то выходит соответствующее уведомление.
    """
    try:
        child = Schoolkid.objects.get(full_name__contains = child)
    except Schoolkid.DoesNotExist:
        print('Записей не найдено')
        return
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено больше одной записи')
        return
    chastisement = Chastisement.objects.filter(schoolkid = child)
    chastisement.delete()
    return


def create_commendation(child, subject):
    """Создать поддельную запись с похвалой от учителя ученику.

    Args:
        child (str): ФИО ученика.
        subject (str): Название предмета.

    Returns:
        На сайте появляется похвала от учителя.
        Если количество найденных учеников отличается от одного, то выходит соответствующее уведомление.
        Если название предмета указано неверно, то выходит соответствующее уведомление.
    """
    try:
        child = Schoolkid.objects.get(full_name__contains = child)
    except Schoolkid.DoesNotExist:
        print('Записей не найдено')
        return
    except Schoolkid.MultipleObjectsReturned:
        print('Найдено больше одной записи')
        return
    lesson_date = Lesson.objects.filter(year_of_study=child.year_of_study, group_letter=child.group_letter, subject__title=subject).last()
    if not lesson_date:
        raise AttributeError('Название урока введено некорректно')
    praise = [
        'Отлично!',
        'Молодец!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!'
    ]
    text = choice(praise)
    Commendation.objects.create(text=text, created=lesson_date.date, schoolkid=child, subject=lesson_date.subject, teacher=lesson_date.teacher)
    return
