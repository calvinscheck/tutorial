from flask import Blueprint, render_template, request
from app.cookies.models import Cookie
from app.orders.models import Order, Address, CookieOrder

blueprint = Blueprint('orders', __name__)

@blueprint.get('/checkout')
def get_checkout():
  cookies = Cookie.query.all()
  return render_template('orders/new.html', cookies=cookies)

@blueprint.post('/checkout')
def post_checkout():
  # Create an order
  order = Order()
  order.save()
  # Add a new address
  address = Address(
    name=request.form.get('name'),
    street=request.form.get('street'),
    city=request.form.get('city'),
    state=request.form.get('state'),
    zip=request.form.get('zip'),
    country=request.form.get('country'),
    order=order
  )
  address.save()

  cookies = Cookie.query.all()

  for cookie in cookies:
    number_of_cookies = request.form.get(cookie.slug, 0)

    if int(number_of_cookies) > 0:
      cookie_order = CookieOrder(
        cookie=cookie,
        order=order,
        number_of_cookies=number_of_cookies
      )
      cookie_order.save()

  return render_template('orders/new.html', cookies=cookies)