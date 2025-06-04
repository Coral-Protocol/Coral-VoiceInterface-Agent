# LiveKit Voice Interface Agent

A real-time voice interface agent built with LiveKit for interactive communication experiences with other agents. This agent acts as a central coordinator that connects users with specialized agents to fulfill their queries.

## Installation

### Prerequisites
- Python 3.13+
- [uv](https://docs.astral.sh/uv/) package manager

### Install uv
```bash
pip install uv
```

### Setup Project
1. Clone the repository
2. Install dependencies using uv:
```bash
uv sync
```

This will create a virtual environment and install all required dependencies including:
- `livekit-agents[mcp,openai]~=1.0`
- `livekit-plugins-noise-cancellation~=0.2`
- `python-dotenv>=1.1.0`

## Running the Application

### Start the Agent
```bash
uv run python main.py
```

### Development Mode
For development with auto-reload:
```bash
uv run python main.py dev
```

## Functionality

### Core Features
- **Voice Interface**: Real-time voice communication using LiveKit's Coral voice
- **Agent Coordination**: Acts as a central interface that connects users with specialized agents
- **MCP Integration**: Connects to Coral Protocol to act like a Central Agent
- **Noise Cancellation**: Built-in noise cancellation for clear voice communication

## Environment Variables

Change `.env.example` to `.env` file for environment variables