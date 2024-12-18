# SafeScape-AI

SafeScape-AI is a Flask-based Python application that processes and analyzes Instagram webhook events such as comments, messages, reactions, and more. It uses SQLite to store event data and provides insights using a powerful analysis script.

---

## Features

- **Webhook Integration**: Captures real-time Instagram events.
- **Database Storage**: Stores all events in an SQLite database for persistence.
- **Event Handlers**: Processes multiple types of events (comments, messages, reactions, etc.).
- **Data Analysis**: Generates insights like top users, event counts, and more.
- **Lightweight Setup**: Easy to run locally or deploy on a cloud service.

---

## Prerequisites

Before setting up, ensure you have the following installed on your system:
- **Python**: Version 3.9 or later.
- **Pip**: Python's package installer.

---

## Setup Instructions

### Step 1: Clone the Repository

```bash
git clone <repository_url>
cd SafeScape-AI 
