from tests.test_setup import TestSetup
from tests.apps.event.factories.event_factories import EventFactory
from apps.event.models import Event

class EventTestCase(TestSetup):
    url = 'http://localhost:8000/api/v1/event'

    def test_list_events(self):
        event_1 = EventFactory().create_event()
        event_2 = EventFactory().create_event()

        response = self.client.get(self.url, format='json', follow=True)
        print(response)
        # self.assertEqual(Event.objects.all().count(), len(response.data))
        
