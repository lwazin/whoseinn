from django.shortcuts import render, redirect
from .models import Accom, Application, CustomUser, Image, InternalMessage
from django.db.models import Q
import googlemaps
import random
import string

gmaps_key = googlemaps.Client(key="AIzaSyBzGdfXJDH-I53mWEqNG3lisZ0stwiL3Bw")

def Create(request):
    def ran_gen(size=6, chars=string.ascii_letters):
        x = ''.join(random.choice(chars) for x in range(size))
        if len(Accom.objects.filter(slug=x)) != 0:
            ran_gen()
        else:
            return x

    if request.method == 'POST':
        post = Accom()
        post.address = request.POST['address']
        location = gmaps_key.geocode(post.address)
        post.province = location[0]['address_components'][5]['long_name']
        post.lng = location[0]['geometry']['location']['lng']
        post.lat = location[0]['geometry']['location']['lat']
        post.type = request.POST['type']
        post.gender = request.POST['gender']
        post.title = request.POST['title']
        post.description = request.POST['description']
        post.price = request.POST['price']

        if request.POST['electricity'] == 'true':
            post.electricity = True
        else:
            post.electricity = False
        if request.POST['shuttle'] == 'true':
            post.shuttle = True
        else:
            post.shuttle = False
        if request.POST['wifi'] == 'true':
            post.wifi = True
        else:
            post.wifi = False
        if request.POST['furnished'] == 'true':
            post.furnished = True
        else:
            post.furnished = False

        post.cover = post.cover+str(request.FILES.getlist('related_images')[0]).replace(" ", "_")
        post.user = request.user
        try:
            post.slug = ran_gen()
        except:
            print('Unique identifier taken.. attempting a new one..')
        post.save()


        for i in request.FILES.getlist('related_images'):
            image = Image()
            image.image = i
            image.post = post
            image.save()


        app = Application()
        app.viewer = request.user
        app.accom = post
        app.status = 'owned'
        app.save()
    return redirect('home')


def Update(request, slug):
    obj = Accom.objects.get(slug=slug)
    img = Image.objects.filter(post=Accom.objects.get(slug=slug))

    context = {
    'obj': obj,
    'img': img
    }

    if request.method == 'POST':
        obj.type = request.POST['type']
        obj.gender = request.POST['gender']
        obj.title = request.POST['title']
        obj.description = request.POST['title']
        obj.price = request.POST['price']

        obj.electricity = request.POST['electricity']
        obj.shuttle = request.POST['shuttle']
        obj.wifi = request.POST['wifi']
        obj.tv = request.POST['tv']
        obj.furnished = request.POST['furnished']

        obj.cover = obj.cover+str(request.FILES.getlist('image0')[0]).replace(" ", "_")
        obj.save()

    return render(request, 'posts/update.html', context)

def Delete(request, slug):
    obj = Accom.objects.get(slug=slug)
    if request.user==obj.user:
        obj.delete()
    return redirect('home')

def Search(request):
    context = {

    }
    if request.method == 'POST':
        context = {
            'search_term':""
        }
        if request.POST['label_search'] == 'single_search':
            context['search_term'] = request.POST['search']
            search = (Q(description__icontains=request.POST['search']) | Q(title__icontains=request.POST['search']) | Q(province__icontains=request.POST['search']))

            context['posts'] = Accom.objects.filter(search)

        elif request.POST['label_search'] == 'multiple_search':
            def bool(term):
                if term == 'true':
                    return True
                elif term == 'false':
                    return False

            province = Q(province__icontains=request.POST['province_search'])
            gender = Q(gender__icontains=request.POST['gender_search'])
            type = Q(type__icontains=request.POST['room_search'])
            wifi = Q(wifi__icontains=bool(request.POST['wifi_search']))
            electricity = Q(electricity__icontains=bool(request.POST['electricity_search']))
            shuttle = Q(shuttle__icontains=bool(request.POST['shuttle_search']))
            furnished = Q(furnished__icontains=bool(request.POST['furnished_search']))

            search = (province & ((type | gender) & (wifi & electricity & shuttle & furnished)))

            context['posts'] = Accom.objects.filter(search)
            print(context['posts'])

    return render(request, "index.html", context)

def Detail(request, slug):
    accom = Accom.objects.get(slug=slug)
    context = {
    'accom': accom,
    'images': Image.objects.filter(post=accom),
    'messages': InternalMessage.objects.filter(accom=accom).order_by('-id')
    }
    return render(request, 'detail.html', context)
