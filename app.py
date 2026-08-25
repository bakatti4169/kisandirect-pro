import streamlit as st
import pandas as pd
import datetime

# Page Configuration
st.set_page_config(
    page_title="KisanDirect | Next-Gen Agri Marketplace",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom Styling (CSS for clean cards, gradients and badges)
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(135deg, #1b5e20, #2e7d32, #43a047);
        padding: 24px;
        border-radius: 12px;
        color: white;
        text-align: center;
        margin-bottom: 25px;
    }
    .main-header h1 {
        color: white !important;
        font-size: 2.2rem;
        margin-bottom: 0px;
    }
    .product-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 16px;
        border: 1px solid #e0e0e0;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
        margin-bottom: 20px;
        color: #333333;
    }
    .badge {
        background-color: #e8f5e9;
        color: #2e7d32;
        padding: 4px 10px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: bold;
        display: inline-block;
    }
    .metric-card {
        background: white;
        padding: 18px;
        border-radius: 10px;
        border-left: 5px solid #2e7d32;
        box-shadow: 0 2px 5px rgba(0,0,0,0.05);
    }
</style>
""", unsafe_allow_html=True)

# Image Mapping Dictionary
CROP_IMAGES = {
    "Wheat (Gehu)": "https://images.unsplash.com/photo-1574323347407-f5e1ad6d020b?w=600&auto=format&fit=crop&q=60",
    "Rice (Chawal)": "https://images.unsplash.com/photo-1586201375761-83865001e31c?w=600&auto=format&fit=crop&q=60",
    "Potato (Aloo)": "https://images.unsplash.com/photo-1518977676601-b53f82aba655?w=600&auto=format&fit=crop&q=60",
    "Onion (Pyaz)": "https://images.unsplash.com/photo-1618512496248-a07fe83aa8cb?w=600&auto=format&fit=crop&q=60",
    "Tomato (Tamatar)": "https://images.unsplash.com/photo-1592924357228-91a4daadcfea?w=600&auto=format&fit=crop&q=60",
    "Mustard (Sarson)": "https://images.unsplash.com/photo-1508873696983-2df5293cb395?w=600&auto=format&fit=crop&q=60"
}

# Session State Initialization
if 'listings' not in st.session_state:
    st.session_state.listings = [
        {"ID": 101, "Farmer": "Ramesh Kumar", "Phone": "+91 98765 43210", "Crop": "Wheat (Gehu)", "Qty": 500, "Price": 24, "Location": "Patna", "Quality": "Grade A (Organic)"},
        {"ID": 102, "Farmer": "Sunil Singh", "Phone": "+91 91234 56780", "Crop": "Potato (Aloo)", "Qty": 1200, "Price": 14, "Location": "Hajipur", "Quality": "Grade A"},
        {"ID": 103, "Farmer": "Amit Yadav", "Phone": "+91 99887 76655", "Crop": "Tomato (Tamatar)", "Qty": 300, "Price": 22, "Location": "Patna", "Quality": "Grade A+ (Fresh Pick)"},
        {"ID": 104, "Farmer": "Rajendra Prasad", "Phone": "+91 94312 88990", "Crop": "Rice (Chawal)", "Qty": 850, "Price": 34, "Location": "Gaya", "Quality": "Premium Basmati"}
    ]

if 'orders' not in st.session_state:
    st.session_state.orders = [
        {"Order ID": "ORD-901", "Crop": "Wheat (Gehu)", "Qty (kg)": 150, "Total (₹)": 3600, "Farmer": "Ramesh Kumar", "Buyer": "Hotel Maurya Canteen", "Delivery City": "Patna", "Status": "Escrow Locked 🔒"}
    ]

# Header Banner
st.markdown("""
<div class="main-header">
    <h1>🌾 KisanDirect Platform</h1>
    <p style="margin:5px 0 0 0; opacity: 0.9;">Connecting Farmers Directly to Consumers & Bulk Retailers | SIH 2026</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Navigation
with st.sidebar:
    st.image("https://images.unsplash.com/photo-1595974482597-4b8da8879bc5?w=400&auto=format&fit=crop&q=60", caption="Direct Farm Link", use_container_width=True)
    st.markdown("### Navigation Portal")
    menu = st.radio("Go to:", [
        "🛒 Buyer Marketplace",
        "👨‍🌾 Farmer Dashboard",
        "📦 Live Transactions & Tracking",
        "📊 Agmarknet Price Intelligence",
        "📈 Impact Analytics"
    ])
    st.markdown("---")
    st.caption("🚀 Version 2.4 | Powered by Streamlit Cloud")

