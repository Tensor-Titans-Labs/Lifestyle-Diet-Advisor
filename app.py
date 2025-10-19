import streamlit as st
import google.generativeai as genai
from gemini_api_key import GEMINI_API_KEY
import json
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="Lifestyle & Diet Advisor",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for premium UI
st.markdown("""
<style>
    /* Import Google Fonts */
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap');
    
    /* Main background with gradient */
    .stApp {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Poppins', sans-serif;
    }
    
    .main {
        background: transparent;
    }
    
    /* Glass morphism container */
    .glass-container {
        background: rgba(255, 255, 255, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 30px;
        padding: 3rem;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.37);
        border: 1px solid rgba(255, 255, 255, 0.18);
        margin: 2rem auto;
        max-width: 1400px;
    }
    
    /* Animated header */
    .main-header {
        font-size: 3.5rem;
        font-weight: 700;
        background: linear-gradient(120deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 0.5rem;
        animation: gradient 3s ease infinite;
        background-size: 200% 200%;
    }
    
    @keyframes gradient {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .sub-header {
        text-align: center;
        color: #666;
        font-size: 1.2rem;
        margin-bottom: 3rem;
        font-weight: 300;
    }
    
    /* Premium section headers */
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #2d3748;
        margin: 2rem 0 1.5rem 0;
        padding: 1rem 1.5rem;
        background: linear-gradient(135deg, #667eea15 0%, #764ba215 100%);
        border-radius: 15px;
        border-left: 4px solid #667eea;
        display: flex;
        align-items: center;
        transition: all 0.3s ease;
    }
    
    .section-header:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.2);
    }
    
    /* Enhanced input styling */
    .stSelectbox label, .stMultiSelect label, .stSlider label, .stRadio label, 
    .stNumberInput label, .stTextArea label {
        font-size: 0.95rem;
        font-weight: 600;
        color: #2d3748 !important;
        margin-bottom: 0.5rem;
    }
    
    div[data-baseweb="select"] > div,
    div[data-baseweb="input"] > div {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
        background: white;
    }
    
    div[data-baseweb="select"] > div:hover,
    div[data-baseweb="input"] > div:hover {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    
    div[data-baseweb="select"] > div:focus-within,
    div[data-baseweb="input"] > div:focus-within {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
    }
    
    /* Gradient sliders */
    .stSlider > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    /* Premium button */
    .stButton>button {
        width: 100%;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-weight: 600;
        padding: 1rem 2rem;
        border-radius: 15px;
        border: none;
        font-size: 1.2rem;
        transition: all 0.3s ease;
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.3);
        margin-top: 2rem;
    }
    
    .stButton>button:hover {
        transform: translateY(-3px);
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
    }
    
    /* Score card with animation */
    .score-card {
        padding: 2.5rem;
        border-radius: 25px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        box-shadow: 0 20px 60px rgba(102, 126, 234, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .score-card::before {
        content: '';
        position: absolute;
        top: -50%;
        left: -50%;
        width: 200%;
        height: 200%;
        background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 70%);
        animation: rotate 10s linear infinite;
    }
    
    @keyframes rotate {
        0% { transform: rotate(0deg); }
        100% { transform: rotate(360deg); }
    }
    
    .health-score {
        font-size: 5rem;
        font-weight: 700;
        margin: 1rem 0;
        position: relative;
        z-index: 1;
    }
    
    /* Metric cards */
    .metric-card {
        padding: 1.5rem;
        border-radius: 20px;
        background: white;
        box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        margin: 1rem 0;
        border: 1px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 8px 30px rgba(102, 126, 234, 0.15);
        border-color: #667eea;
    }
    
    /* Recommendation box */
    .recommendation-box {
        padding: 2rem;
        border-radius: 20px;
        background: white;
        margin: 1rem 0;
        border: 2px solid #e2e8f0;
        box-shadow: 0 4px 20px rgba(0,0,0,0.05);
        color: #2d3748;
        line-height: 1.8;
        transition: all 0.3s ease;
    }
    
    .recommendation-box:hover {
        box-shadow: 0 8px 30px rgba(0,0,0,0.1);
    }
    
    /* Tab styling */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1rem;
        background: transparent;
    }
    
    .stTabs [data-baseweb="tab"] {
        border-radius: 15px;
        padding: 1rem 2rem;
        background: white;
        border: 2px solid #e2e8f0;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .stTabs [data-baseweb="tab"]:hover {
        border-color: #667eea;
        background: #667eea10;
    }
    
    .stTabs [data-baseweb="tab"][aria-selected="true"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-color: transparent;
    }
    
    /* Progress bar */
    .stProgress > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Info boxes */
    .stAlert {
        border-radius: 15px;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
    }
    
    /* Divider */
    .input-divider {
        height: 1px;
        background: linear-gradient(90deg, transparent, #e2e8f0, transparent);
        margin: 2rem 0;
    }
    
    /* Form container */
    [data-testid="stForm"] {
        background: transparent;
        border: none;
    }
    
    /* Smooth animations */
    * {
        transition: all 0.2s ease;
    }
    
    /* Text area styling */
    .stTextArea textarea {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
        background: white;
    }
    
    .stTextArea textarea:focus {
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.2);
    }
    
    /* Number input */
    .stNumberInput input {
        border-radius: 12px;
        border: 2px solid #e2e8f0;
    }
    
    /* Radio buttons */
    .stRadio > label {
        background: white;
        padding: 0.5rem;
        border-radius: 10px;
    }
    
    /* Multiselect */
    .stMultiSelect [data-baseweb="tag"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 8px;
    }
    
    /* Welcome card */
    .welcome-card {
        background: white;
        padding: 3rem;
        border-radius: 25px;
        box-shadow: 0 10px 40px rgba(0,0,0,0.1);
        text-align: center;
    }
    
    .welcome-card h3 {
        color: #2d3748;
        margin-bottom: 1.5rem;
    }
    
    .feature-grid {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: 1.5rem;
        margin: 2rem 0;
    }
    
    .feature-item {
        background: linear-gradient(135deg, #667eea10 0%, #764ba210 100%);
        padding: 1.5rem;
        border-radius: 15px;
        border: 2px solid #e2e8f0;
        transition: all 0.3s ease;
    }
    
    .feature-item:hover {
        transform: translateY(-5px);
        border-color: #667eea;
        box-shadow: 0 10px 25px rgba(102, 126, 234, 0.15);
    }
</style>
""", unsafe_allow_html=True)

