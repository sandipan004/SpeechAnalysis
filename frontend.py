import streamlit as st
import requests

# API Configuration
API_URL = "http://localhost:8000/predict"

# Set page config
st.set_page_config(
    page_title="SpeechAnalysis",
    page_icon="🎙️",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
<style>
    .stProgress .st-bo {
        background-color: #6366f1;
    }
    .metric-safe {
        color: #10b981;
        font-weight: bold;
    }
    .metric-danger {
        color: #ef4444;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.title("SpeechAnalysis 🎙️")
st.markdown("AI-powered toxicity detection using classical Machine Learning models.")

# Input area
st.subheader("Analyze Text")
user_input = st.text_area("Enter a comment or message to analyze:", height=150, placeholder="Type something here...")

# Analyze button
if st.button("Analyze Text", type="primary"):
    if not user_input.strip():
        st.warning("Please enter some text to analyze.")
    else:
        with st.spinner("Analyzing toxicity..."):
            try:
                # Make POST request to FastAPI backend
                response = requests.post(API_URL, json={"text": user_input})
                
                if response.status_code == 200:
                    results = response.json()
                    
                    st.success("Analysis Complete!")
                    st.subheader("Results")
                    
                    # Display results with progress bars
                    for category, probability in results.items():
                        # Convert to percentage
                        percentage = int(probability * 100)
                        
                        col1, col2 = st.columns([1, 4])
                        with col1:
                            st.write(f"**{category.replace('_', ' ').title()}**")
                        with col2:
                            # Use Streamlit's progress bar
                            st.progress(percentage)
                            
                            # Display status text
                            if percentage > 50:
                                st.markdown(f"<span class='metric-danger'>{percentage}% Detected</span>", unsafe_allow_html=True)
                            else:
                                st.markdown(f"<span class='metric-safe'>{percentage}% Safe</span>", unsafe_allow_html=True)
                                
                        st.divider()
                else:
                    st.error(f"Error from API: {response.status_code}")
                    
            except requests.exceptions.ConnectionError:
                st.error("Failed to connect to the backend API. Please make sure the FastAPI server is running on localhost:8000.")
            except Exception as e:
                st.error(f"An unexpected error occurred: {e}")
