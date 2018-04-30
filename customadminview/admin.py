from django.contrib import admin
from .models import BackendTeam
from django import forms
# Register your models here.

class BackendTeamForm(forms.ModelForm):

    team_member1 = forms.CharField()
    team_member2 = forms.CharField()
    team_member3 = forms.CharField()

    def save(self,commit=True):
        team_member1 = self.cleaned_data.get('team_member1',None)
        team_member2 = self.cleaned_data.get('team_member2',None)
        team_member3 = self.cleaned_data.get('team_member3',None)
        return super(BackendTeamForm, self).save(commit=commit)

        class Meta:
            model = BackendTeam

class BackendTeamAdmin(admin.ModelAdmin):
    form = BackendTeamForm

    fieldsets = (
        (None, {
            'fields': ('team_member1', 'team_member2', 'team_member3'),
        }),
    )

    def save_model(self,request,obj,form,change):
        print(obj,'11111',request.POST)
        obj.team_members = [request.POST["team_member1"],request.POST["team_member2"],request.POST["team_member3"]]
        super().save_model(request,obj,form,change)

    def get_form(self, request, obj=None, **kwargs):

        if obj:
            form = super(BackendTeamAdmin, self).get_form(request, obj, **kwargs)
            form.base_fields['team_member1'].initial = obj.team_members[0]
            form.base_fields['team_member2'].initial = obj.team_members[1]
            form.base_fields['team_member3'].initial = obj.team_members[2]
            return form
        else:
            form = super(BackendTeamAdmin, self).get_form(request, obj, **kwargs)
            form.base_fields['team_member1'].initial = ""
            form.base_fields['team_member2'].initial = ""
            form.base_fields['team_member3'].initial = ""
            return form

admin.site.register(BackendTeam,BackendTeamAdmin)
