from django.contrib import admin
from workflows.models import State
from workflows.models import StateInheritanceBlock
from workflows.models import StatePermissionRelation
from workflows.models import StateObjectRelation
from workflows.models import Transition
from workflows.models import Workflow
from workflows.models import WorkflowObjectRelation
from workflows.models import WorkflowModelRelation
from workflows.models import WorkflowPermissionRelation


class StateInline(admin.TabularInline):
    model = State


class WorkflowAdmin(admin.ModelAdmin):
    inlines = [
        StateInline,
    ]

admin.site.register(Workflow, WorkflowAdmin)


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'workflow', 'transitions_count')
    list_filter = ('workflow',)
    search_fields = ('name',)

    def transitions_count(self, object):
        return object.transitions.count()

admin.site.register(State, StateAdmin)


class StateInheritanceBlockAdmin(admin.ModelAdmin):
    list_display = ('state', 'permission')

admin.site.register(StateInheritanceBlock, StateInheritanceBlockAdmin)


class StateObjectRelationAdmin(admin.ModelAdmin):
    list_display = ('state', 'content_type', 'content_id')

admin.site.register(StateObjectRelation, StateObjectRelationAdmin)


class StatePermissionRelationAdmin(admin.ModelAdmin):
    list_display = ('state', 'role', 'permission')
    list_filter = ('role', 'state')

admin.site.register(StatePermissionRelation, StatePermissionRelationAdmin)


class TransitionAdmin(admin.ModelAdmin):
    list_display = ('name', 'destination', 'permission')
    list_filter = ('workflow', 'destination')
    search_fields = ('name',)

admin.site.register(Transition, TransitionAdmin)


class WorkflowObjectRelationAdmin(admin.ModelAdmin):
    list_display = ('workflow', 'content_type', 'content_id')
    list_filter = ('workflow',)

admin.site.register(WorkflowObjectRelation, WorkflowObjectRelationAdmin)


class WorkflowModelRelationAdmin(admin.ModelAdmin):
    list_display = ('workflow', 'content_type')
    list_filter = ('workflow', 'content_type')

admin.site.register(WorkflowModelRelation, WorkflowModelRelationAdmin)


class WorkflowPermissionRelationAdmin(admin.ModelAdmin):
    list_display = ('workflow', 'permission')
    list_filter = ('workflow',)

admin.site.register(
    WorkflowPermissionRelation, WorkflowPermissionRelationAdmin)
