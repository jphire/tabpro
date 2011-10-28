from mytab.main.models import *
from django.contrib import admin

class AppartmentInline(admin.StackedInline):
    model = Appartment
    extra = 2
    fields = ['stair', 'appartment_number']
    #readonly_fields = ['appartment_number', 'stair']
    

class HabitantInline(admin.StackedInline):
    model = Habitant
    extra = 0
#    fieldsets = [
#                 ('Habitants', {'fields': ('last_name', 'social_security')}), 
#                 ]
    
class HouseAdmin(admin.ModelAdmin):
    
    #list_display = ('road', 'number')
    list_filter = ['road','number']
    search_fields = ['road', 'number']
    fieldsets = [
                 (None, {'fields': ['road', 'number']}),
                  ('Real-estate Agent', {'fields': ['real_estate_agency'], 'classes':['collapse']})
                 ]
    inlines = [AppartmentInline]
    class Media:
        js = ['js/jquery-1.6.4.js', 'js/collapsed-stacked-inline.js',]
    

class HabitantAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
#    fieldsets = [
#                 ('Habitants', {'fields': ('first_name', 'last_name', 'social_security')}), 
#                 ]
    
class AppartmentAdmin(admin.ModelAdmin):
    inlines = [HabitantInline]
    search_fields = ['house__road', 'house__number', 'stair', 'appartment_number']
    fieldsets = [ 
                  (None, {'fields': ['house', 'stair', 'appartment_number']}),
                  #('Habitants', {'fields': ['first_name'], 'classes':['collapse']})
                  ]
    class Media:
        js = ['js/jquery-1.6.4.js', 'js/collapsed-stacked-inline.js',]
    
class KeyAdmin(admin.ModelAdmin):
    pass
    #fields = ['appartment', 'owner', 'key_id']

class WorkOrderAdmin(admin.ModelAdmin):
    search_fields = ['creator', 'finisher', 'order_made_date']
    date_hierarchy = 'order_made_date'


admin.site.register(House, HouseAdmin)
admin.site.register(Habitant, HabitantAdmin)
admin.site.register(Key, KeyAdmin)
admin.site.register(Appartment, AppartmentAdmin)
admin.site.register(Employee)
admin.site.register(TargetOfReservation)
admin.site.register(WorkOrder, WorkOrderAdmin)
admin.site.register(Reservation)