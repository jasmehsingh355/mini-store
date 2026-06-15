import streamlit as st

# ----------------------------------
# Page Configuration
# ----------------------------------
st.set_page_config(
    page_title="MiniStore",
    page_icon="🛍️",
    layout="wide"
)

# ----------------------------------
# Custom CSS Styling
# ----------------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.hero {
    background: linear-gradient(90deg, #4f46e5, #7c3aed);
    padding: 30px;
    border-radius: 15px;
    color: white;
    text-align: center;
    margin-bottom: 25px;
}

.product-card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}

.product-name {
    font-size: 22px;
    font-weight: bold;
}

.product-price {
    color: green;
    font-size: 20px;
    font-weight: bold;
}

.category-tag {
    background-color: #eef2ff;
    padding: 5px 10px;
    border-radius: 10px;
    display: inline-block;
    margin-top: 10px;
}
</style>
""", unsafe_allow_html=True)

# ----------------------------------
# Sample Product Data
# ----------------------------------
products = [
    {
        "name": "Wireless Headphones",
        "price": 2999,
        "description": "Noise-cancelling Bluetooth headphones with premium sound quality.",
        "category": "Electronics"
    },
    {
        "name": "Smart Watch",
        "price": 4999,
        "description": "Track fitness, heart rate, and notifications on the go.",
        "category": "Electronics"
    },
    {
        "name": "Running Shoes",
        "price": 2499,
        "description": "Lightweight and comfortable shoes for everyday workouts.",
        "category": "Fashion"
    },
    {
        "name": "Laptop Backpack",
        "price": 1499,
        "description": "Stylish backpack with padded laptop compartment.",
        "category": "Accessories"
    },
    {
        "name": "Coffee Maker",
        "price": 3499,
        "description": "Brew delicious coffee at home with one touch.",
        "category": "Home"
    },
    {
        "name": "Gaming Mouse",
        "price": 1999,
        "description": "High-precision gaming mouse with customizable RGB lighting.",
        "category": "Electronics"
    }
]

# ----------------------------------
# Sidebar
# ----------------------------------
st.sidebar.title("🛒 MiniStore")

categories = ["All"] + sorted(
    list(set(product["category"] for product in products))
)

selected_category = st.sidebar.radio(
    "Browse Categories",
    categories
)

st.sidebar.markdown("---")
st.sidebar.subheader("Shopping Cart Summary")

cart_items = 3
cart_total = 7497

st.sidebar.write(f"Items in Cart: {cart_items}")
st.sidebar.write(f"Total Amount: ₹{cart_total}")

st.sidebar.button("Proceed to Checkout")

# ----------------------------------
# Homepage Hero Section
# ----------------------------------
st.markdown("""
<div class="hero">
    <h1>🛍️ Welcome to MiniStore</h1>
    <h3>Your One-Stop Online Shopping Destination</h3>
    <p>Discover amazing products at affordable prices.</p>
</div>
""", unsafe_allow_html=True)

# ----------------------------------
# Welcome Section
# ----------------------------------
st.header("Welcome")

st.write("""
MiniStore is a demo e-commerce website built using Streamlit.
Browse through our featured collection of electronics, fashion,
home products, and accessories.
""")

# ----------------------------------
# Filter Products by Category
# ----------------------------------
if selected_category == "All":
    filtered_products = products
else:
    filtered_products = [
        product
        for product in products
        if product["category"] == selected_category
    ]

# ----------------------------------
# Featured Products Section
# ----------------------------------
st.subheader("⭐ Featured Products")

cols = st.columns(3)

for index, product in enumerate(filtered_products):
    with cols[index % 3]:
        st.markdown(f"""
        <div class="product-card">
            <div class="product-name">{product['name']}</div>
            <br>
            <div class="product-price">₹{product['price']}</div>
            <p>{product['description']}</p>
            <div class="category-tag">{product['category']}</div>
        </div>
        """, unsafe_allow_html=True)

        st.button(
            f"Add to Cart",
            key=product["name"]
        )

# ----------------------------------
# Footer
# ----------------------------------
st.markdown("---")
st.markdown(
    "<center><b>© 2026 MiniStore | Demo E-Commerce Website</b></center>",
    unsafe_allow_html=True
)
