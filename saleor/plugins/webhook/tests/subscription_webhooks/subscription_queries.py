from .....graphql.tests.queries import fragments

GIFT_CARD_CREATED = (
    fragments.GIFT_CARD_DETAILS
    + """
    subscription{
      event{
        ...on GiftCardCreated{
          giftCard{
            ...GiftCardDetails
          }
        }
      }
    }
"""
)


GIFT_CARD_UPDATED = (
    fragments.GIFT_CARD_DETAILS
    + """
    subscription{
      event{
        ...on GiftCardUpdated{
          giftCard{
            ...GiftCardDetails
          }
        }
      }
    }
"""
)

GIFT_CARD_DELETED = (
    fragments.GIFT_CARD_DETAILS
    + """
    subscription{
      event{
        ...on GiftCardDeleted{
          giftCard{
            ...GiftCardDetails
          }
        }
      }
    }
"""
)


GIFT_CARD_STATUS_CHANGED = (
    fragments.GIFT_CARD_DETAILS
    + """
    subscription{
      event{
        ...on GiftCardStatusChanged{
          giftCard{
            ...GiftCardDetails
          }
        }
      }
    }
"""
)


VOUCHER_CREATED = (
    fragments.VOUCHER_DETAILS
    + """
    subscription{
      event{
        ...on VoucherCreated{
          voucher{
            ...VoucherDetails
          }
        }
      }
    }
"""
)


VOUCHER_UPDATED = (
    fragments.VOUCHER_DETAILS
    + """
    subscription{
      event{
        ...on VoucherUpdated{
          voucher{
            ...VoucherDetails
          }
        }
      }
    }
"""
)


VOUCHER_DELETED = (
    fragments.VOUCHER_DETAILS
    + """
    subscription{
      event{
        ...on VoucherDeleted{
          voucher{
            ...VoucherDetails
          }
        }
      }
    }
"""
)


CHANNEL_CREATED = """
    subscription{
      event{
        ...on ChannelCreated{
          channel{
            id
          }
        }
      }
    }
"""

CHANNEL_UPDATED = """
    subscription{
      event{
        ...on ChannelUpdated{
          channel{
            id
          }
        }
      }
    }
"""

CHANNEL_DELETED = """
    subscription{
      event{
        ...on ChannelDeleted{
          channel{
            id
          }
        }
      }
    }
"""

CHANNEL_STATUS_CHANGED = """
    subscription{
      event{
        ...on ChannelStatusChanged{
          channel{
            id
            isActive
          }
        }
      }
    }
"""


CATEGORY_CREATED = (
    fragments.CATEGORY_DETAILS
    + """
    subscription{
      event{
        ...on CategoryCreated{
          category{
            ...CategoryDetails
          }
        }
      }
    }
    """
)

CATEGORY_UPDATED = (
    fragments.CATEGORY_DETAILS
    + """
    subscription{
      event{
        ...on CategoryUpdated{
          category{
            ...CategoryDetails
          }
        }
      }
    }
    """
)

CATEGORY_DELETED = """
    subscription{
      event{
        ...on CategoryDeleted{
          category{
              id
            }
        }
      }
    }
"""


SHIPPING_PRICE_CREATED = (
    fragments.SHIPPING_METHOD_DETAILS
    + """
    subscription{
      event{
        ...on ShippingPriceCreated{
          shippingMethod{
            ...ShippingMethodDetails
          }
          shippingZone{
            id
            name
          }
        }
      }
    }
"""
)

SHIPPING_PRICE_UPDATED_UPDATED = (
    fragments.SHIPPING_METHOD_DETAILS
    + """
    subscription{
      event{
        ...on ShippingPriceUpdated{
          shippingMethod{
            ...ShippingMethodDetails
          }
          shippingZone{
            id
            name
          }
        }
      }
    }
"""
)

SHIPPING_PRICE_DELETED = """
    subscription{
      event{
        ...on ShippingPriceDeleted{
          shippingMethod{
            id
            name
          }
        }
      }
    }
"""

SHIPPING_ZONE_CREATED = """
    subscription{
      event{
        ...on ShippingZoneCreated{
          shippingZone{
            id
            name
            countries {
                code
            }
            channels {
                name
            }
          }
        }
      }
    }
"""

SHIPPING_ZONE_UPDATED_UPDATED = """
    subscription{
      event{
        ...on ShippingZoneUpdated{
          shippingZone{
            id
            name
            countries {
                code
            }
            channels {
                name
            }
          }
        }
      }
    }
"""

SHIPPING_ZONE_DELETED = """
    subscription{
      event{
        ...on ShippingZoneDeleted{
          shippingZone{
            id
            name
          }
        }
      }
    }
"""

PRODUCT_UPDATED = """
    subscription{
      event{
        ...on ProductUpdated{
          product{
            id
          }
        }
      }
    }
"""

PRODUCT_CREATED = """
    subscription{
      event{
        ...on ProductCreated{
          product{
            id
          }
        }
      }
    }
"""

PRODUCT_DELETED = """
    subscription{
      event{
        ...on ProductDeleted{
          product{
            id
          }
        }
      }
    }
"""

