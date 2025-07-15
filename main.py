from dotenv import load_dotenv
import os
import urllib.parse

from livekit import agents
from livekit.agents import AgentSession, Agent, RoomInputOptions, cli, mcp
from livekit.plugins import (
    openai,
    noise_cancellation,
)

load_dotenv(override=True)


class Assistant(Agent):
    def __init__(self) -> None:
        super().__init__(instructions="""You are the central interface agent that connects users with specialized agents to fulfill their queries.
YOU MUST SPEAK IN ENGLISH.
Your workflow:
1. List available agents using `list_agents` to understand capabilities
2. Analyze user queries and select the most appropriate agent
3. For Coral Server information requests, handle directly using available tools
4. For other requests: create a thread with `create_thread`, send clear instructions via `send_message`, and wait for responses with `wait_for_mentions` after using send message you must keep using the wait for mentions tool until you get the response from the agent.
5. Present agent responses back to the user in a helpful format
6. Continue assisting with follow-up queries

Always act as the central coordinator - you receive user requests, delegate to specialist agents when needed, and deliver comprehensive responses back to users.""")


async def entrypoint(ctx: agents.JobContext):
    # MCP Server configuration
    base_url = os.getenv("CORAL_SSE_URL")
    params = {
        #"waitForAgents": 1,
        "agentId": os.getenv("CORAL_AGENT_ID"),
        "agentDescription": "You are a helpful voice AI assistant."
    }
    query_string = urllib.parse.urlencode(params)
    MCP_SERVER_URL = f"{base_url}?{query_string}"

    session = AgentSession(
        llm=openai.realtime.RealtimeModel(
            voice="coral"
        ),
        mcp_servers=[
            mcp.MCPServerHTTP(
                url=MCP_SERVER_URL,
                timeout=600,
                client_session_timeout_seconds=600,
            ),
        ]
    )

    await session.start(
        room=ctx.room,
        agent=Assistant(),
        room_input_options=RoomInputOptions(
            # LiveKit Cloud enhanced noise cancellation
            # - If self-hosting, omit this parameter
            # - For telephony applications, use `BVCTelephony` for best results
            noise_cancellation=noise_cancellation.BVC(),
        ),
    )

    await ctx.connect()

    await session.generate_reply(
        instructions="Start by listing all connected agents and then greet the user with 'How can I assist you today?'"
    )


if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
