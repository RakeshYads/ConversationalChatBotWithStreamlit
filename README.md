## 🤖 Simple Rasa Chatbot integrated with Streamlit and deployed using Railway

### Overview
This project demonstrates how to build a simple chatbot using Rasa, integrate it with Streamlit for a user-friendly interface, and deploy it using Railway, a platform for deploying applications.

### Project Structure

.
├── actions # Rasa custom actions (Python code)
│ └── ...
├── data # Training data for Rasa (NLU and stories)
│ └── ...
├── models # Trained Rasa models
│ └── ...
├── streamlit_app # Streamlit application files
│ ├── assets # CSS, images, etc.
│ ├── components # Reusable Streamlit components
│ ├── pages # Different pages/screens of the Streamlit app
│ ├── config.py # Configuration for Streamlit app
│ └── main.py # Main script to run Streamlit app
├── tests # Unit tests, if any
│ └── ...
├── .gitignore # Git ignore file
├── Dockerfile # Dockerfile for Rasa action server
├── README.md # README file (you're reading this)
├── requirements.txt # Python dependencies
└── railway.yml # Railway configuration file

markdown


### Prerequisites
- Python 3.7+
- Railway account (for deployment)
- Docker (for running Rasa action server locally)

### Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>

    Install dependencies:

    bash

pip install -r requirements.txt

Train Rasa model:

bash

rasa train

Run Rasa action server:

bash

docker build -t rasa-action-server .
docker run -p 5055:5055 rasa-action-server

Run Streamlit app locally:

bash

    streamlit run streamlit_app/main.py

Deployment with Railway

    Sign in to Railway using CLI:

    bash

railway login

Initialize Railway project:

bash

railway init

Configure Railway deployment:
Modify railway.yml to include deployment configurations for your Rasa and Streamlit services.

Deploy to Railway:

bash

    railway up

    Access your deployed application:
    Once deployed, Railway will provide you with a URL to access your deployed Rasa chatbot integrated with Streamlit.

Usage

    Open the Streamlit app URL provided by Railway.
    Interact with the chatbot interface. Start by typing a message to initiate the conversation.

Customization

    Rasa: Customize intents, entities, and responses in the data folder.
    Streamlit: Modify the UI components, styling, and logic in the streamlit_app folder.

Contributing

Contributions are welcome! If you have suggestions or improvements, please create a pull request or open an issue.
License

This project is licensed under the MIT License.
Acknowledgements

    This project uses Rasa for chatbot development.
    Streamlit is used for creating the user interface.
    Railway is used for deployment.

Contact

For questions or support, please contact Rakesh Yadav.



