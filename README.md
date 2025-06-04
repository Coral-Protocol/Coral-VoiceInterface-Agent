# LiveKit Voice Interface Agent

**Responsibility:**  
A real-time voice interface agent that coordinates communication between users and specialized agents. Built on LiveKit with Coral Protocol integration, it enables seamless voice interaction and agent communication. 

## Details

- **Framework:** LiveKit Agents  
- **Tools Used:** LiveKit, OpenAI LLM
- **AI Model:** GPT-4  
- **Date Added:** June 2025  
- **License:** MIT  


## Install Dependencies

```bash
pip install uv
uv sync
````

## Configure Environment Variables

Copy the example file and update it with your credentials:

```bash
cp env.example .env
```

Required environment variables:

* `LIVEKIT_URL`
* `LIVEKIT_API_KEY`
* `LIVEKIT_API_SECRET`
* `OPENAI_API_KEY`


## Run Agent

Run in terminal (console) mode:

```bash
uv run python main.py console
```

## Agent Capabilities

* **Voice Interface** – Real-time voice communication via voice
* **Agent Routing** – Acts as a central coordinator to connect users with task-specific agents
* **MCP Integration** – Bridges communication using Coral Protocol

## Example Usage

1. Launch the voice interface agent.
2. Speak your query naturally.
3. The system:

   * Captures your voice input
   * Routes the query to the appropriate agent
   * Responds using a clean, real-time voice channel

## Creator Details

* **Name:** Ahsen Tahir
* **Contact:** [ahsen.t@coralprotocol.org](mailto:ahsen.t@coralprotocol.org)

