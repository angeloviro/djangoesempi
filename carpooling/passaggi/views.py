from django.shortcuts import render
from passaggi.models import Type_Vehicle, Path_Offer, User, Vehicle

from django.views import generic
# Create your views here.
def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_type_vehicles = Type_Vehicle.objects.all().count()
    num_path_offers = Path_Offer.objects.all().count()


    context = {

       'num_type_vehicles': num_type_vehicles,
        'num_path_offers': num_path_offers,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
class Type_VehiclesListView(generic.ListView):
    model = Type_Vehicle
    paginate_by = 10
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(Type_VehiclesListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
    def get_queryset(self):
        return Type_Vehicle.objects.filter(description__icontains='i')[:5] # Get 5 books containing the title war
    template_name = 'type_vehicles/my_arbitrary_template_name_list.html'  # Specify your own template name/location
class Type_VehicleDetailView(generic.DetailView):
    model = Type_Vehicle

    def type_vehicle_detail_view(request, primary_key):
        try:
            type_vehicle = Type_Vehicle.objects.get(pk=primary_key)
        except Book.DoesNotExist:
            raise Http404('Type Vehicle does not exist')

        return render(request, 'passaggi/type_vehicle_detail.html', context={'type_vehicle': type_vehicle})
class Path_OfferListView(generic.ListView):
    model = Path_Offer
    paginate_by = 10
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get the context
        context = super(Path_OfferListView, self).get_context_data(**kwargs)
        # Create any data and add it to the context
        context['some_data'] = 'This is just some data'
        return context
    def get_queryset(self):
        return Path_Offer.objects.filter(departure__icontains='n')[:5]
    template_name = 'path_offers/my_arbitrary_template_name_list.html'  # Specify your own template name/location
class Path_OfferDetailView(generic.DetailView):
    model = Path_Offer

    def path_offer_detail_view(request, primary_key):
        try:
            path_offer = Path_Offer.objects.get(pk=primary_key)
        except Path_Offer.DoesNotExist:
            raise Http404('Path Offer does not exist')

        return render(request, 'passaggi/path_offer_detail.html', context={'path_offer': path_offer})
class UserDetailView(generic.DetailView):
    model= User
    def user_detail_view(request, primary_key):
        try:
            user:User.objects.get(pk=primary_key)
        except User.DoesNotExist:
            raise Http404('User does not exist')
        return render(request, 'passaggi/user_detail.html',context={'user':user})
class VehicleDetailView(generic.DetailView):
    model= Vehicle
    def vehicle_detail_view(request, primary_key):
        try:
            vehicle:Vehicle.objects.get(pk=primary_key)
        except Vehicle.DoesNotExist:
            raise Http404('Vehicle does not exist')
        return render(request, 'passaggi/vehicle_detail.html',context={'vehicle': vehicle})

