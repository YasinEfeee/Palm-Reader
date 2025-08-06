# 🔮 AI Palm Reader

A fun and mystical AI-powered palm reading application that analyzes palm images using Google's Gemini AI model. Get instant palm readings in both English and Turkish!

🌐 **Live Demo**: [Try it out!](https://palm-reader-ai.streamlit.app/)

## 🌟 Features

- 📸 Upload a palm image or use your device's camera
- 🔍 AI-powered palm analysis using Google's Gemini model
- 🌍 Bilingual support (English and Turkish)
- 🎨 Clean and intuitive Streamlit interface
- 📱 Mobile-friendly design

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Gemini API key
- Required Python packages (install via `pip install -r requirements.txt`)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/palm-reader.git
   cd palm-reader
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the project root and add your Gemini API key:
   ```
   GEMINI_API_KEY=your_api_key_here
   ```

   Alternatively, you can set up your API key in Streamlit secrets when deploying.

### Running Locally

Run the Streamlit app:
```bash
streamlit run PalmReader.py
```

## 🤖 How It Works

1. Choose your preferred input method: upload an image or use your camera
2. Take a clear photo of your palm or upload an existing image
3. Click "Read My Palm" and let the AI analyze your palm lines
4. Receive your personalized palm reading in both English and Turkish

## 📝 Requirements

- streamlit>=1.31.0
- Pillow>=10.0.0
- python-dotenv>=1.0.0
- google-generativeai>=0.3.0

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Powered by Google's Gemini AI
- Built with Streamlit