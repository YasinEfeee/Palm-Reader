# 🔮 AI Palm Reader

A mystical AI-powered palm reading application that analyzes palm images using advanced vision language models. Get instant, personalized palm readings in both English and Turkish with poetic, mystical insights about your personality, life path, and future opportunities.

🌐 **Live Demo**: [Try it out!](https://palm-reader-ai.streamlit.app/)

## 🌟 Features

- 📸 **Dual Input Methods**: Upload palm images or capture them directly with your device's camera
- 🤖 **AI-Powered Analysis**: Uses LiteLLM with structured outputs via Instructor for reliable palm reading generation
- 🌍 **Bilingual Support**: Simultaneous readings in English and Turkish with mystical, poetic tone
- 🎨 **Elegant Interface**: Clean, responsive Streamlit design optimized for both desktop and mobile
- 🧙‍♂️ **Mystical Insights**: Comprehensive readings covering personality traits, life path, emotions, and predictions
- ✨ **Smart Detection**: Intelligent palm detection that works even with partially visible or unclear hand images

## 🚀 Getting Started

### Prerequisites

- **Python 3.12 or higher**
- **uv package manager** (recommended but optional)
- **LiteLLM compatible API key** from any supported provider (OpenAI, Anthropic, Google, etc.)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YasinEfeee/Palm-Reader.git
   cd Palm-Reader
   ```

2. **Install dependencies:**

   Using `uv` (recommended):
   ```bash
   uv sync
   ```

   Or using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure your API credentials:**

   Create a `.streamlit/secrets.toml` file in the project root:
   ```toml
   LLM_API_KEY = "your_api_key_here"
   LLM_MODEL = "your_model_name_here"  # it must support vision capabilities
   ```

   **Supported models**: Any vision-capable model from LiteLLM's provider list is supported.
   - See [LiteLLM Models](https://models.litellm.ai) for full list.

### Running the Application

**Local Development:**
```bash
uv run streamlit run PalmReader.py
```

**Alternative (if uv not available):**
```bash
streamlit run PalmReader.py
```

The app will be available at `http://localhost:8501`

## 🤖 How It Works

The application combines modern AI technology with mystical palm reading traditions:

1. **Image Capture**: Choose between uploading an existing palm image or capturing one directly using your device's camera
2. **AI Analysis**: The image is processed by a vision-language model using structured outputs via the Instructor library
3. **Palm Detection**: Smart detection system identifies hands even in partially visible or unclear images
4. **Mystical Generation**: AI generates comprehensive palm readings covering:
   - **Personality Traits**: Hidden strengths and character insights
   - **Life Path**: Future opportunities and personal growth
   - **Emotional Nature**: Relationship patterns and emotional depth
   - **Mystical Predictions**: Inspiring forecasts about your journey
5. **Dual Language Output**: Receive your reading in both English and Turkish with poetic, mystical language

## 🏗️ Technical Architecture

- **Frontend**: Streamlit with responsive design and camera integration
- **AI Integration**: LiteLLM for multi-provider LLM access
- **Structured Output**: Instructor (Pydantic) for reliable response parsing
- **Image Processing**: PIL for image handling and base64 encoding
- **Dependencies**: Modern Python stack with uv package management

## 🙏 Acknowledgments

- **[LiteLLM](https://github.com/BerriAI/litellm)** - Universal LLM API for seamless model integration
- **[Instructor](https://github.com/jxnl/instructor)** - Structured outputs for reliable AI responses  
- **[Streamlit](https://streamlit.io/)** - Beautiful web apps for machine learning and data science
- **[Pydantic](https://pydantic.dev/)** - Data validation using Python type annotations
