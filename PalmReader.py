import streamlit as st
from PIL import Image
from litellm import completion
import instructor
import io
from pydantic import BaseModel, Field
from pathlib import Path
import base64


class PalmResult(BaseModel):
    suitable: bool = Field(
        ..., description="Indicates if the image is suitable for palm reading"
    )
    english: str | None = Field(
        None, description="The palm reading explanation in English"
    )
    turkish: str | None = Field(
        None, description="The palm reading explanation in Turkish"
    )


LLM_API_KEY = st.secrets["LLM_API_KEY"]
LLM_MODEL = st.secrets["LLM_MODEL"]
PROMPT = Path("prompt.md").read_text()

client = instructor.from_litellm(completion, mode=instructor.Mode.JSON)

st.set_page_config(page_title="AI Palm Reader", page_icon="🔮")
st.title("🔮 AI Palm Reader")
st.caption(
    "Upload or capture a photo of your palm and receive a mystical AI reading ✋"
)

input_mode = st.radio("Choose input method", ["📁 Upload Image", "📸 Use Camera"])

image_data = None

match input_mode:
    case "📁 Upload Image":
        uploaded_file = st.file_uploader(
            "Upload an image of your palm", type=["jpg", "jpeg", "png"]
        )
        if uploaded_file:
            image_data = uploaded_file.read()
            img = Image.open(io.BytesIO(image_data))
            st.markdown(
                "<div style='display: flex; justify-content: center;'><img src='data:image/png;base64,"
                + base64.b64encode(image_data).decode()
                + "' width='200' style='border-radius: 10px;'/></div>",
                unsafe_allow_html=True,
            )

    case "📸 Use Camera":
        camera_image = st.camera_input("Take a picture of your palm")
        if camera_image:
            image_data = camera_image.getvalue()
            img = Image.open(io.BytesIO(image_data))
            st.markdown(
                "<div style='display: flex; justify-content: center;'><img src='data:image/png;base64,"
                + base64.b64encode(image_data).decode()
                + "' width='200' style='border-radius: 10px;'/></div>",
                unsafe_allow_html=True,
            )

# Palm reading
if image_data:
    with st.spinner("🔮 Reading your palm..."):
        base64_image = base64.b64encode(image_data).decode("utf-8")
        try:
            response = client.chat.completions.create(
                api_key=LLM_API_KEY,
                model=LLM_MODEL,
                messages=[
                    {"role": "system", "content": PROMPT},
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "image_url",
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{base64_image}",
                                },
                            },
                        ],
                    },
                ],
                response_model=PalmResult,
            )
            if response.suitable:
                eng_text = response.english
                tr_text = response.turkish

                st.markdown("## 🧙‍♂️ Your Palm Explanation | Fal Açıklamanız")

                st.markdown("### English Explanation")
                st.write(eng_text)

                st.markdown("### Türkçe Açıklama")
                st.write(tr_text)

            else:
                st.error(
                    "The AI couldn't detect a clear palm in the image. Please make sure your hand is clearly visible with good lighting and try again."
                )

        except Exception as e:
            st.error(f"Error generating palm reading: {e}")
            with st.expander("Debug Information"):
                st.write(f"Full error: {str(e)}")
                st.write(f"Error type: {type(e)}")
