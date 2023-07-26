from faker import Faker
from apps.event.models import Event, EventType, EventStatus

faker = Faker()

class EventFactory:

    def build_event_type_JSON(self):
        event_type = ['Evento tipo 1', 'Evento tipo 2', 'Evento tipo 3']
        return {
            'name': faker.random_element(elements=event_type)
        }

    def build_event_status_JSON(self):
        event_status = ['Pendiente', 'Revisado']
        return {
            'name': faker.random_element(elements=event_status)
        }

    def build_event_JSON(self):
        event_type = self.create_event_type()
        event_status = self.create_event_status()
        return {
            'description': faker.description(),
            'date': faker.date_this_decade()
            'management': faker.random_element(elements=(True, False)),
            'type': event_type,
            'status': event_status
        }

    def create_event_type():
        return EventType.objects.create(**self.build_event_type_JSON())

    def create_event_status():
        return EventStatus.objects.create(**self.build_event_status_JSON())

    def create_event():
        return Event.objects.create(**self.build_event_JSON())