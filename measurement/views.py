from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Sensor, Measurement
from .serializers import SensorSerializers, MesurementSerializers

class SensorView(APIView):
    def get(self,request,id=None):

        if id:
            try:
                sensor = Sensor.objects.get(id=id)
            except:
                return Response('Not found')
            ser = SensorSerializers(sensor)
            return Response(ser.data)

        sensors = Sensor.objects.all()
        ser = SensorSerializers(sensors,many = True)
        return Response(ser.data)
    
    def post(self,request):

        name = request.data.get('name')
        description = request.data.get('description')
        db = Sensor(name=name,description=description)
        db.save()
        return Response('ok')
    
    def patch(self,request,id):

        name = request.data.get('name')
        description = request.data.get('description')

        try:
            db = Sensor.objects.get(id=id)
        except:
            return Response('Not found')
        if name:
            db.name = name
        if description:
            db.description = description

        db.save()
        return Response('ok')
    
    def delete(self,request,id):

        try:
            db = Sensor.objects.get(id=id)
        except:
            return Response('Not found')
        db.delete()
        return Response('ok')

class MeasurementView(APIView):
    def get(self,request,id=None):
        if id:
            try:
                measurement = Measurement.objects.get(id=id)
            except:
                return Response('id not found')
            ser = MesurementSerializers(measurement)
            return Response(ser.data)

        measurements = Measurement.objects.all()
        ser = MesurementSerializers(measurements,many=True)
        return Response(ser.data)

    def post(self,request):
        try:
            sensor = Sensor.objects.get(id = int(request.data.get('sensor')))
        except:
            return Response('id sensor not found')
        temperature = request.data.get('temperature')
        db = Measurement(sensor=sensor,temperature=temperature)
        db.save()
        return Response('ok')

    def patch(self,request,id):

        pass

    def delete(self,request,id):

        pass