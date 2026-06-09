from django.db import models


class CooperativeInfo(models.Model):
    name = models.CharField('Название', max_length=200, default='ГСК «Камовец»')
    tagline = models.CharField('Подзаголовок', max_length=300, blank=True)
    short_description = models.TextField('Краткое описание (для главной)')
    full_description = models.TextField('Полное описание')
    address = models.CharField('Адрес', max_length=300)
    established_year = models.CharField('Год основания', max_length=10, blank=True)
    total_garages = models.CharField('Количество гаражей', max_length=50, blank=True)
    working_hours = models.CharField('Часы работы', max_length=200, blank=True)

    class Meta:
        verbose_name = 'Информация о кооперативе'
        verbose_name_plural = 'Информация о кооперативе'

    def __str__(self):
        return self.name


class ImportantInfo(models.Model):
    meetings_schedule = models.TextField('Расписание собраний')
    fee_amount = models.CharField('Размер членского взноса', max_length=100)
    fee_period = models.CharField('Периодичность оплаты', max_length=100)
    fee_payment_info = models.TextField('Как и где платить взносы')
    extra_info = models.TextField('Дополнительная информация', blank=True)

    class Meta:
        verbose_name = 'Важная информация'
        verbose_name_plural = 'Важная информация'

    def __str__(self):
        return 'Важная информация'


class Contact(models.Model):
    name = models.CharField('ФИО', max_length=200)
    role = models.CharField('Должность', max_length=200)
    phone = models.CharField('Телефон', max_length=50, blank=True)
    email = models.EmailField('Email', blank=True)
    note = models.CharField('Примечание', max_length=200, blank=True)
    order = models.PositiveIntegerField('Порядок отображения', default=0)

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'
        ordering = ['order']

    def __str__(self):
        return f'{self.role} — {self.name}'


class Document(models.Model):
    CATEGORY_CHOICES = [
        ('charter', 'Устав и учредительные документы'),
        ('protocol', 'Протоколы собраний'),
        ('regulation', 'Положения и правила'),
        ('other', 'Прочие документы'),
    ]
    title = models.CharField('Название документа', max_length=300)
    category = models.CharField('Категория', max_length=50, choices=CATEGORY_CHOICES, default='other')
    url = models.URLField('Ссылка на документ (Яндекс.Диск или другое)')
    date = models.DateField('Дата документа')
    description = models.TextField('Описание', blank=True)
    is_published = models.BooleanField('Опубликован', default=True)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'
        ordering = ['-date']

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField('Заголовок', max_length=300)
    content = models.TextField('Текст новости')
    date = models.DateField('Дата публикации', auto_now_add=True)
    is_published = models.BooleanField('Опубликована', default=True)

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-date']

    def __str__(self):
        return self.title


class WorkReport(models.Model):
    title = models.CharField('Заголовок', max_length=300)
    period = models.CharField('Период (напр. «2024 год» или «Лето 2024»)', max_length=100)
    content = models.TextField('Описание выполненных работ')
    date = models.DateField('Дата отчёта')

    class Meta:
        verbose_name = 'Отчёт о работах'
        verbose_name_plural = 'Отчёты о работах'
        ordering = ['-date']

    def __str__(self):
        return f'{self.title} ({self.period})'


class FinancialReport(models.Model):
    title = models.CharField('Заголовок', max_length=300)
    period = models.CharField('Период', max_length=100)
    content = models.TextField('Содержание отчёта (статьи доходов и расходов)')
    url = models.URLField('Ссылка на полный документ (Яндекс.Диск)', blank=True)
    date = models.DateField('Дата отчёта')
    income = models.DecimalField('Доходы (руб.)', max_digits=12, decimal_places=2, null=True, blank=True)
    expenses = models.DecimalField('Расходы (руб.)', max_digits=12, decimal_places=2, null=True, blank=True)

    class Meta:
        verbose_name = 'Финансовый отчёт'
        verbose_name_plural = 'Финансовые отчёты'
        ordering = ['-date']

    def __str__(self):
        return f'{self.title} ({self.period})'