PRODUCT_VARIANT_CREATED = """
    subscription{
      event{
        ...on ProductVariantCreated{
          productVariant{
            id
          }
        }
      }
    }
"""

PRODUCT_VARIANT_UPDATED = """
    subscription{
      event{
        ...on ProductVariantUpdated{
          productVariant{
            id
          }
        }
      }
    }
"""


PRODUCT_VARIANT_DELETED = """
    subscription{
      event{
        ...on ProductVariantDeleted{
          productVariant{
            id
          }
        }
      }
    }
"""

PRODUCT_VARIANT_OUT_OF_STOCK = """
    subscription{
      event{
        ...on ProductVariantOutOfStock{
          productVariant{
            id
          }
        }
      }
    }
"""

PRODUCT_VARIANT_BACK_IN_STOCK = """
    subscription{
      event{
        ...on ProductVariantBackInStock{
          productVariant{
            id
          }
        }
      }
    }
"""

ORDER_CREATED = """
    subscription{
      event{
        ...on OrderCreated{
          order{
            id
          }
        }
      }
    }
"""

ORDER_UPDATED = """
    subscription{
      event{
        ...on OrderUpdated{
          order{
            id
          }
        }
      }
    }
"""

ORDER_CONFIRMED = """
    subscription{
      event{
        ...on OrderConfirmed{
          order{
            id
          }
        }
      }
    }
"""

ORDER_FULLY_PAID = """
    subscription{
      event{
        ...on OrderFullyPaid{
          order{
            id
          }
        }
      }
    }
"""

ORDER_CANCELLED = """
    subscription{
      event{
        ...on OrderCancelled{
          order{
            id
          }
        }
      }
    }
"""

ORDER_FULFILLED = """
    subscription{
      event{
        ...on OrderFulfilled{
          order{
            id
          }
        }
      }
    }
"""

DRAFT_ORDER_CREATED = """
    subscription{
      event{
        ...on DraftOrderCreated{
          order{
            id
          }
        }
      }
    }
"""

DRAFT_ORDER_UPDATED = """
    subscription{
      event{
        ...on DraftOrderUpdated{
          order{
            id
          }
        }
      }
    }
"""

DRAFT_ORDER_DELETED = """
    subscription{
      event{
        ...on DraftOrderDeleted{
          order{
            id
          }
        }
      }
    }
"""

SALE_CREATED = (
    fragments.SALE_DETAILS
    + """
    subscription{
      event{
        ...on SaleCreated{
          sale{
            ...SaleDetails
          }
        }
      }
    }
"""
)

SALE_UPDATED = (
    fragments.SALE_DETAILS
    + """
    subscription{
      event{
        ...on SaleUpdated{
          sale{
            ...SaleDetails
          }
        }
      }
    }
"""
)

SALE_DELETED = (
    fragments.SALE_DETAILS
    + """
    subscription{
      event{
        ...on SaleDeleted{
          sale{
            ...SaleDetails
          }
        }
      }
    }
"""
)

INVOICE_REQUESTED = (
    fragments.INVOICE_DETAILS
    + """
    subscription{
      event{
        ...on InvoiceRequested{
          invoice{
            ...InvoiceDetails
          }
        }
      }
    }
"""
)

INVOICE_DELETED = (
    fragments.INVOICE_DETAILS
    + """
    subscription{
      event{
        ...on InvoiceDeleted{
          invoice{
            ...InvoiceDetails
          }
        }
      }
    }
"""
)

INVOICE_SENT = (
    fragments.INVOICE_DETAILS
    + """
    subscription{
      event{
        ...on InvoiceSent{
          invoice{
            ...InvoiceDetails
          }
        }
      }
    }
"""
)

FULFILLMENT_CREATED = (
    fragments.FULFILLMENT_DETAILS
    + """
    subscription{
      event{
        ...on FulfillmentCreated{
          fulfillment{
            ...FulfillmentDetails
          }
        }
      }
    }
"""
)

FULFILLMENT_CANCELED = (
    fragments.FULFILLMENT_DETAILS
    + """
    subscription{
      event{
        ...on FulfillmentCanceled{
          fulfillment{
            ...FulfillmentDetails
          }
        }
      }
    }
"""
)

CUSTOMER_CREATED = (
    fragments.USER_DETAILS
    + """
    subscription{
      event{
        ...on CustomerCreated{
          user{
            ...UserDetails
          }
        }
      }
    }
"""
)

CUSTOMER_UPDATED = (
    fragments.USER_DETAILS
    + """
    subscription{
      event{
        ...on CustomerUpdated{
          user{
            ...UserDetails
          }
        }
      }
    }
"""
)

COLLECTION_CREATED = (
    fragments.COLLECTION
    + """
    subscription{
      event{
        ...on CollectionCreated{
          collection(channel: "main"){
            ...CollectionDetails
          }
        }
      }
    }
    """
)

COLLECTION_UPDATED = (
    fragments.COLLECTION
    + """
    subscription{
      event{
        ...on CollectionUpdated{
          collection(channel: "main"){
            ...CollectionDetails
          }
        }
      }
    }
    """
)

