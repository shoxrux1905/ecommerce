
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from shop.forms import OrderForm
from shop.models import Order, Shop, Category, Types


class IndexView(ListView) :
    queryset = Shop.objects.all()
    template_name = 'index.html'

# def home(request) :
#     return render(request, 'index.html')

class Products(ListView) :
    queryset = Shop.objects.all()
    template_name = 'products.html'
    context_object_name = 'shops'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['types'] = Types.objects.all()
        return context

# def products(request) :
#     shops = Shop.objects.all()
#     categories = Category.objects.all()
#     types = Types.objects.all()
#     context = {
#         'shops': shops,
#         'categories': categories,
#         'types': types,
#     }
#     return render(request, 'products.html', context=context)

class Detail(DetailView) :
    queryset = Shop.objects.all()
    template_name = 'detail.html'
    context_object_name = 'shops'

# def detail(request, pk) :
#     shops = get_object_or_404(Shop, id=pk)
#     categories = Category.objects.all()
#     context = {
#         'shops': shops,
#         'categories': categories,
#     }
#     return render(request, 'detail.html', context=context)

class Order_View(CreateView):
    queryset = Order
    form_class = OrderForm
    template_name = 'order.html'
    success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        messages.success(self.request, "Buyurtma qabul qilindi !")
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        shop_id = self.kwargs.get('pk')
        context['shops'] = Shop.objects.get(id=shop_id)
        return context


# def order_view(request, shop_id):
#     shops = get_object_or_404(Shop, id=shop_id)
#     orders = Order.objects.all()
#     if request.method == 'POST':
#         form = OrderForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, "Buyurtma muvaffaqiyatli yuborildi!")
#             return redirect(reverse('home'))
#         else:
#             print(form.errors)
#     else:
#         form = OrderForm()
        
#     context = {
#         'orders': orders,
#         'form': form,
#         'shops': shops,
#     }
#     return render(request, 'order.html', context)