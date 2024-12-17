from django.http import StreamingHttpResponse, JsonResponse
from .models import Event
import json
import time

def stream_events(request):
    def event_generator():
        while True:
            event = Event.objects.create(metric="temperature", value=25.6)
            yield f"data: {json.dumps({'timestamp': event.timestamp.isoformat(), 'metric': event.metric, 'value': event.value})}\n\n"
            time.sleep(1)  # Adjust interval here

    return StreamingHttpResponse(event_generator(), content_type='text/event-stream')

def event_history(request):
    limit = int(request.GET.get('limit', 10))
    events = Event.objects.all().order_by('-timestamp')[:limit]
    data = [{"timestamp": e.timestamp, "metric": e.metric, "value": e.value} for e in events]
    return JsonResponse(data, safe=False)
