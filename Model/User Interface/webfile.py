import streamlit as st
import os
from dotenv import load_dotenv
import base64
load_dotenv()

st.set_page_config(
    page_title="TRY OUTFIT",
    page_icon="logo.png",
)
def load_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode("utf-8")

# Default product image (encoded in base64)
product_image_base64 = None

# File uploader (hidden but used when 🖼️ button is clicked)
uploaded_file = st.file_uploader("", type=["jpg", "jpeg"], label_visibility="hidden")

if uploaded_file is not None:
    product_image_base64 = load_image(uploaded_file)

# If no uploaded image, load a default image
if product_image_base64 is None:
    with open("D:/Projects/TRY-ON/captured_image.jpeg", "rb") as img_file:
        product_image_base64 = base64.b64encode(img_file.read()).decode("utf-8")

# HTML for logo and small text
col1, col2 = st.columns([1, 7])

# To Showcase the Products
#st.markdown("<h2 style='color: #FFF;'>Product Showcase</h2>", unsafe_allow_html=True)

with col1:
    st.image("whitelogo.png", width=100)  # Display the logo with specified width

with col2:
    st.markdown("""
   <div style="display: flex; justify-content: space-between; align-items: center; height: 100px;">
        <div style="flex: 1; display: flex; flex-direction: column; justify-content: center;">
            <div style="font-size: 15px; color: #FFF; font-weight: bold; font-family: 'Rigot', sans-serif;">Try Outfit</div>
            <div style="font-size: 12px; color: #AAA; font-family: 'Rigot', sans-serif; margin-top: 3px;">Wear Your Standards</div>
        </div>
        <a href="#signup" style="text-decoration: none;">
            <button style="font-size: 14px; padding: 8px 16px; border: none; border-radius: 5px; background-color: #6A0D91; color: #FFF;font-weight: bold; cursor: pointer; margin-right: 10px;">Sign Up</button>
        </a>
        <a href="#login" style="text-decoration: none;">
            <button style="font-size: 14px; padding: 8px 16px; border: none; border-radius: 5px; background-color: #6A0D91; color: #FFF;font-weight: bold; cursor: pointer;">Login</button>
        </a>
    </div>
       """.format('whitelogo.png'), unsafe_allow_html=True)

# Display product image and details in one container with a border
st.markdown(f"""
    <div style="border: 2px solid #ADD8E6; padding: 20px; border-radius: 10px; margin-top: 20px; display: flex; background-color: ##808080;">
        <!-- Product Image -->
        <img src="data:image/jpeg;base64,{product_image_base64}" alt="Product Image" style="width: 200px; height: auto; margin-right: 20px; border-radius: 10px; border: 2px solid #ADD8E6;">
         <!-- Small Button at Bottom-Left -->
             <a href="#buy" style="text-decoration: none;">
               <button style="position: absolute; bottom: 10px; left: 160px; font-size: 17px; padding: 1px 13px; border: 2px solid #808080; border-radius: 10px; background-color: #FFF; color: #BEBEBE; cursor: pointer;">
                    🖼️
                </button>
            </a>
        <!-- Product Details -->
        <div style="flex: 1;">
            <h2 style="margin-bottom: 10px; color: #FFF;">Men's Polo Tshirt</h2>
            <p style="color: #888; font-size: 14px;">
                Pack of 2 Men Solid Polo Neck Cotton Blend Green, Blue T-Shirt
            </p>
            
        
    </div>
""", unsafe_allow_html=True)

# Sidebar for parameter selection
st.sidebar.subheader("Select the parameter:", divider='rainbow')

content_type = st.sidebar.radio(
    "Select Content type:",
    ["T-Shirts", "Jeans (Coming Soon!)", "Shoes (Coming Soon!)"],index=None,
)

if (content_type == "Jeans (Coming Soon!)") or (content_type == "Shoes (Coming Soon!)"):
    st.toast('Image Generation is not Supported Yet!', icon='🚫')
    st.sidebar.error("Can't Generate !, Select other Content Type")
