from django.shortcuts import render, get_object_or_404, redirect
from django.views import View
from .forms import ProductForm, SubmitForm
from django.contrib.auth.decorators import login_required
from django.dispatch import receiver
from PIL import Image, ImageDraw, ImageFont



def index(request):


    return render(
        request,
        "index.html",)


def category_list(request):
    return render(request, "category_list.html")


def category_detail(request):

    return render(
        request, "category_detail.html")


def product_list(request):
    return render(request, "shopgrid.html")


def product_detail(request):
    return render(request, "shopdetails.html")


def cart(request):

    return render(request, "cart.html")



@login_required
def checkout(request):
    return render(request, "checkout.html")


def contact(request):
    return render(request, "contact.html")

def product_create(request):

    return render(request, "product_form.html")



def trend(request):
    return render(request, "trand.html")


# @receiver(post_save, sender=Product)
# def add_watermark(sender, instance, created, **kwargs):
#     if created:  # Only perform this action if the product is newly created
#         watermark_path = "assets/assets/img/WaterMark.png"
#         product_image_path = (
#             instance.image1.path
#         )  # Assuming image1 is the main product image

#         # Open the product image
#         with Image.open(product_image_path) as img:
#             # Open the watermark image
#             with Image.open(watermark_path) as watermark:
#                 # Calculate the position to place the watermark at the center
#                 position = (
#                     (img.width - watermark.width) // 2,
#                     (img.height - watermark.height) // 2,
#                 )

                # Paste the watermark onto the product image
                img.paste(watermark, position, watermark)

                # Save the modified image
                img.save(product_image_path)


# @login_required
# def product_create(request):
#     if request.method == "POST":
#         form = ProductForm(request.POST)
#         if form.is_valid():
#             product = form.save(commit=False)
#             # Associate the product with the current user
#             product.user = request.user
#             product.save()
#             return redirect(
#                 "/", pk=product.pk
#             )  # Redirect to product detail page
#     else:
#         form = ProductForm()
#     return render(request, "product_form.html", {"form": form})


def product_edit(request, pk):

    return render(request, "product_edit.html")


# def product_delete(request, pk):
#     product = get_object_or_404(Product, pk=pk)
#     if request.method == "POST":
#         product.delete()
#         return redirect("Profile")  # Redirect to "my_ads" after successful deletion
#     return render(request, "product_confirm_delete.html", {"product": product})


@login_required
def success(request):
    return render(request, "success.html")


@login_required
def Dash(request):


    return render(request, "dashboard.html")


@login_required
def Profile(request):
    return render(request, "profile.html")


@login_required
def Privacy(request):
    return render(request, "privacy-setting.html")


@login_required
def my_ads(request):
    return render(request, "account-myads.html")

@login_required
def payment(request):
    return render(request, "payments.html")