import streamlit as st
from PIL import Image
import google.generativeai as genai
import io
from dotenv import load_dotenv


load_dotenv()

api_key = st.secrets["GEMINI_API_KEY"]

# Configure Gemini
genai.configure(api_key)
model = genai.GenerativeModel("gemini-2.5-flash")

st.set_page_config(page_title="AI Palm Reader", page_icon="🔮")
st.title("🔮 AI Palm Reader")
st.caption("Upload or capture a photo of your palm and receive a mystical AI reading ✋")

# Input mode toggle
input_mode = st.radio("Choose input method", ["📁 Upload Image", "📸 Use Camera"])

image_data = None

if input_mode == "📁 Upload Image":
    uploaded_file = st.file_uploader("Upload an image of your palm", type=["jpg", "jpeg", "png"])
    if uploaded_file:
        image_data = uploaded_file.read()
        st.image(Image.open(io.BytesIO(image_data)), caption="Uploaded Palm", use_container_width=True)

elif input_mode == "📸 Use Camera":
    camera_image = st.camera_input("Take a picture of your palm")
    if camera_image:
        image_data = camera_image.getvalue()
        st.image(Image.open(io.BytesIO(image_data)), caption="Captured Palm", use_container_width=True)        

# Palm reading
if image_data:
    if st.button("🔍 Read My Palm"):
        with st.spinner("🔮 Reading your palm..."):
            image = Image.open(io.BytesIO(image_data))
            prompt = """
            You are a mystical palm reader with ancient knowledge. Analyze the uploaded palm image and generate a creative, fictional palm reading.

            Respond in **two parts**:
            1. 🇺🇸 **English Reading** — Write a one-paragraph palm reading including personality, life path, love life, and future predictions.
            2. 🇹🇷 **Turkish Reading** — Translate the English reading into fluent, natural Turkish.

            Format strictly like this:

            - 🇺🇸 English: <your English paragraph here>
            - 🇹🇷 Turkish: <your Turkish translation here>
            """
            try:  # Convert bytes to PIL.Image.Image
                response = model.generate_content([prompt, image], stream=True)
                full_output = "".join(chunk.text for chunk in response)
                
                # Split manually if needed
                eng_text = ""
                tr_text = ""
                if "- 🇺🇸 English:" in full_output and "- 🇹🇷 Turkish:" in full_output:
                    try:
                        eng_text = full_output.split("- 🇺🇸 English:")[1].split("- 🇹🇷 Turkish:")[0].strip()
                        tr_text = full_output.split("- 🇹🇷 Turkish:")[1].strip()
                    except:
                        eng_text = full_output
                else:
                    eng_text = full_output  # fallback in case formatting breaks
                    
                st.markdown("### 🧞 Your Palm Reading")
                
                st.markdown("## English Reading")
                st.write(eng_text)

                st.markdown("## Türkçe Yorum")
                st.write(tr_text)  
                
            except Exception as e:
                st.error(f"Error: {e}")