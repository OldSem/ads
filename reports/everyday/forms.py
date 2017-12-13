# -*- coding: utf-8 -*-
from django import forms
from .models import personel
from .models import DTE

class personelForm(forms.ModelForm):

     class Meta:
         model = personel
         fields = ('Name', 'Position',)



class DTEForm(forms.ModelForm):
    class Meta:

        model = DTE

        fields = ('work','ESN','adress','rezult','executor','elapsed_time','note',)
        labels = {'work':u'Вид работ','ESN':u'Номер ЕСР/Код УЧН','adress':u'Адресс объекта','rezult':u'Результат','executor':u'Исполнитель','elapsed_time':u'Затраченное время','note':u'Примечание'}
        values = {"save":u'Добавить'}
