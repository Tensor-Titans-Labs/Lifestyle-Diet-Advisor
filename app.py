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

# Custom CSS for modern UI
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        font-weight: 700;
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin-bottom: 1rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .score-card {
        padding: 2rem;
        border-radius: 15px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    }
    .metric-card {
        padding: 1.5rem;
        border-radius: 12px;
        background: white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        margin: 0.5rem 0;
        border-left: 4px solid #667eea;
    }
    .recommendation-box {
        padding: 2rem;
        border-radius: 12px;
        background: #ffffff;
        margin: 1rem 0;
        border: 2px solid #e0e0e0;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        color: #1a1a1a;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: 600;
        color: #333;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #84fab0;
    }
    .stButton>button {
        width: 100%;
        background: linear-gradient(120deg, #84fab0 0%, #8fd3f4 100%);
        color: white;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
        border-radius: 10px;
        border: none;
        font-size: 1.1rem;
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 10px 25px rgba(132, 250, 176, 0.3);
    }
    .health-score {
        font-size: 4rem;
        font-weight: 700;
        margin: 1rem 0;
    }
    .input-section {
        background: transparent;
        padding: 2rem 0;
        margin: 1.5rem 0;
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
st.markdown('<h1 class="main-header">🌱 Lifestyle & Diet Advisor</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Get personalized recommendations powered by AI</p>', unsafe_allow_html=True)

# Show form or recommendations based on state
if st.session_state.show_form:
    # Main form on the main screen
    st.markdown("---")
    
    with st.form("lifestyle_form"):
        # Diet & Nutrition Section
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
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
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Sleep & Recovery Section
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
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
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Physical Activity Section
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
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
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Mental Health Section
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
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
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Lifestyle Habits Section
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
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
        st.markdown('</div>', unsafe_allow_html=True)
        st.markdown('<div class="input-divider"></div>', unsafe_allow_html=True)
        
        # Personal Information Section
        st.markdown('<div class="input-section">', unsafe_allow_html=True)
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
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        submit_button = st.form_submit_button("✨ Get Personalized Recommendations")

    if submit_button:
        with st.spinner("🔮 Analyzing your lifestyle and generating personalized recommendations..."):
            try:
                # Prepare data for Gemini
                user_data = {
                    "diet_type": diet_type,
                    "meals_per_day": meals_per_day,
                    "water_intake": water_intake,
                    "sleep_hours": sleep_hours,
                    "sleep_quality": sleep_quality,
                    "exercise_frequency": exercise_frequency,
                    "exercise_types": exercise_type,
                    "stress_level": stress_level,
                    "meditation": meditation,
                    "smoking": smoking,
                    "alcohol": alcohol,
                    "age": age,
                    "health_goals": health_goals
                }
                
                # Create detailed prompt for Gemini
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

                Format the response as structured sections with clear headings.
                """
                
                # Call Gemini API
                response = model.generate_content(prompt)
                recommendations_text = response.text
                
                # Calculate a simple lifestyle score based on inputs
                score = 0
                score += min(water_intake * 5, 40)  # Max 40 points for hydration
                score += min(sleep_hours * 5, 35)  # Max 35 points for sleep
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
        
        # Determine health level and color
        if score >= 80:
            level = "Excellent"
            color = "#00C853"
            emoji = "🌟"
        elif score >= 60:
            level = "Good"
            color = "#64DD17"
            emoji = "✅"
        elif score >= 40:
            level = "Fair"
            color = "#FFD600"
            emoji = "⚠️"
        else:
            level = "Needs Improvement"
            color = "#FF6D00"
            emoji = "🔔"
        
        st.markdown(f"""
        <div class="score-card">
            <h3>Your Lifestyle Score</h3>
            <div class="health-score" style="color: {color};">{score}</div>
            <h2>{emoji} {level}</h2>
        </div>
        """, unsafe_allow_html=True)
        
        # Progress bar
        st.progress(score / 100)
    
    st.markdown("---")
    
    # Display recommendations in tabs
    tab1, tab2, tab3, tab4 = st.tabs(["📊 Overview", "🥗 Diet Plan", "💪 Fitness", "🧠 Wellness"])
    
    with tab1:
        st.markdown("### 🎯 Your Personalized Recommendations")
        
        # Display recommendations with proper formatting
        recommendations_html = st.session_state.recommendations.replace('\n', '<br>')
        st.markdown(f'<div class="recommendation-box" style="line-height: 1.8;">{recommendations_html}</div>', 
                   unsafe_allow_html=True)
    
    with tab2:
        st.markdown("### 🥗 Nutrition Guidelines")
        st.info("💡 **Tip**: Distribute your meals evenly throughout the day and stay hydrated!")
        st.markdown(st.session_state.recommendations)
    
    with tab3:
        st.markdown("### 💪 Activity Overview")
        st.success("🎯 **Goal**: Aim for 150 minutes of moderate activity per week!")
        st.markdown(st.session_state.recommendations)
    
    with tab4:
        st.markdown("### 🧠 Mental Wellness")
        st.warning("🌙 **Tip**: Quality sleep is crucial for overall health. Aim for 7-9 hours nightly!")
        st.markdown(st.session_state.recommendations)
    
    # Button to start over
    st.markdown("---")
    if st.button("🔄 Start New Assessment"):
        st.session_state.show_form = True
        st.session_state.recommendations = None
        st.session_state.lifestyle_score = None
        st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: #666; padding: 2rem 0;'>
    <p>🌱 <strong>Lifestyle & Diet Advisor</strong> | Powered by Google Gemini AI</p>
    <p style='font-size: 0.9rem;'>⚠️ Disclaimer: This tool provides general wellness guidance. Always consult healthcare professionals for medical advice.</p>
</div>
""", unsafe_allow_html=True)
