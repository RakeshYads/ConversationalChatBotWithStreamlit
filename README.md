## 🤖 Simple Rasa Chatbot integrated with Streamlit and deployed using Railway

### Overview
This project demonstrates how to build a simple chatbot using Rasa, integrate it with Streamlit for a user-friendly interface, and deploy it using Docker.
### Project Structure
```bash
.
├── actions # Rasa custom actions (Python code)
│ └── ...
├── data # Training data for Rasa (NLU and stories)
│ └── ...
├── models # Trained Rasa models
│ └── ...
├── streamlit_app # Streamlit application files
|
| └── main.py # Main script to run Streamlit app
├── .gitignore # Git ignore file
├── Dockerfile # Dockerfile for Rasa action server
├── README.md # README file (you're reading this)
├── requirements.txt # Python dependencies

```

### Prerequisites
- Python 3.7+
- Docker (for running Rasa action server locally)

### Setup Instructions
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. **Install dependencies:**

    ```bash

     pip install -r requirements.txt
     ```
3. **Train Rasa model:**

   ```bash

    rasa train
    ```
4. **Run Rasa action server:**

   ```bash

   docker build -t rasa-action-server .
   docker run -p 5055:5055 rasa-action-server
   ```
5. **Run Streamlit app locally:**

   ```bash

    streamlit run streamlit_app/main.py
    ```
### Deployment with Railway:**
    
1. **Sign in to Railway using CLI:**

    ```bash

     railway login
     ```

2. **Initialize Railway project:**

   ```bash

    railway init
    ```

3. **Configure Railway deployment:**
   Modify railway.yml to include deployment configurations for Rasa and Streamlit services.

4. **Deploy to Railway:**

    ```bash

    railway up
    ```
    
5.  **Access the deployed application:**
    Once deployed, Railway will provide a URL to access deployed Rasa chatbot integrated with Streamlit.
### Usage

   - Open the Streamlit app URL provided by Railway.
   - Interact with the chatbot interface. Start by typing a message to initiate the conversation.

### Customization

   - Rasa: Customize intents, entities, and responses in the data folder.
   - Streamlit: Modify the UI components, styling, and logic in the streamlit_app folder.

### Acknowledgements

  - This project uses Rasa for chatbot development.
  - Streamlit is used for creating the user interface.
  - Railway is used for deployment.

### Contact

For questions or support, please contact [Rakesh Yadav](https://www.linkedin.com/in/rakesh-yadav-556724118/).
