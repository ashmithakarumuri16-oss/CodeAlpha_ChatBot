"""
Flask Web Application for Advanced AI/ML Expert Chatbot
CodeAlpha AI Internship - Task 2 (Enhanced Version)
"""

from flask import Flask, render_template, request, jsonify
from advanced_chatbot import AdvancedAIMLChatbot

app = Flask(__name__)
bot = AdvancedAIMLChatbot()

# Store conversation sessions
sessions = {}

@app.route('/')
def home():
    """Render the main chatbot interface"""
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_bot_response():
    """Handle user messages and return chatbot responses"""
    user_message = request.json.get('message', '')
    session_id = request.json.get('session_id', 'default')
    
    if not user_message:
        return jsonify({'response': 'Please enter a message.'})
    
    # Get response from bot
    answer = bot.get_response(user_message)
    
    # Find topic match for confidence display
    best_match, confidence = bot.find_best_match(user_message)
    
    return jsonify({
        'response': answer,
        'confidence': round(confidence * 100, 1) if confidence > 0.3 else 0,
        'topic': best_match if confidence > 0.3 else None
    })

@app.route('/get_topics', methods=['GET'])
def get_topics():
    """Return list of available topics"""
    topics = [
        "What is Artificial Intelligence?",
        "Explain Machine Learning",
        "Tell me about Deep Learning",
        "What is NLP?",
        "Computer Vision applications",
        "Python for AI",
        "How to learn AI?",
        "AI Career opportunities",
        "About CodeAlpha internship"
    ]
    return jsonify({'topics': topics})

if __name__ == '__main__':
    print("\n" + "="*80)
    print("🤖 ADVANCED AI/ML EXPERT CHATBOT - Web Application Starting...")
    print("="*80)
    print("\n✨ Features:")
    print("   • Intelligent conversational responses")
    print("   • Deep knowledge of AI/ML topics")
    print("   • Career guidance and learning paths")
    print("   • CodeAlpha internship support")
    print("\n🌐 Open your browser and go to: http://127.0.0.1:5000")
    print("\n⌨️  Press CTRL+C to stop the server")
    print("="*80 + "\n")
    app.run(debug=True, host='0.0.0.0', port=5000)
