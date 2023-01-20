from rest_framework import permissions
from Authentication.models import SportCoordinatorRole, EventCoordinatorRole, UniversityCoordinatorRole, TeamCoordinatorRole

class IsSportCoordinator(permissions.BasePermission):
    """
    Allows access only to coordinators for a given sport.
    """

    def has_permission(self, request, view):
        sport = request.data.get('sport')
        user = request.user
        role = SportCoordinatorRole.objects.get(person=user.id, sport=sport)
        return role.exists()

class IsEventCoordinator(permissions.BasePermission):
    """
    Allows access only to event coordinators.
    """

    def has_permission(self, request, view):
        event = request.data.get('event')
        user = request.user
        print(user)
        role = EventCoordinatorRole.objects.get(person=user.id, event=event)
        return role.exists()

class IsUniversityCoordinator(permissions.BasePermission):
    """
    Allows access only to university coordinators.
    """

    def has_permission(self, request, view):
        university = request.data.get('university')
        user = request.user
        role = UniversityCoordinatorRole.objects.get(person=user.id, university=university)
        return role.exists()

class IsTeamCoordinator(permissions.BasePermission):
    """
    Allows access only to team coordinators.
    """

    def has_permission(self, request, view):
        team = request.data.get('team')
        user = request.user
        role = TeamCoordinatorRole.objects.get(person=user.id, team=team)
        return role.exists()

class AdminRole(permissions.BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        return request.user.is_superuser

class ReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        print('request.method: ' + request.method)
        return request.method in permissions.SAFE_METHODS