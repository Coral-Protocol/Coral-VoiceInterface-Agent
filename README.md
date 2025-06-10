# LiveKit Voice Interface Agent (STT-LLM-TTS Pipeline)

**Responsibility:**  
A real-time voice interface agent that provides natural voice interaction using a complete STT-LLM-TTS pipeline. Built on LiveKit with Deepgram for speech-to-text, OpenAI for language processing, and Cartesia for text-to-speech synthesis.

## Details

- **Framework:** LiveKit Agents  
- **Tools Used:** LiveKit, Deepgram STT, OpenAI LLM, Cartesia TTS, Silero VAD
- **AI Model:** GPT-4o-mini with Nova-3 STT and Sonic-2 TTS
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

* `LIVEKIT_URL` - Your LiveKit server URL
* `LIVEKIT_API_KEY` - LiveKit API key  
* `LIVEKIT_API_SECRET` - LiveKit API secret
* `OPENAI_API_KEY` - OpenAI API key for GPT-4o-mini
* `DEEPGRAM_API_KEY` - Deepgram API key for Nova-3 STT
* `CARTESIA_API_KEY` - Cartesia API key for Sonic-2 TTS

##First download the Turn detector files
Run this command in terminal
```bash
 uv run python main.py download-files
```

## Run Agent

Run in terminal (console) mode:

```bash
uv run python main.py console
```

## Agent Capabilities

* **Speech-to-Text** – High-quality multilingual speech recognition using Deepgram Nova-3
* **Language Processing** – Intelligent conversation handling with GPT-4o-mini
* **Text-to-Speech** – Natural voice synthesis using Cartesia Sonic-2
* **Voice Activity Detection** – Smart turn detection with Silero VAD
* **Noise Cancellation** – Enhanced audio quality with LiveKit BVC

## Pipeline Components

1. **STT (Speech-to-Text):** Deepgram Nova-3 with multilingual support
2. **LLM (Language Model):** OpenAI GPT-4o-mini for intelligent responses  
3. **TTS (Text-to-Speech):** Cartesia Sonic-2 for natural voice synthesis
4. **VAD (Voice Activity Detection):** Silero for accurate speech detection
5. **Turn Detection:** Multilingual model for conversation flow

## Example Usage

1. Launch the voice interface agent.
2. Speak your query naturally.
3. The system:
   * Captures your voice input using Deepgram STT
   * Processes your request with OpenAI LLM
   * Responds using natural voice synthesis via Cartesia TTS

## Creator Details

* **Name:** Ahsen Tahir
* **Contact:** [ahsen.t@coralprotocol.org](mailto:ahsen.t@coralprotocol.org)

