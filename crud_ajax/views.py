from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from .models import CrudUser, t_calls, t_staff, t_dict
from django.views.generic import TemplateView, View, DeleteView
from django.core import serializers
from django.http import JsonResponse

# view front page
class CrudView(TemplateView):
    template_name = 'crud_ajax/crud.html'
    def get_context_data(self, **kwargs):
        context = {}
        context['users'] = CrudUser.objects.all()
        return context
 

class CreateCrudUser(View):
    def  get(self, request):
        # form text fields
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.create(
            name = name1,
            address = address1,
            age = age1
        )

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class DeleteCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        CrudUser.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)


class UpdateCrudUser(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        name1 = request.GET.get('name', None)
        address1 = request.GET.get('address', None)
        age1 = request.GET.get('age', None)

        obj = CrudUser.objects.get(id=id1)
        obj.name = name1
        obj.address = address1
        obj.age = age1
        obj.save()

        user = {'id':obj.id,'name':obj.name,'address':obj.address,'age':obj.age}

        data = {
            'user': user
        }
        return JsonResponse(data)

class CallsView(TemplateView):
    template_name = 'calls.html'
    def get_context_data(self, **kwargs):
        context = {}
        context['calls'] = t_calls.objects.all().order_by('-id')
        context['staff'] = t_staff.objects.all()
        context['dict'] = t_dict.objects.all()
        return context


class CreateCall(View):
    def  get(self, request):
        # form text fields
        trip_no1 = request.GET.get('trip_no', None)
        driver1 = request.GET.get('driver', None)
        notes1 = request.GET.get('notes', None)
        private_notes1 = request.GET.get('private_notes', None)
        timestamp1 = request.GET.get('timestamp', None)
        user1 = request.GET.get('user', None)

        obj = t_calls.objects.create(
            trip_no = trip_no1,
            driver = driver1,
            notes = notes1,
            private_notes = private_notes1,
            timestamp =timestamp1,
            user = user1
        )

        call = {
                'id':obj.id, 
                'trip_no':obj.trip_no,
                'driver':obj.driver,
                'notes':obj.notes,
                'private_notes': obj.private_notes,
                'timestamp': obj.timestamp
                }

        data = {
            'call': call
        }
        return JsonResponse(data)

class DeleteCall(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        t_calls.objects.get(id=id1).delete()
        data = {
            'deleted': True
        }
        return JsonResponse(data)

class UpdateTrip(View):
    def  get(self, request):
        id1 = request.GET.get('id', None)
        trip_no1 = request.GET.get('trip_no', None)
        driver1 = request.GET.get('driver', None)
        notes1 = request.GET.get('notes', None)

        obj = t_calls.objects.get(id=id1)
        obj.trip_no = trip_no1
        obj.driver = driver1
        obj.notes = notes1
        obj.save()

        call = {'id':obj.id, 
                'trip_no':obj.trip_no, 
                'driver':obj.driver, 
                'notes':obj.notes
                }

        data = {
            'call': call
        }
        return JsonResponse(data)

def call_details(request, id):

    instance = get_object_or_404(t_calls, id=id)

    context = {
        'id': instance.id,
        "trip_no": instance.trip_no,
        'driver': instance.driver,
        'notes': instance.notes,
        'private_notes': instance.private_notes,
    }

    template = 'call_details.html'

    return render (request, template, context)
