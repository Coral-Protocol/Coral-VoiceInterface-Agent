## LiveKit Voice Interface Agent

The LiveKit Voice Interface Agent is a real-time voice interface agent that coordinates communication between users and specialized agents. Built on LiveKit with Coral Protocol integration, it enables seamless voice interaction and agent communication.

## Responsibility
The LiveKit Voice Interface Agent acts as a central coordinator, connecting users with task-specific agents via real-time voice communication. It captures user voice input, routes queries to the appropriate agent, and responds using a clean, real-time voice channel, leveraging LiveKit and Coral Protocol for seamless integration.

## Details
- **Framework**: LiveKit Agents
- **Tools used**: LiveKit, OpenAI LLM
- **AI model**: GPT-4
- **Date added**: June 2025
- **License**: MIT


## Use the Agent  

### 1. Clone & Install Dependencies
Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system
<details>


Ensure you have Python and [uv](https://github.com/astral-sh/uv) installed.

```bash
# In a new terminal clone the repository:
git clone https://github.com/Coral-Protocol/Voice-Interface-Agent.git

# Navigate to the project directory:
cd Voice-Interface-Agent
# Install `uv`:
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync
```

</details>

### 2. Configure Environment Variables

<details>

Copy the example file and update it with your credentials:

```bash
cp -r .env.example .env
```

Required environment variables:

* `LIVEKIT_URL`
* `LIVEKIT_API_KEY` ([Get LiveKit API Key](https://cloud.livekit.io/))
* `LIVEKIT_API_SECRET` ([Get LiveKit API Secret](https://cloud.livekit.io/))
* `OPENAI_API_KEY` ([Get OpenAI API Key](https://platform.openai.com/api-keys))

</details>

### 3. Run Agent

<details>

Run the agent in terminal (console) mode:

```bash
uv run python main.py console
```

</details>

### 4. Example

<details>

```bash
# Speak your query naturally after launching the agent.

# The system will:
# - Capture your voice input
# - Route the query to the appropriate agent
# - Respond using a clean, real-time voice channel
```

</details>

## Creator Details
- **Name**: Ahsen Tahir
- **Contact**: [Discord](https://discord.com/invite/Xjm892dtt3)

