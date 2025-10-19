# 🌱 Lifestyle & Diet Advisor

An AI-powered health and wellness application that provides personalized lifestyle recommendations based on your daily habits, diet, exercise routine, and mental wellness practices.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![Google Gemini](https://img.shields.io/badge/Google-Gemini%20AI-orange.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Technology Stack](#technology-stack)
- [Project Structure](#project-structure)
- [Screenshots](#screenshots)
- [How It Works](#how-it-works)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

## 🎯 Overview

The **Lifestyle & Diet Advisor** is an intelligent health companion that analyzes your lifestyle habits across multiple dimensions and provides comprehensive, personalized recommendations to help you achieve your wellness goals. Using Google's advanced Gemini AI, the application delivers expert-level advice tailored to your unique profile.

## ✨ Features

### 🔍 Comprehensive Health Assessment
- **Diet & Nutrition Analysis**: Track your diet type, meal frequency, and water intake
- **Sleep Monitoring**: Evaluate sleep duration and quality
- **Physical Activity**: Assess exercise frequency and types
- **Mental Wellness**: Monitor stress levels and meditation practices
- **Lifestyle Habits**: Review smoking and alcohol consumption

### 🤖 AI-Powered Recommendations
- Personalized meal suggestions with timing and portions
- Custom exercise plans tailored to your fitness level
- Sleep optimization strategies and bedtime routines
- Stress management techniques and mindfulness practices
- Habit modification strategies for long-term wellness

### 📊 Lifestyle Score System
- Real-time health score calculation (0-100)
- Detailed breakdown by category:
  - Water Intake (max 40 points)
  - Sleep Duration (max 35 points)
  - Sleep Quality (10 points)
  - Exercise Frequency (15 points)
  - Stress Management (10 points)
  - Non-smoking Status (10 points)
  - Alcohol Moderation (5 points)
  - Meditation Practice (5 points)

### 📱 User-Friendly Interface
- Clean, modern design optimized for both desktop and mobile
- Interactive tabs for easy navigation
- Visual progress indicators
- Downloadable health reports in TXT format
- Mobile-responsive layout with high-contrast design

### 📄 Detailed Reporting
- Comprehensive health reports with all user data
- AI-generated personalized recommendations
- Score breakdown and analysis
- Timestamped for progress tracking
- Easy-to-share format

## 🖼️ Demo

### Main Assessment Form
Fill out comprehensive lifestyle information across multiple categories:
- Diet and nutrition preferences
- Sleep patterns and quality
- Exercise frequency and types
- Mental health and stress levels
- Lifestyle habits

### Results Dashboard
View your personalized results including:
- Overall lifestyle score with visual indicators
- Tabbed interface for different health aspects
- Detailed AI-generated recommendations
- Download and reassessment options

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Google Gemini API key

### Step-by-Step Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/lifestyle-diet-advisor.git
cd lifestyle-diet-advisor
```

2. **Create a virtual environment (recommended)**
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install required packages**
```bash
pip install -r requirements.txt
```

4. **Set up your API key**
Create a file named `gemini_api_key.py` in the project root:
```python
GEMINI_API_KEY = "your_gemini_api_key_here"
```

## ⚙️ Configuration

### Getting Your Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key and add it to `gemini_api_key.py`

### Requirements File

Create a `requirements.txt` file with the following dependencies:

```txt
streamlit==1.28.0
google-generativeai==0.3.1
```

## 💻 Usage

### Running the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

### Using the Application

1. **Fill Out the Assessment Form**
   - Enter your age and health goals
   - Select your diet type and eating patterns
   - Rate your sleep quality and duration
   - Choose your exercise frequency and types
   - Assess your stress levels and meditation habits
   - Report smoking and alcohol consumption

2. **Submit for Analysis**
   - Click "✅ Get My Recommendations"
   - Wait for AI analysis (typically 5-10 seconds)

3. **Review Your Results**
   - View your lifestyle score and rating
   - Navigate through different recommendation tabs
   - Read personalized advice for each health category

4. **Download or Reassess**
   - Download your complete health report
   - Start a new assessment to track progress

## 🛠️ Technology Stack

### Frontend
- **Streamlit**: Web application framework for Python
- **HTML/CSS**: Custom styling for enhanced UI/UX
- **Responsive Design**: Mobile-optimized interface

### Backend
- **Python 3.8+**: Core programming language
- **Google Gemini AI**: Advanced language model for recommendations

### AI/ML
- **Gemini 2.0 Flash Exp**: Latest Google AI model
- **Natural Language Processing**: Context-aware health advice
- **Personalization Engine**: Tailored recommendations based on user profile

## 📁 Project Structure

```
lifestyle-diet-advisor/
│
├── app.py                      # Main application file
├── gemini_api_key.py          # API key configuration (not in repo)
├── requirements.txt           # Python dependencies
├── README.md                  # Project documentation
│
├── .gitignore                 # Git ignore file
└── LICENSE                    # MIT License
```

## 📸 Screenshots

### Welcome Screen
Clean interface with easy-to-understand form sections

### Assessment Form
Organized sections covering all aspects of lifestyle:
- 🍽️ Diet & Nutrition
- 💤 Sleep & Recovery
- 🏃 Physical Activity
- 🧘 Mental Health & Wellness
- 🚭 Lifestyle Habits
- 👤 Personal Information

### Results Dashboard
- Score visualization with color-coded ratings
- Tabbed navigation (Overview, Nutrition, Fitness, Wellness)
- Comprehensive recommendations
- Action buttons for download and reassessment

## 🔬 How It Works

### 1. Data Collection
The application collects comprehensive lifestyle data across 8 key categories through an intuitive form interface.

### 2. Score Calculation
```python
Score Components:
- Water Intake: Up to 40 points (5 points per glass)
- Sleep Duration: Up to 35 points (5 points per hour)
- Sleep Quality: 10 points (Good/Excellent)
- Exercise: 15 points (regular activity)
- Stress Management: 10 points (Low stress)
- Non-smoking: 10 points
- Alcohol Moderation: 5 points
- Meditation: 5 points
Total Maximum: 100 points
```

### 3. AI Analysis
The application sends your profile to Google Gemini AI with a specialized prompt that requests:
- Lifestyle health score analysis
- Category-specific recommendations
- Personalized action plans
- Health risk assessments

### 4. Results Generation
- Real-time score calculation
- AI-powered personalized recommendations
- Formatted for easy reading and action
- Downloadable report generation

### 5. Report Download
Generates a comprehensive TXT report including:
- Timestamp
- Complete user profile
- Lifestyle score with breakdown
- Full AI recommendations
- Health disclaimer

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/AmazingFeature
   ```
3. **Commit your changes**
   ```bash
   git commit -m 'Add some AmazingFeature'
   ```
4. **Push to the branch**
   ```bash
   git push origin feature/AmazingFeature
   ```
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guidelines for Python code
- Add comments for complex logic
- Test on both desktop and mobile browsers
- Update documentation for new features

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Contact

**MD Zaheer JK**

- GitHub: [@mdzaheerjk](https://github.com/mdzaheerjk)
- Email: your.email@example.com
- LinkedIn: [your-linkedin-profile](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- **Google Gemini AI** for providing the powerful language model
- **Streamlit** for the amazing web framework
- **Open Source Community** for inspiration and support

## ⚠️ Disclaimer

This application provides general wellness guidance based on lifestyle factors. It is **NOT** a substitute for professional medical advice, diagnosis, or treatment. Always consult with qualified healthcare professionals for medical concerns and before making significant changes to your diet, exercise, or lifestyle.

## 🔮 Future Enhancements

- [ ] User authentication and profile saving
- [ ] Progress tracking over time
- [ ] Integration with fitness trackers
- [ ] Meal planning and recipe suggestions
- [ ] Community features and goal sharing
- [ ] Multi-language support
- [ ] Mobile app (iOS/Android)
- [ ] PDF report generation with charts
- [ ] Email notifications for follow-ups
- [ ] Integration with healthcare providers

## 📊 Version History

### Version 1.0.0 (Current)
- Initial release
- Basic lifestyle assessment
- AI-powered recommendations
- Score calculation system
- Report download feature
- Mobile-responsive design

---

**Made with ❤️ by MD Zaheer JK**

**Powered by Google Gemini AI**