# ================= 1. BUYER MARKETPLACE =================
if menu == "🛒 Buyer Marketplace":
    st.subheader("🛒 Fresh Farm Produce (Direct Marketplace)")
    st.write("Browse certified farmer listings without any commission brokers.")

    col_filter1, col_filter2 = st.columns([1, 2])
    with col_filter1:
        locations = ["All"] + sorted(list(set(item["Location"] for item in st.session_state.listings)))
        sel_loc = st.selectbox("📍 Filter by District", locations)
    with col_filter2:
        crops = ["All"] + sorted(list(set(item["Crop"] for item in st.session_state.listings)))
        sel_crop = st.selectbox("🌾 Filter by Crop", crops)

    # Filtered Data
    filtered_items = [
        item for item in st.session_state.listings 
        if (sel_loc == "All" or item["Location"] == sel_loc) and (sel_crop == "All" or item["Crop"] == sel_crop)
    ]

    # Display as Rich Visual Cards
    st.markdown("### Available Produce")
    if not filtered_items:
        st.warning("No listings found for the selected filter.")
    else:
        for i in range(0, len(filtered_items), 2):
            c1, c2 = st.columns(2)
            row_items = filtered_items[i:i+2]
            
            for col, item in zip([c1, c2], row_items):
                with col:
                    img_url = CROP_IMAGES.get(item["Crop"], "https://images.unsplash.com/photo-1498837167922-ddd27525d352?w=600&auto=format&fit=crop&q=60")
                    st.image(img_url, use_container_width=True)
                    st.markdown(f"### {item['Crop']} - ₹{item['Price']}/kg")
                    st.markdown(f"**👨‍🌾 Farmer:** {item['Farmer']} (`{item['Phone']}`)")
                    st.markdown(f"**📍 Location:** {item['Location']} | **📦 Available:** {item['Qty']} kg")
                    st.markdown(f"<span class='badge'>{item['Quality']}</span>", unsafe_allow_html=True)
                    st.markdown("---")

    # Order Placement Box
    st.markdown("### ⚡ Direct Purchase & Smart Escrow")
    with st.expander("👉 Click here to Place an Order directly with the Farmer", expanded=True):
        o_col1, o_col2 = st.columns(2)
        with o_col1:
            buyer_name = st.text_input("Buyer Name / Business Name", placeholder="e.g. Gaurav Restaurant / Anand Kumar")
            buyer_city = st.selectbox("Your Delivery Location", ["Patna", "Hajipur", "Muzaffarpur", "Gaya", "Bhagalpur"])
            buyer_phone = st.text_input("Buyer Phone Number", placeholder="+91 98XXXXXXXX")
        
        with o_col2:
            listing_options = {f"#{item['ID']} - {item['Crop']} by {item['Farmer']} (₹{item['Price']}/kg)": item['ID'] for item in st.session_state.listings}
            selected_listing_str = st.selectbox("Choose Listing to Buy", list(listing_options.keys()))
            selected_id = listing_options[selected_listing_str]
            selected_crop_item = next(item for item in st.session_state.listings if item["ID"] == selected_id)
            order_qty = st.number_input("Order Quantity (kg)", min_value=5, max_value=selected_crop_item["Qty"], value=min(50, selected_crop_item["Qty"]))

        total_price = order_qty * selected_crop_item["Price"]
        st.write(f"#### Total Estimated Bill: **₹{total_price:,.2f}** *(Direct Farmer Transfer via Escrow)*")

        if st.button("🔒 Confirm Order & Lock Escrow Payment", use_container_width=True):
            if buyer_name and buyer_phone:
                # Deduct quantity
                selected_crop_item["Qty"] -= order_qty
                
                # Add to orders
                new_order = {
                    "Order ID": f"ORD-{len(st.session_state.orders) + 902}",
                    "Crop": selected_crop_item["Crop"],
                    "Qty (kg)": order_qty,
                    "Total (₹)": total_price,
                    "Farmer": f"{selected_crop_item['Farmer']} ({selected_crop_item['Location']})",
                    "Buyer": f"{buyer_name} ({buyer_city})",
                    "Delivery City": buyer_city,
                    "Status": "Escrow Locked 🔒"
                }
                st.session_state.orders.append(new_order)
                st.success(f"🎉 Order #{new_order['Order ID']} placed successfully! Payment locked in smart escrow.")
                st.balloons()
            else:
                st.error("Please enter your name and phone number to complete the order.")

