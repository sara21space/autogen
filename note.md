- Install the VS Code Python extension:
  ```sh
  code --install-extension ms-python.python
  ```
- Create a virtual environment: 
    ```sh 
    python -m venv .venv 
    ```
- Activate the virtual environment:
    ```sh
    .venv\Scripts\activate
    ```
- Install required packages:
    ```sh
    pip install -r requirements.txt
    ```
- Set environment variables:
    ```sh
    AZURE_OPENAI_API_KEY=your_azure_openai_api_key
    AZURE_OPENAI_ENDPOINT=https://your_azure_openai_endpoint
    OPENAI_API_VERSION=2025-01-01-preview
    OLLAMA_BASE_URL=http://localhost:11434/v1
    LMSTUDIO_BASE_URL=http://192.168.1.48:1234/v1
    OPENAI_API_KEY=your_openai_api_key
    ```
- Run the application:
  ```python 
  python chat.py
  ```