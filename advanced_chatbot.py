"""
Advanced AI/ML Expert Chatbot - FIXED VERSION
CodeAlpha AI Internship - Task 2
"""

import re
from difflib import SequenceMatcher
import random

class AdvancedAIMLChatbot:
    def __init__(self):
        self.knowledge_base = {
            "artificial intelligence": {
                "keywords": ["artificial intelligence", "what is ai", "define ai", "explain ai", "about ai"],
                "response": """Artificial Intelligence (AI) is a fascinating field! Think of it as teaching computers to think and learn like humans do. 

At its core, AI involves creating systems that can:
• Perceive their environment (like computer vision)
• Reason about information (like decision-making algorithms)
• Learn from experience (like machine learning)
• Understand language (like me!)

There are different types of AI:
1. Narrow AI (Weak AI) - Specialized in one task (like spam filters or Netflix recommendations)
2. General AI (Strong AI) - Can understand and learn any intellectual task a human can (still theoretical)
3. Super AI - Would surpass human intelligence (currently science fiction)

Today's AI powers things you use every day - voice assistants, recommendation systems, self-driving cars, and chatbots!

What aspect of AI interests you most? I can dive deeper into any area!"""
            },
            
            "machine learning": {
                "keywords": ["machine learning", "what is ml", "how does ml work", "explain machine learning", "about ml"],
                "response": """Machine Learning is the engine that powers modern AI! Let me break it down for you.

The Core Concept:
Instead of programming explicit rules, we train computers to learn patterns from data. Think of it like teaching a child - you show examples, and they learn to generalize!

The Three Main Types:

1. Supervised Learning (Learning with a teacher)
   - You provide labeled data (inputs + correct answers)
   - Algorithm learns to map inputs to outputs
   - Examples: Email spam detection, house price prediction
   - Common algorithms: Linear Regression, Decision Trees, Neural Networks

2. Unsupervised Learning (Finding patterns independently)
   - No labels provided - algorithm finds hidden patterns
   - Examples: Customer segmentation, anomaly detection
   - Common algorithms: K-means clustering, PCA, Autoencoders

3. Reinforcement Learning (Learning by trial and error)
   - Agent learns by interacting with environment
   - Gets rewards for good actions, penalties for bad ones
   - Examples: Game-playing AI, robotics, recommendation systems
   - Famous example: AlphaGo beating world champions

The Process:
1. Collect data
2. Prepare and clean it
3. Choose an algorithm
4. Train the model
5. Evaluate performance
6. Deploy and monitor

The magic happens in the training phase - the algorithm adjusts its internal parameters to minimize errors!

Want to explore any specific type of ML or algorithm?"""
            },
            
            "deep learning": {
                "keywords": ["deep learning", "neural network", "what is deep learning", "explain deep learning", "about deep learning", "dl"],
                "response": """Deep Learning is like giving computers a brain! It's inspired by how our own brains work.

What Makes It 'Deep'?
The 'deep' comes from using neural networks with many layers (sometimes hundreds!). Each layer learns increasingly complex features:
- Layer 1: Edges and basic shapes
- Layer 2: Textures and patterns
- Layer 3: Parts of objects
- Final layers: Complete objects and concepts

Key Architectures:

1. Convolutional Neural Networks (CNNs)
   - Specialized for images and spatial data
   - Used in: Face recognition, medical imaging, self-driving cars
   - Why they work: They understand spatial relationships

2. Recurrent Neural Networks (RNNs)
   - Handle sequential data with memory
   - Used in: Language translation, speech recognition, time series
   - Improved versions: LSTM, GRU (solve the vanishing gradient problem)

3. Transformers (The revolution!)
   - Attention mechanism - focuses on relevant parts of input
   - Used in: ChatGPT, Claude, image generation
   - Why revolutionary: Parallel processing, better long-range dependencies

Why Deep Learning Exploded:
- More data available
- Powerful GPUs for training
- Better algorithms and architectures
- Open-source frameworks (TensorFlow, PyTorch)

Real-World Impact:
- Healthcare: Disease detection from medical scans
- Autonomous vehicles: Understanding road scenes
- Language: Translation, chatbots, content generation
- Creativity: AI art, music composition, video generation

The amazing thing? Deep learning models discover features automatically - no manual feature engineering needed!

Curious about a specific architecture or application?"""
            },
            
            "nlp": {
                "keywords": ["nlp", "natural language processing", "language processing", "what is nlp", "explain nlp"],
                "response": """Natural Language Processing (NLP) is how I'm able to understand and respond to you! It's the bridge between human language and computer understanding.

The Challenge:
Human language is messy, ambiguous, and context-dependent. "I saw her duck" - did someone see a bird, or someone ducking down? NLP handles this complexity!

Core NLP Tasks:

1. Text Understanding:
   - Tokenization: Breaking text into words/subwords
   - Part-of-speech tagging: Identifying nouns, verbs, etc.
   - Named Entity Recognition: Finding names, places, organizations
   - Sentiment Analysis: Detecting emotions and opinions

2. Text Generation:
   - Machine Translation: Converting between languages
   - Summarization: Creating concise versions of long texts
   - Question Answering: Finding answers in text
   - Dialogue Systems: Chatbots and virtual assistants

3. Advanced Tasks:
   - Text Classification: Categorizing documents
   - Information Extraction: Pulling structured data from text
   - Relation Extraction: Finding relationships between entities

Evolution of NLP:

Traditional Era (Rule-based):
- Hand-crafted rules and patterns
- Dictionary lookups
- Limited and brittle

Statistical Era (2000s):
- Machine learning on text features
- Word2Vec, GloVe embeddings
- Better, but still limited context

Deep Learning Era (2010s-now):
- RNNs, LSTMs for sequences
- Transformers (BERT, GPT, T5)
- Pre-training + fine-tuning paradigm
- Context-aware understanding!

Modern Techniques:
- Word Embeddings: Words as vectors capturing meaning
- Attention Mechanisms: Focusing on relevant words
- Transfer Learning: Pre-train on huge data, fine-tune for tasks
- Few-shot Learning: Learn from just a few examples

Real Applications:
- Voice assistants (Siri, Alexa)
- Email auto-complete
- Language translation apps
- Content moderation
- Medical record analysis
- Legal document review

I'm actually a large language model powered by advanced NLP!

Want to know more about any specific NLP technique?"""
            },
            
            "computer vision": {
                "keywords": ["computer vision", "cv", "image recognition", "image processing", "visual recognition"],
                "response": """Computer Vision is teaching computers to 'see' and understand the visual world!

What is Computer Vision?
It's enabling computers to derive meaningful information from digital images and videos. Think of it as giving machines eyes and the brain to interpret what they see.

Core Tasks:

1. Image Classification
   - What's in this image? (Cat, dog, car?)
   - Single label for entire image
   - Networks: ResNet, EfficientNet, Vision Transformers

2. Object Detection
   - Where are objects? What are they?
   - Multiple objects with bounding boxes
   - Networks: YOLO, Faster R-CNN, RetinaNet

3. Semantic Segmentation
   - Label every pixel in the image
   - Pixel-level understanding
   - Networks: U-Net, DeepLab, Mask R-CNN

4. Image Generation
   - Creating new images from scratch
   - Networks: GANs, Diffusion Models, VAEs
   - Applications: Art, face generation, image editing

How It Works:

Traditional Approach:
- Hand-crafted features (edges, corners, textures)
- Classical algorithms (SIFT, HOG)
- Limited accuracy

Deep Learning Approach:
- CNNs automatically learn features
- Hierarchical feature learning
- State-of-the-art accuracy!

Breakthrough Moments:
- 2012: AlexNet wins ImageNet (deep learning revolution)
- 2014: VGGNet, GoogLeNet (deeper networks work!)
- 2015: ResNet (skip connections solve vanishing gradients)
- 2017: Attention mechanisms enter computer vision
- 2020+: Vision Transformers challenge CNN dominance

Amazing Applications:

Healthcare:
- Detecting tumors in X-rays/MRIs
- Diabetic retinopathy detection
- COVID-19 diagnosis from chest scans

Autonomous Vehicles:
- Lane detection
- Pedestrian recognition
- Traffic sign understanding
- 3D scene reconstruction

Retail:
- Visual search (find similar products)
- Inventory management
- Checkout-free stores (Amazon Go)

Security:
- Face recognition
- Anomaly detection in surveillance
- Biometric authentication

What aspect of computer vision would you like to explore further?"""
            },
            
            "python": {
                "keywords": ["python", "python programming", "why python", "python for ai", "python ml"],
                "response": """Python is THE language for AI and Machine Learning! Let me tell you why it's so popular.

Why Python Dominates AI/ML:

1. Simple, Readable Syntax
   - Looks almost like English
   - Focus on problem-solving, not syntax
   - Perfect for rapid prototyping

2. Rich Ecosystem
   - Hundreds of specialized libraries
   - Active community support
   - Regular updates and improvements

3. Versatility
   - Data analysis, web development, automation
   - Scripting to production deployment
   - Cross-platform compatibility

Essential Python Libraries for AI/ML:

Data Manipulation:
- NumPy: Fast numerical computing, arrays
- Pandas: DataFrames for structured data
- SciPy: Scientific computing algorithms

Machine Learning:
- scikit-learn: Classic ML algorithms
- XGBoost: Gradient boosting (Kaggle winner!)
- LightGBM: Fast gradient boosting

Deep Learning:
- TensorFlow: Google's powerhouse
- PyTorch: Research favorite (by Meta)
- JAX: High-performance with auto-differentiation

Computer Vision:
- OpenCV: Image/video processing
- Pillow: Basic image operations
- torchvision: Pre-trained models

NLP:
- NLTK: Traditional NLP toolkit
- spaCy: Industrial-strength NLP
- Transformers (HuggingFace): Pre-trained models

Visualization:
- Matplotlib: Basic plotting
- Seaborn: Statistical visualizations
- Plotly: Interactive plots

Deployment:
- Flask/FastAPI: Create ML APIs
- Streamlit: Quick data apps
- MLflow: Experiment tracking

Learning Path:
1. Basics: Variables, loops, functions, OOP
2. Data Science: NumPy, Pandas, Matplotlib
3. ML Fundamentals: scikit-learn
4. Deep Learning: TensorFlow or PyTorch
5. Specialized: NLP, CV, or RL libraries

Python makes AI accessible - you can go from idea to working model in minutes!

Want specific examples or help with any library?"""
            },
            
            "learn ai": {
                "keywords": ["how to learn ai", "learn ai", "start learning ai", "ai learning path", "study ai"],
                "response": """Great question! Learning AI is an exciting journey. Here's your comprehensive roadmap:

PHASE 1: Foundations (2-3 months)

Mathematics (Essential!):
- Linear Algebra: Vectors, matrices, eigenvalues
- Calculus: Derivatives, gradients, chain rule
- Probability & Statistics: Distributions, Bayes theorem

Programming:
- Master Python basics
- Learn NumPy, Pandas, Matplotlib
- Practice on LeetCode/HackerRank

PHASE 2: Machine Learning (3-4 months)

Core Concepts:
- Supervised vs Unsupervised learning
- Bias-variance tradeoff
- Overfitting and regularization
- Cross-validation

Key Algorithms:
1. Linear/Logistic Regression
2. Decision Trees & Random Forests
3. Support Vector Machines
4. K-Means Clustering
5. Naive Bayes
6. Gradient Boosting

Courses (Pick one):
- Andrew Ng's ML Course (Coursera) - The classic!
- Fast.ai's Practical ML - Hands-on approach
- Google's ML Crash Course - Quick and free

PHASE 3: Deep Learning (4-6 months)

Neural Network Basics:
- Perceptrons and activation functions
- Forward and backpropagation
- Gradient descent and optimization

Advanced Architectures:
- CNNs for computer vision
- RNNs/LSTMs for sequences
- Transformers for NLP
- GANs for generation

Frameworks:
- Start with TensorFlow/Keras OR PyTorch
- Build projects in both eventually

PHASE 4: Specialization (3-6 months)

Pick ONE area:
- Computer Vision: Object detection, image segmentation
- NLP: Transformers, BERT, GPT models
- Reinforcement Learning: Q-Learning, DQN

PHASE 5: Projects (Ongoing)

Beginner:
- Iris flower classification
- House price prediction
- MNIST digit recognition

Intermediate:
- Image classification
- Object detection system
- Chatbot with NLP

Advanced:
- Build a GAN
- Create a self-driving car simulation
- Fine-tune GPT for specific domain

Pro Tips:

1. Learn by Doing - Don't just watch
2. Master the Basics - Don't rush
3. Read Papers - Implement papers in code
4. Join Competitions - Kaggle competitions
5. Stay Consistent - Code every day

Realistic Timeline:
- 6 months: Basic ML, simple projects
- 12 months: Deep learning, good projects
- 18-24 months: Job-ready with portfolio

Remember: AI is a marathon, not a sprint. Focus on understanding concepts deeply!

What aspect would you like to start with?"""
            },
            
            "ai career": {
                "keywords": ["ai career", "ai job", "ml engineer", "data scientist", "career in ai", "jobs in ai"],
                "response": """Let's talk about AI careers - it's one of the hottest fields right now!

Main AI Career Paths:

1. Machine Learning Engineer
   - Design and implement ML systems
   - Deploy models to production
   - Build ML pipelines
   - Salary: $120k - $200k+ (US)

2. Data Scientist
   - Analyze complex datasets
   - Build predictive models
   - Extract business insights
   - Salary: $100k - $180k+ (US)

3. AI Research Scientist
   - Develop new AI algorithms
   - Publish research papers
   - Push boundaries of AI
   - Salary: $150k - $300k+ (US)

4. Computer Vision Engineer
   - Build systems that understand images/video
   - Face recognition, object detection
   - Medical imaging, autonomous vehicles
   - Salary: $130k - $220k+ (US)

5. NLP Engineer
   - Build language understanding systems
   - Chatbots, translation, sentiment analysis
   - Voice assistants
   - Salary: $125k - $210k+ (US)

6. MLOps Engineer
   - Deploy and maintain ML systems
   - Build ML pipelines
   - Monitor model performance
   - Salary: $110k - $190k+ (US)

Industry Demand:

Hottest Industries:
- Tech companies (Google, Meta, Microsoft, Amazon)
- Healthcare and biotech
- Finance and fintech
- Autonomous vehicles
- E-commerce

Education Paths:

Traditional Route:
- BS in CS, Math, or Engineering
- MS in AI/ML (increasingly common)
- PhD for research positions

Alternative Route:
- Self-taught + portfolio
- Bootcamps (3-6 months)
- Online degrees

Getting Your First AI Job:

1. Build Strong Portfolio (Critical!)
   - 3-5 substantial projects
   - GitHub with clean code
   - Deployed models

2. Contribute to Open Source
   - scikit-learn, TensorFlow, PyTorch
   - Fix bugs, add features

3. Compete on Kaggle
   - Gain practical experience
   - Learn from top solutions

4. Network
   - LinkedIn connections
   - AI conferences and meetups
   - Online communities

5. Apply Strategically
   - Start with junior positions
   - Apply to startups (easier entry)
   - Consider internships first

My Advice:

1. Start Now - Don't wait for perfect timing
2. Focus on Fundamentals - Math and programming
3. Build Projects - Portfolio > Certificates
4. Stay Current - AI evolves rapidly
5. Network Actively - Connections matter
6. Keep Learning - It never stops!

Common Mistakes to Avoid:
- Only doing tutorials, no projects
- Jumping to deep learning too fast
- Ignoring math foundations
- Not learning software engineering

Remember: The AI field is accessible! With dedication, you can build a successful career regardless of your background.

Want specific advice for your situation?"""
            },
            
            "codealpha": {
                "keywords": ["codealpha", "code alpha", "internship", "certificate", "tasks", "about codealpha"],
                "response": """Let me tell you about the CodeAlpha AI Internship!

About CodeAlpha:
CodeAlpha is a leading software development company focused on driving innovation across emerging technologies. They offer practical, hands-on internship programs designed to give students real-world experience.

AI Internship Overview:

What You'll Work On:
- AI model development
- Machine learning workflows
- Real-time data processing
- Industry-standard projects

Internship Requirements:

You need to complete 2 or 3 out of 4 tasks:
1. Language Translation Tool - API integration
2. FAQ Chatbot - NLP and text matching
3. Music Generation with AI - Deep learning, RNNs/GANs
4. Object Detection & Tracking - Computer vision, YOLO

Important: Completing only 1 task = No certificate!

What You Get:

Certificates & Documents:
- Internship Offer Letter
- QR-Verified Completion Certificate
- Unique ID Certificate
- Letter of Recommendation (performance-based)

Career Support:
- Job opportunities
- Placement support
- Resume building assistance

Submission Requirements:

For Each Task:
1. GitHub Repository - Name: CodeAlpha_ProjectName
2. LinkedIn Post - Tag @CodeAlpha, video demo, GitHub link
3. Submission Form - Submit via WhatsApp group

Success Tips:

For Your Projects:
- Write clean, commented code
- Create professional README
- Add screenshots/demos
- Explain your approach

For LinkedIn Posts:
- Show working demo
- Explain the technology
- Share what you learned
- Be enthusiastic but professional

For Video Demo:
- 60-90 seconds ideal
- Show the working project
- Explain key features
- Professional presentation

Contact CodeAlpha:
- Website: www.codealpha.tech
- WhatsApp: +91 8052293611
- Email: services@codealpha.tech

My Recommendation:
Treat this seriously! These projects will be in your portfolio for years. Make them impressive!

What task are you working on? I can help you make it exceptional!"""
            }
        }
        
        self.conversation_history = []
        self.simple_greetings = ["hi", "hello", "hey"]
        self.farewells = ["bye", "goodbye", "see you"]
        
    def find_best_match(self, user_input):
        user_input_lower = user_input.lower().strip()
        best_match = None
        best_score = 0
        
        for topic, data in self.knowledge_base.items():
            for keyword in data["keywords"]:
                similarity = SequenceMatcher(None, user_input_lower, keyword).ratio()
                
                if keyword in user_input_lower:
                    similarity = max(similarity, 0.85)
                
                if similarity > best_score:
                    best_score = similarity
                    best_match = topic
        
        return best_match, best_score
    
    def get_response(self, user_input):
        user_input_lower = user_input.lower().strip()
        
        # Handle ONLY simple single-word greetings
        if user_input_lower in self.simple_greetings and len(user_input.split()) == 1:
            responses = [
                "Hello! 👋 I'm your AI/ML expert chatbot. I can answer questions about Artificial Intelligence, Machine Learning, Deep Learning, NLP, Computer Vision, Python programming, AI careers, and the CodeAlpha internship. What would you like to learn about?",
                "Hi there! 🤖 Great to meet you! Ask me anything about AI and ML!",
                "Hey! 😊 Welcome! I specialize in AI and ML topics. What interests you?"
            ]
            return random.choice(responses)
        
        # Handle farewells
        if any(farewell in user_input_lower for farewell in self.farewells):
            return "Goodbye! 👋 Keep learning and building amazing AI projects!"
        
        # Find best matching topic
        best_match, confidence = self.find_best_match(user_input)
        
        if confidence > 0.3 and best_match:
            response = self.knowledge_base[best_match]["response"]
            return response
        else:
            return """I'd love to help you with that! I specialize in AI and Machine Learning topics. Here are some areas I can discuss in depth:

• AI Fundamentals - What is AI, types of AI
• Machine Learning - Supervised, unsupervised, reinforcement learning
• Deep Learning - Neural networks, CNNs, RNNs, Transformers
• NLP - Natural language processing
• Computer Vision - Image recognition, object detection
• Python for AI - Libraries, frameworks
• Learning AI - Roadmap, resources
• AI Careers - Job roles, salaries
• CodeAlpha Internship - Tasks, requirements

Could you rephrase your question to focus on one of these areas?"""
    
    def chat(self):
        print("="  * 80)
        print("🤖 ADVANCED AI/ML EXPERT CHATBOT - CodeAlpha AI Internship")
        print("=" * 80)
        print("\nType 'quit', 'exit', or 'bye' to end.\n")
        print("=" * 80)
        
        while True:
            user_input = input("\n🧑 You: ").strip()
            
            if not user_input:
                continue
            
            if user_input.lower() in ['quit', 'exit']:
                print(f"\n🤖 Bot: {self.get_response('bye')}")
                break
            
            response = self.get_response(user_input)
            print(f"\n🤖 Bot:\n{response}")


if __name__ == "__main__":
    bot = AdvancedAIMLChatbot()
    bot.chat()
