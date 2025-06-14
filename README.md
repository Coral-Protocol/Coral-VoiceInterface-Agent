# Voice French Agent

The Voice French Agent is a real-time multilingual voice assistant that listens to English speech and translates it into French. It uses Deepgram for speech-to-text, OpenAI for translation, ElevenLabs for French voice synthesis, and LiveKit for real-time communication with built-in noise cancellation.

## Responsibility
A real-time multilingual voice assistant that listens to English speech, translates it to French, and responds in natural French voice using advanced AI and speech technologies.

## Details
- **Framework:** LiveKit Agents
- **Tools Used:** Deepgram STT, ElevenLabs TTS, OpenAI LLM, LiveKit Plugins
- **AI Model:** GPT-4
- **Date Added:** June 2025
- **License:** MIT
- **Original Source:** [Voice French Agent](https://github.com/livekit-examples/python-agents-examples/blob/main/translators/pipeline_translator.py)

## Use the Agent

### 1. Clone & Install Dependencies

Ensure that the [Coral Server](https://github.com/Coral-Protocol/coral-server) is running on your system. If you are trying to run Voice French Agent and require an input, you can either create your agent which communicates on the coral server or run and register the [Interface Agent](https://github.com/Coral-Protocol/Coral-Interface-Agent) on the Coral Server.

```bash
# In a new terminal clone the repository:
git clone https://github.com/Coral-Protocol/Voice-French-Agent.git

# Navigate to the project directory:
cd Voice-French-Agent

# Install `uv`:
pip install uv

# Install dependencies from `pyproject.toml` using `uv`:
uv sync
```

### 2. Configure Environment Variables
<details>

Copy the example file and add your API keys:

```bash
cp .env.example .env
```

Update `.env` with:
- `LIVEKIT_URL`  ([Get LiveKit Url](https://cloud.livekit.io/))
- `LIVEKIT_API_KEY` ([Get LiveKit API Key](https://cloud.livekit.io/))
- `LIVEKIT_API_SECRET` ([Get LiveKit API Secret](https://cloud.livekit.io/))
- `OPENAI_API_KEY` ([Get OpenAI API Key](https://platform.openai.com/api-keys))
- `DEEPGRAM_API_KEY` ([Get Deepgram API Key](https://deepgram.com/))
- `ELEVENLABS_API_KEY` ([Get ElevenLabs API Key](https://elevenlabs.io/app/settings/api-keys))

</details>

### 3. Run Agent
<details>

Start the agent with voice input/output:

```bash
uv run python main.py console
```

</details>

## Agent System

- **English Speech Recognition:** via Deepgram
- **AI Translation to French:** powered by OpenAI
- **French Voice Output:** using ElevenLabs
- **Noise Cancellation:** with LiveKit plugins

## Usage Examples
<details>

1. Start the agent.
2. Speak in English.
3. The agent:
   - Transcribes your speech.
   - Translates to French.
   - Responds in natural French voice.

**For a Multi-Agent-System:**
```python
# Other agents can communicate with French agent like this:
# 1. Send message to french_agent via MCP
# 2. French agent will notify interface agent
# 3. Users can then speak directly with French agent
# 4. All responses are in French via speech
```

</details>

## Creator Details
- **Name:** Ahsen Tahir
- **Contact:** [ahsen.t@coralprotocol.org](mailto:ahsen.t@coralprotocol.org)