COLLECTION_DELETED = (
    fragments.COLLECTION
    + """
    subscription{
      event{
        ...on CollectionDeleted{
          collection(channel: "main"){
            ...CollectionDetails
          }
        }
      }
    }
    """
)


CHECKOUT_CREATED = """
    subscription{
      event{
        ...on CheckoutCreated{
          checkout{
            id
          }
        }
      }
    }
"""

CHECKOUT_UPDATED = """
    subscription{
      event{
        ...on CheckoutUpdated{
          checkout{
            id
          }
        }
      }
    }
"""

PAGE_CREATED = (
    fragments.PAGE_DETAILS
    + """
    subscription{
      event{
        ...on PageCreated{
          page{
            ...PageDetails
          }
        }
      }
    }
"""
)

PAGE_UPDATED = (
    fragments.PAGE_DETAILS
    + """
    subscription{
      event{
        ...on PageUpdated{
          page{
            ...PageDetails
          }
        }
      }
    }
"""
)

PAGE_DELETED = (
    fragments.PAGE_DETAILS
    + """
    subscription{
      event{
        ...on PageDeleted{
          page{
            ...PageDetails
          }
        }
      }
    }
"""
)

MULTIPLE_EVENTS = """
subscription{
  event{
    ...on ProductCreated{
      product{
        id
      }
    }
    ...on ProductUpdated{
      product{
        id
      }
    }
    ...on OrderCreated{
      order{
        id
      }
    }
  }
}
"""

TRANSLATION_CREATED = """
subscription {
  event {
    ... on TranslationCreated {
      translation {
        ... on ProductTranslation {
          id
        }
        ... on CollectionTranslation {
          id
        }
        ... on CategoryTranslation {
          id
        }
        ... on AttributeTranslation {
          id
        }
        ... on ProductVariantTranslation {
          id
        }
        ... on PageTranslation {
          id
        }
        ... on ShippingMethodTranslation {
          id
        }
        ... on SaleTranslation {
          id
        }
        ... on VoucherTranslation {
          id
        }
        ... on MenuItemTranslation {
          id
        }
        ... on AttributeValueTranslation {
          id
        }
      }
    }
  }
}
"""

TRANSLATION_UPDATED = """
subscription {
  event {
    ... on TranslationUpdated {
      translation {
        ... on ProductTranslation {
          id
        }
        ... on CollectionTranslation {
          id
        }
        ... on CategoryTranslation {
          id
        }
        ... on AttributeTranslation {
          id
        }
        ... on ProductVariantTranslation {
          id
        }
        ... on PageTranslation {
          id
        }
        ... on ShippingMethodTranslation {
          id
        }
        ... on SaleTranslation {
          id
        }
        ... on VoucherTranslation {
          id
        }
        ... on MenuItemTranslation {
          id
        }
        ... on AttributeValueTranslation {
          id
        }
      }
    }
  }
}
"""

TEST_VALID_SUBSCRIPTION = """
    subscription{
      event{
        ...on ProductUpdated{
          product{
            id
          }
        }
      }
    }
"""

TEST_INVALID_MULTIPLE_SUBSCRIPTION = """
subscription{
  event{
    ...on ProductUpdated{
      product{
        id
      }
    }
  }
}
subscription{
  event{
    ...on ProductCreated{
      product{
        id
      }
    }
  }
}
"""


TEST_INVALID_SUBSCRIPTION_AND_QUERY = """
subscription{
  event{
    ...on ProductUpdated{
      product{
        id
      }
    }
  }
}
query{
  products(first:100){
    edges{
      node{
        id
      }
    }
  }
}
"""

TEST_INVALID_QUERY_AND_SUBSCRIPTION = """
query{
  products(first:100){
    edges{
      node{
        id
      }
    }
  }
}
subscription{
  event{
    ...on ProductUpdated{
      product{
        id
      }
    }
  }
}"""

TEST_VALID_SUBSCRIPTION_QUERY_WITH_FRAGMENT = """
fragment productFragment on Product{
  name
}
subscription{
  event{
    ...on ProductUpdated{
      product{
        id
        ...productFragment
      }
    }
  }
}
"""

TEST_VALID_SUBSCRIPTION_QUERY = """
    subscription{
      event{
        ...on ProductUpdated{
          product{
            id
          }
        }
      }
    }
"""


WAREHOUSE_CREATED = (
    fragments.WAREHOUSE_DETAILS
    + """
    subscription{
      event{
        ...on WarehouseCreated{
          warehouse{
            ...WarehouseDetails
          }
        }
      }
    }
"""
)

WAREHOUSE_UPDATED = (
    fragments.WAREHOUSE_DETAILS
    + """
    subscription{
      event{
        ...on WarehouseUpdated{
          warehouse{
            ...WarehouseDetails
          }
        }
      }
    }
"""
)

WAREHOUSE_DELETED = (
    fragments.WAREHOUSE_DETAILS
    + """
    subscription{
      event{
        ...on WarehouseDeleted{
          warehouse{
            ...WarehouseDetails
          }
        }
      }
    }
"""
)