import stripe
stripe.api_key = "sk_test_51OJLHxGNMWfJBC8Z2qqodpsLy6uZUJwgD4DbVV31AieE51C40otahL0LdqNazwwCE12klQMu0Cwyj8x8dYsKQgkZ00vOOfOkI6"

starter_subscription = stripe.Product.create(
  name="Starter Subscription",
  description="$12/Month subscription",
)

starter_subscription_price = stripe.Price.create(
  unit_amount=1200,
  currency="usd",
  recurring={"interval": "month"},
  product=starter_subscription['id'],
)

# Save these identifiers
print(f"Success! Here is your starter subscription product id: {starter_subscription.id}")
print(f"Success! Here is your starter subscription price id: {starter_subscription_price.id}")
