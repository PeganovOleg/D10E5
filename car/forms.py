from django import forms  
from p_library.models import Author, Book  
from django.forms import formset_factory  
from p_library.models import UserProfile



<form action="{% url "main" %}">
    <input type="text" name="manufacturer" placeholder="производитель">
    <input type="text" name="model" placeholder="модель">
    <input type="number" name="year" placeholder="год выпуска">
    <select name="kpp">
      <option value="" selected>Выберите коробку передач</option>
      <option value="0">Механика</option>
      <option value="1">Автомат</option>
      <option value="2">Робот</option>
    </select>
    <input type="text" name="color" placeholder="цвет">
    <input type="submit">
</form>