# Initialize Gemini API
try:
    genai.configure(api_key=GEMINI_API_KEY)
    model = genai.GenerativeModel('gemini-2.0-flash-exp')
except Exception as e:
    st.error(f"⚠️ API Configuration Error: {str(e)}")

# Initialize session state
if 'recommendations' not in st.session_state:
    st.session_state.recommendations = None
if 'lifestyle_score' not in st.session_state:
    st.session_state.lifestyle_score = None
if 'show_form' not in st.session_state:
    st.session_state.show_form = True

# Header
st.markdown('<div class="glass-container">', unsafe_allow_html=True)
st.markdown('<h1 class="main-header">🌱 Lifestyle & Diet Advisor</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">AI-Powered Personalized Health & Wellness Recommendations</p>', unsafe_allow_html=True)

# Show form or recommendations based on state
if st.session_state.show_form:
    st.markdown("---")
    
    with st.form("lifestyle_form"):
        # Diet & Nutrition Section
        st.markdown('<div class="section-header">🍽️ Diet & Nutrition</div>', unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            diet_type = st.selectbox(
                "Primary Diet Type",
                ["Omnivore", "Vegetarian", "Vegan", "Pescatarian", "Keto", "Paleo", "Mediterranean"],
                help="Select your primary dietary preference"
            )
        with col2:
            meals_per_day = st.slider("Meals per Day", 1, 6, 3, help="How many meals do you typically eat?")
        with col3:
            water_intake = st.slider("Water Intake (glasses/day)", 0, 15, 8, help="Recommended: 8-10 glasses")
        
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Sleep & Recovery Section
        st.markdown('<div class="section-header">💤 Sleep & Recovery</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            sleep_hours = st.slider("Average Sleep (hours/night)", 3, 12, 7, help="Recommended: 7-9 hours")
        with col2:
            sleep_quality = st.select_slider(
                "Sleep Quality",
                options=["Very Poor", "Poor", "Fair", "Good", "Excellent"],
                help="How would you rate your sleep quality?"
            )
        
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Physical Activity Section
        st.markdown('<div class="section-header">🏃 Physical Activity</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            exercise_frequency = st.selectbox(
                "Exercise Frequency",
                ["Sedentary", "1-2 times/week", "3-4 times/week", "5-6 times/week", "Daily"],
                help="How often do you exercise?"
            )
        with col2:
            exercise_type = st.multiselect(
                "Exercise Types",
                ["Cardio", "Strength Training", "Yoga", "Sports", "Walking", "Cycling", "Swimming"],
                help="Select all that apply"
            )
        
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Mental Health Section
        st.markdown('<div class="section-header">🧘 Mental Health & Wellness</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            stress_level = st.select_slider(
                "Stress Level",
                options=["Very Low", "Low", "Moderate", "High", "Very High"],
                help="How stressed do you feel on average?"
            )
        with col2:
            meditation = st.radio(
                "Do you meditate?", 
                ["Yes, regularly", "Sometimes", "No"],
                help="Meditation can help reduce stress"
            )
        
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Lifestyle Habits Section
        st.markdown('<div class="section-header">🚭 Lifestyle Habits</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            smoking = st.radio(
                "Smoking Status", 
                ["Non-smoker", "Occasional", "Regular"],
                help="Your smoking habits"
            )
        with col2:
            alcohol = st.selectbox(
                "Alcohol Consumption",
                ["None", "Occasional (1-2/week)", "Moderate (3-5/week)", "Regular (daily)"],
                help="How often do you consume alcohol?"
            )
        
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Personal Information Section
        st.markdown('<div class="section-header">👤 Personal Information</div>', unsafe_allow_html=True)
        
        col1, col2 = st.columns(2)
        with col1:
            age = st.number_input("Age", min_value=15, max_value=100, value=30, help="Your current age")
        with col2:
            health_goals = st.text_area(
                "Health Goals (optional)",
                placeholder="e.g., Weight loss, Muscle gain, Better energy...",
                help="What are your main health objectives?"
            )
        
        submit_button = st.form_submit_button("✨ Generate My Personalized Plan")

    if submit_button:
        with st.spinner("🔮 Analyzing your lifestyle and crafting personalized recommendations..."):
            try:
                # Prepare data for Gemini
                prompt = f"""
                As a professional health and lifestyle advisor, analyze the following user profile and provide comprehensive recommendations:

                User Profile:
                - Age: {age}
                - Diet Type: {diet_type}
                - Meals per Day: {meals_per_day}
                - Water Intake: {water_intake} glasses/day
                - Sleep: {sleep_hours} hours/night, Quality: {sleep_quality}
                - Exercise: {exercise_frequency}, Types: {', '.join(exercise_type) if exercise_type else 'None'}
                - Stress Level: {stress_level}
                - Meditation: {meditation}
                - Smoking: {smoking}
                - Alcohol: {alcohol}
                - Health Goals: {health_goals if health_goals else 'General wellness'}

                Please provide:
                1. A lifestyle health score (0-100)
                2. Detailed recommendations in these categories:
                   - Diet & Nutrition (specific meal suggestions, timing, portions)
                   - Hydration (optimal intake, timing)
                   - Sleep Optimization (sleep hygiene tips)
                   - Exercise Plan (specific activities, duration, frequency)
                   - Stress Management (practical techniques)
                   - Habit Modifications (lifestyle changes)
                3. A personalized action plan with 3-5 immediate steps
                4. Potential health risks to watch for based on current lifestyle

                Format the response with clear headings and bullet points for easy reading.
                """
                
                # Call Gemini API
                response = model.generate_content(prompt)
                recommendations_text = response.text
                
                # Calculate lifestyle score
                score = 0
                score += min(water_intake * 5, 40)
                score += min(sleep_hours * 5, 35)
                if sleep_quality in ["Good", "Excellent"]: score += 10
                if exercise_frequency in ["3-4 times/week", "5-6 times/week", "Daily"]: score += 15
                if stress_level in ["Very Low", "Low"]: score += 10
                if smoking == "Non-smoker": score += 10
                if alcohol in ["None", "Occasional (1-2/week)"]: score += 5
                score = min(score, 100)
                
                st.session_state.recommendations = recommendations_text
                st.session_state.lifestyle_score = score
                st.session_state.show_form = False
                st.rerun()
                
            except Exception as e:
                st.error(f"⚠️ Unable to fetch recommendations. Please check your API key and try again.")
                st.error(f"Error details: {str(e)}")

else:
    # Display recommendations
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        score = st.session_state.lifestyle_score
        
        if score >= 80:
            level = "Excellent"
            color = "#10b981"
            emoji = "🌟"
        elif score >= 60:
            level = "Good"
            color = "#84fab0"
            emoji = "✅"
        elif score >= 40:
            level = "Fair"
            color = "#fbbf24"
            emoji = "⚠️"
        else:
            level = "Needs Improvement"
            color = "#ef4444"
            emoji = "🔔"
        
        st.markdown(f"""
        <div class="score-card">
            <h3 style="margin: 0; font-size: 1.5rem;">Your Lifestyle Score</h3>
            <div class="health-score" style="color: {color};">{score}</div>
            <h2 style="margin: 0; font-size: 2rem;">{emoji} {level}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        st.progress(score / 100)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Display recommendations in tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Full Report", "🥗 Nutrition", "💪 Fitness", "🧠 Wellness"])
    
    with tab1:
        st.markdown("### 🎯 Your Personalized Health Plan")
        recommendations_html = st.session_state.recommendations.replace('\n', '<br>')
        st.markdown(f'<div class="recommendation-box">{recommendations_html}</div>', 
                   unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 🥗 Nutrition Guidelines")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Current Diet", diet_type, help="Your dietary preference")
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Daily Water", f"{water_intake} glasses", help="Current hydration")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.info("💡 **Nutrition Tip**: Balance your macros - aim for a mix of proteins, healthy fats, and complex carbs at each meal!")
    
    with tab3:
        st.markdown("### 💪 Fitness Overview")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Exercise Frequency", exercise_frequency)
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Activities", ", ".join(exercise_type) if exercise_type else "None")
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.success("🎯 **Fitness Goal**: Aim for 150 minutes of moderate-intensity activity weekly!")
    
    with tab4:
        st.markdown("### 🧠 Mental Wellness")
        
        col1, col2 = st.columns(2)
        with col1:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Sleep Duration", f"{sleep_hours} hours")
            st.metric("Sleep Quality", sleep_quality)
            st.markdown('</div>', unsafe_allow_html=True)
        with col2:
            st.markdown('<div class="metric-card">', unsafe_allow_html=True)
            st.metric("Stress Level", stress_level)
            st.metric("Meditation", meditation)
            st.markdown('</div>', unsafe_allow_html=True)
        
        st.warning("🌙 **Sleep Tip**: Create a consistent bedtime routine and aim for 7-9 hours of quality sleep!")
    
    # Button to start over
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("🔄 Create New Assessment"):
        st.session_state.show_form = True
        st.session_state.recommendations = None
        st.session_state.lifestyle_score = None
        st.rerun()

# Welcome screen when no recommendations yet
if st.session_state.show_form and st.session_state.recommendations is None:
    st.markdown("---")
    st.markdown("""
    <div class="welcome-card">
        <h3>👋 Welcome to Your Personal AI Health Advisor!</h3>
        <p style="font-size: 1.1rem; color: #666; margin-bottom: 2rem;">
            Transform your lifestyle with personalized, AI-powered recommendations
        </p>
        <div class="feature-grid">
            <div class="feature-item">
                <h4>📊 Smart Analysis</h4>
                <p>Advanced AI analyzes your unique lifestyle profile</p>
            </div>
            <div class="feature-item">
                <h4>🎯 Personalized Plan</h4>
                <p>Get tailored recommendations just for you</p>
            </div>
            <div class="feature-item">
                <h4>💡 Actionable Steps</h4>
                <p>Receive practical, easy-to-follow guidance</p>
            </div>
            <div class="feature-item">
                <h4>🌟 Holistic Approach</h4>
                <p>Cover diet, fitness, sleep, and mental wellness</p>
            </div>
        </div>
        <p style="margin-top: 2rem; color: #667eea; font-weight: 600;">
            Fill out the form above to get started on your wellness journey! ⬆️
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: white; padding: 2rem 0;'>
    <p style='font-size: 1.1rem;'><strong>🌱 Lifestyle & Diet Advisor</strong> | Powered by Google Gemini AI</p>
    <p style='font-size: 0.9rem; opacity: 0.8;'>⚠️ Disclaimer: This tool provides general wellness guidance. Always consult healthcare professionals for medical advice.</p>
</div>
""", unsafe_allow_html=True)
