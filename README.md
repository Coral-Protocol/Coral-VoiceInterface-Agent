# LiveKit Voice Interface Agent (STT-LLM-TTS Pipeline)

## [Voice Interface Agent](https://github.com/Coral-Protocol/Voice-Interface-Agent)

The Voice Interface Agent is an open-source AI assistant that provides real-time voice interaction using a complete STT-LLM-TTS pipeline, enabling natural conversations with AI systems.

## Responsibility
The Voice Interface Agent enables natural, real-time voice interaction using a full STT-LLM-TTS pipeline. It leverages LiveKit for streaming, Deepgram for speech-to-text, OpenAI for language processing, and Cartesia for text-to-speech synthesis.

## Details
- **Framework**: LiveKit Agents
- **Tools used**: LiveKit, Deepgram STT, OpenAI LLM, Cartesia TTS, Silero VAD
- **AI model**: GPT-4o-mini with Nova-3 STT and Sonic-2 TTS
- **Date added**: June 2025
- **License**: MIT

## Use the Agent

### 1. Clone & Install Dependencies

<details>

```bash
# In a new terminal clone the repository:
git clone https://github.com/Coral-Protocol/Voice-Interface-Agent.git

# Navigate to the project directory:
cd Voice-Interface-Agent

# Install uv:
pip install uv

# Install dependencies from pyproject.toml using uv:
uv sync

# Copy the client sse.py from utils to mcp package (Linux/ Mac)
cp -r utils/sse.py .venv/lib/python3.13/site-packages/mcp/client/sse.py

# OR Copy this for Windows
cp -r utils\sse.py .venv\Lib\site-packages\mcp\client\sse.py
```

</details>

### 2. Configure Environment Variables

<details>

Get the API Keys:
[LiveKit](https://cloud.livekit.io/) |
[OpenAI](https://platform.openai.com/api-keys) |
[Deepgram](https://deepgram.com/) |
[Cartesia](https://play.cartesia.ai/keys)

```bash
# Create .env file in project root
cp -r .env.example .env
```

Required environment variables:
* `LIVEKIT_URL` - Your LiveKit server URL
* `LIVEKIT_API_KEY` - LiveKit API key
* `LIVEKIT_API_SECRET` - LiveKit API secret
* `OPENAI_API_KEY` - OpenAI API key for GPT-4o-mini
* `DEEPGRAM_API_KEY` - Deepgram API key for Nova-3 STT
* `CARTESIA_API_KEY` - Cartesia API key for Sonic-2 TTS

</details>

### 3. Download Turn Detector Files

<details>

```bash
uv run python main.py download-files
```

</details>

### 4. Run Agent

<details>

```bash
# Run in terminal (console) mode:
uv run python main.py console
```

</details>

### 5. Example

<details>

```bash
# Input:
Speak your query naturally into the microphone.

# Output:
The system will:
- Capture your voice input using Deepgram STT
- Process your request with OpenAI LLM
- Respond using natural voice synthesis via Cartesia TTS
```

</details>

## Pipeline Components

1. **STT (Speech-to-Text):** Deepgram Nova-3 with multilingual support
2. **LLM (Language Model):** OpenAI GPT-4o-mini for intelligent responses  
3. **TTS (Text-to-Speech):** Cartesia Sonic-2 for natural voice synthesis
4. **VAD (Voice Activity Detection):** Silero for accurate speech detection
5. **Turn Detection:** Multilingual model for conversation flow

## Creator Details
- **Name**: Ahsen Tahir
- **Affiliation**: Coral Protocol
- **Contact**: [Discord](https://discord.com/invite/Xjm892dtt3)

