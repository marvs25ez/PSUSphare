from django.contrib import admin
# Register your models here.
from .models import College, program, Organization, Student, OrgMember
admin.site.register(College)
admin.site.register(program)
admin.site.register(Organization)
admin.site.register(Student)
admin.site.register(OrgMember)


