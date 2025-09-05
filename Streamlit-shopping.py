import streamlit as st

# Shirt product details
products = [
    {
        "name": "Classic White Shirt",
        "price": 25.00,
        "image_url": "SHIRT1.JPG"
    },
    {
        "name": "Blue Denim Shirt",
        "price": 35.00,
        "image_url": "SHIRT2.JPG"
    }
]

st.set_page_config(page_title="Shirt Shop", layout="wide")

st.title("🛍️ Vijayanand Shirt Shopping Site")
st.markdown("Welcome to our simple shopping site. Choose your shirts and see the total cost instantly.")

st.markdown("---")

# Layout for products
cols = st.columns(2)

quantities = []

for idx, (col, product) in enumerate(zip(cols, products)):
    with col:
        st.image(product["image_url"], use_container_width=200)
        st.subheader(product["name"])
        st.write(f"💲 Price: ${product['price']:.2f}")
        qty = st.number_input(
            f"Select quantity", min_value=0, step=1, key=f"qty_{idx}"
        )
        quantities.append(qty)

st.markdown("---")

# Total cost calculation
total_cost = sum(qty * product["price"] for qty, product in zip(quantities, products))

st.subheader("🧾 Order Summary")
for qty, product in zip(quantities, products):
    if qty > 0:
        st.write(f"- {qty} x {product['name']} @ ${product['price']:.2f} each")

st.success(f"**Total: ${total_cost:.2f}**")