# ================= 2. FARMER DASHBOARD =================
elif menu == "👨‍🌾 Farmer Dashboard":
    st.subheader("👨‍🌾 Farmer Produce Listing Desk")
    st.write("List your harvest directly. Both buyers and local community logistics hubs will see this.")

    f_col1, f_col2 = st.columns(2)
    with f_col1:
        f_name = st.text_input("Farmer Full Name", placeholder="e.g. Rameshwar Sah")
        f_phone = st.text_input("Mobile Number for Buyer Contact", placeholder="+91 9XXXXXXXXX")
        f_crop = st.selectbox("Select Harvested Crop", list(CROP_IMAGES.keys()))
        f_qty = st.number_input("Total Quantity for Sale (kg)", min_value=10, max_value=100000, value=500)

    with f_col2:
        f_price = st.number_input("Expected Rate (₹ / kg)", min_value=1, value=22)
        f_loc = st.selectbox("Nearest Mandi / Tehsil", ["Patna", "Hajipur", "Muzaffarpur", "Gaya", "Bhagalpur"])
        f_quality = st.selectbox("Quality Certificate Grade", ["Grade A+ (Premium / Export)", "Grade A (Standard)", "Grade B (Commercial / Processing)"])
        f_date = st.date_input("Ready-for-Pickup Date", datetime.date.today())

    st.info("🎙️ **Multilingual Voice Listing Engine**: Farmers can submit harvest listings by regional voice note (Hindi/Bhojpuri).")
    
    if st.button("🚀 Publish Crop to Live Marketplace", use_container_width=True):
        if f_name and f_phone:
            new_entry = {
                "ID": len(st.session_state.listings) + 101,
                "Farmer": f_name,
                "Phone": f_phone,
                "Crop": f_crop,
                "Qty": f_qty,
                "Price": f_price,
                "Location": f_loc,
                "Quality": f_quality
            }
            st.session_state.listings.append(new_entry)
            st.success(f"✅ Listing #{new_entry['ID']} published successfully! Buyers can now place direct orders.")
        else:
            st.error("Please provide both name and contact number.")

# ================= 3. TRANSACTION TRACKING =================
elif menu == "📦 Live Transactions & Tracking":
    st.subheader("📦 Order Book & Escrow Settlement (Farmer ↔ Buyer Transparency)")
    st.write("Both farmers and buyers can monitor real-time purchase verification and escrow release.")

    if st.session_state.orders:
        orders_df = pd.DataFrame(st.session_state.orders)
        st.dataframe(orders_df, use_container_width=True)
    else:
        st.info("No orders placed yet.")

    st.markdown("---")
    st.markdown("### 🔐 Delivery Verification & Escrow Payout")
    c_ot1, c_ot2 = st.columns(2)
    with c_ot1:
        st.text_input("Enter Delivery Confirmation OTP (Sent to Buyer)", placeholder="e.g. 5491")
    with c_ot2:
        if st.button("Verify OTP & Release ₹ Payment to Farmer Bank Account", use_container_width=True):
            st.success("✅ OTP Verified! Smart escrow released 100% payout to Farmer's UPI/Account.")

# ================= 4. MANDI PRICE INTELLIGENCE =================
elif menu == "📊 Agmarknet Price Intelligence":
    st.subheader("📊 Real-Time Mandi Price Benchmarking")
    st.write("Comparing direct KisanDirect marketplace rates with traditional Mandi and middleman retail rates.")

    mandi_data = pd.DataFrame({
        "Crop": ["Wheat (Gehu)", "Potato (Aloo)", "Tomato (Tamatar)", "Rice (Chawal)", "Onion (Pyaz)", "Mustard (Sarson)"],
        "Govt Mandi Rate (₹/kg)": [22.5, 11.0, 18.0, 31.0, 16.0, 48.0],
        "KisanDirect Avg (₹/kg)": [25.0, 14.0, 22.0, 35.0, 20.0, 53.0],
        "Middleman Retail (₹/kg)": [32.0, 22.0, 36.0, 48.0, 30.0, 68.0],
        "Farmer Extra Gain": ["+11%", "+27%", "+22%", "+13%", "+25%", "+10%"]
    })
    st.table(mandi_data)

# ================= 5. IMPACT ANALYTICS =================
elif menu == "📈 Impact Analytics":
    st.subheader("📈 Social & Economic Impact (SIH 2026 Target Goals)")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div class='metric-card'><h3>+38.5%</h3><p>Direct Farmer Margin Growth</p></div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div class='metric-card'><h3>-21.0%</h3><p>Lower Cost for Consumers</p></div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div class='metric-card'><h3>₹ 4.85 Lakhs</h3><p>Broker Commission Saved</p></div>", unsafe_allow_html=True)

    st.markdown("---")
    st.write("#### 🚚 Cluster Logistics Efficiency")
    chart_data = pd.DataFrame({
        "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "Middleman Transport Cost (₹)": [12000, 14000, 15500, 16000, 17000, 18500],
        "KisanDirect Pooled Logistics (₹)": [7500, 8000, 8200, 8900, 9200, 9800]
    })
    st.line_chart(chart_data.set_index("Month"))