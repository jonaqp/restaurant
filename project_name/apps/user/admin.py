from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from django.utils.translation import ugettext_lazy as _

from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreationForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """A form for updating users. Includes all the fields on
    the user, but replaces the password field with admin's
    password hash display field.
    """
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'isActive', 'isAdmin')

    def clean_password(self):
        return self.initial["password"]


class MyUserAdmin(UserAdmin):
    list_per_page = 3
    date_hierarchy = 'last_login'
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'isAdmin', 'last_login')
    list_filter = ('isAdmin',)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    fieldsets = (
        (None, {'fields': ('email', 'password', 'isAdmin')}),
        (_('Personal Detail'), {'fields': ('firstName', 'lastName')}),
        (_('Permissions'), {'fields': ('isActive', 'isAdmin')}),
        (_('Rol System'), {'fields': ('groupId', 'roleId')}),
        (_('Important dates'), {'fields': ('last_login',)}),

    )
    filter_horizontal = ()
    search_fields = ('email',)
    ordering = ('last_login',)


admin.site.register(User, MyUserAdmin)
admin.site.unregister(Group)
