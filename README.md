
# Fake Store API Documentation

The FakeStore API is a RESTful API for managing products, orders, carts, and more. This document provides instructions on how to clone and run the FakeStore API on your local machine.

## Prerequisites

Before you begin, make sure you have the following software installed on your computer:

- Python 3.x
- pip (Python package manager)
- Virtualenv (optional but recommended for creating a virtual environment)
  
## Run Locally

### Clone the project 

1. Open your terminal or command prompt.

2. Navigate to the directory where you want to clone the FakeStore API repository.

3. Run the following command to clone the repository:

```bash
    https://github.com/urs-santoshh/fake_store_api.git
```

### Setup Virtual Environment (Optional)

We recommend using a virtual environment to isolate the project's dependencies. If you choose not to use a virtual environment, you can skip this step.

1. Navigate to the project directory:

   ```bash
   cd fake_store_api
   ```

2. Create a virtual environment (Python 3.x) and activate it:

   ```bash
   python -m venv .venv
   source venv/bin/activate  # On Windows, use "./venv/scripts/activate"
   ```
   
### Install Dependencies

1. Install the project dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```
