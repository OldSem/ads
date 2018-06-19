# -*- coding: utf-8 -*-
from django import forms
from .models import Tags
from .models import Ads

#class personelForm(forms.ModelForm):

     #class Meta:
        # model = personel
         #fields = ('Name', 'Position',)


class FilterForm(forms.ModelForm):

        activ = forms.ChoiceField(widget=forms.RadioSelect, choices=(('True', u'Активные',), ('False', u'Неактивные',)))
 #       tegs = forms.MultipleChoiceField(required=False,widget=forms.CheckboxSelectMultiple,choices=Tags.objects.values_list('Teg'))

        start_date = forms.DateField(widget=forms.SelectDateWidget())
        stop_date = forms.DateField(widget=forms.SelectDateWidget())
        text_content = forms.CharField()
        class Meta:
            model = Ads

            fields = ('tegs','activ')
            labels = {'tegs': u'Тэги','activ':u'Время жизни'}




class AdForm(forms.ModelForm):
    text_content = forms.CharField()
    class Meta:

        model = Ads

        fields = ('tegs','activ','text','phone')
        labels = {'tegs':u'Тэги','activ':u'Время жизни','text':u'Текст объявления','phone':u'Телефон'}
        values = {"save":u'Добавить'}
