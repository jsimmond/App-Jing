from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
import json

from Person.models import Person
from Sport.models import Sport
from University.models import University
from University.serializers import UniversitySerializer

from Administration.models import Log
from Administration.serializers import LogSerializer
from Person.serializers import PersonSerializer
from Placement.permissions import AdminRole, TeamCoordinatorRole, EventCoordinatorRole, UniversityCoordinatorRole, SportCoordinatorRole


class LogViewSet(ModelViewSet):
    serializer_class = LogSerializer
    queryset = Log.objects.all()


class AdminPanelView(APIView):
    permission_classes = [AdminRole | TeamCoordinatorRole | EventCoordinatorRole | UniversityCoordinatorRole | SportCoordinatorRole]

    def get(self, request):

        person = None
        people = PersonSerializer(Person.objects.all(), many=True)
        # events = EventSerializer(Event.objects.all(), many=True)
        universities = UniversitySerializer(
            University.objects.all(), many=True)
        # locations = LocationSerializer(Location.objects.all(), many=True)
        # sports = SportSerializer(Sport.objects.all(), many=True)
        sport_types = Sport.SPORT_TYPE
        genders = Sport.SPORT_GENDER
        # sport_coords = PersonSerializer(Person.objects.filter(is_sports_coordinator=True))
        # unis_coords = PersonSerializer(Person.objects.filter(is_university_coordinator=True))

        if request.user.is_authenticated:
            if Person.objects.filter(user=request.user).exists():
                person = PersonSerializer(Person.objects.get(user=request.user))
                

        data = {
            "name": request.user.username,
            "people": people,
            # "events": events,
            "universities": universities.data,
            # "locations": locations,
            "person": person,
            # "sports": sports,
            "sport_types": sport_types,
            "genders": genders,
            "permissions" : request.user.get_all_permissions(),
            # "sports_coords": sport_coords,
            # "unis_coords": unis_coords,
            # "alert": request.session.pop('alert', None)
        }
        print(data["permissions"])
        print(data)
        return Response(data)

# Assume the data HAS the username and password data and correct format
# In the future, AdminCreatePerson (called in create-user url) can call this function
# Or, this function can call AdminCreatePerson method
# This function is especially design for the upload of people from a csv file

def _uploadPersonData( request ):
    file = request.FILES['file']
    data = json.loads(file.read())
    print(data)
    if data:
        for person in data:
            if not Person.objects.filter(rut=person['rut']).exists():
                username = str(person['nombre']).lower() + '.' + str(person['apellido']).lower()
                password = str(person['rut']).split('-')[0]
                p = Person.objects.create_user(username , person['email'], password)
                p.name = person['nombre']
                p.last_name = person['apellido']
                p.rut = person['rut']
                p.university = person['universidad']
                p.phone_number = person['telefono']
                p.emergency_phone_number = person['telefono emergencia']
                p.save()