from .models import Customer, Orders, Product, InventoryItem

def admin_sidebar_counts(request):
    if request.user.is_authenticated and request.user.is_staff:
        total_users = Customer.objects.count()
        # Count only pending orders as per user request
        total_orders = Orders.objects.filter(status='Pending').count()
        total_products = Product.objects.count()
        total_inventory = InventoryItem.objects.count()
        return {
            'sidebar_counts': {
                'users': total_users,
                'orders': total_orders,
                'products': total_products,
                'inventory': total_inventory,
            }
        }
    return {}
