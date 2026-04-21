# OpenJarvis - Getting Started Guide

## ✅ Project Status: RUNNING

Your OpenJarvis installation is working! Here's everything you need to know.

## What is OpenJarvis?

OpenJarvis is a **local-first personal AI assistant framework** from Stanford that runs AI models on your device instead of the cloud. It's designed for:

- **Privacy**: Your data stays on your machine
- **Efficiency**: Optimized for local hardware (CPU, GPU, Apple Silicon)
- **Flexibility**: Works with multiple AI backends (Ollama, vLLM, cloud APIs)
- **Extensibility**: Built-in agents for various tasks

## Your Current Setup

- **Python Version**: 3.14.0
- **Config Location**: `C:\Users\john\.openjarvis\config.toml`
- **Default Engine**: llamacpp
- **Available Models**: qwen2.5-coder:latest, qwen2.5:latest (via Ollama)
- **Default Agent**: simple

## Quick Commands

### Basic Usage

```bash
# Ask a single question
python -m openjarvis.cli ask "What is the weather like?"

# Start interactive chat
python -m openjarvis.cli chat

# Check system status
python -m openjarvis.cli doctor

# View configuration
python -m openjarvis.cli config show
```

### Agent Management

```bash
# List available agents
python -m openjarvis.cli registry list

# Create a persistent agent
python -m openjarvis.cli agents create my-assistant

# Chat with an agent
python -m openjarvis.cli agents chat my-assistant
```

### Skills Management

```bash
# Install skills from Hermes
python -m openjarvis.cli skill install hermes:arxiv

# Sync all research skills
python -m openjarvis.cli skill sync hermes --category research

# List installed skills
python -m openjarvis.cli skill list
```

### Memory & Research

```bash
# Index documents for research
python -m openjarvis.cli memory index ./docs/

# Deep research mode
python -m openjarvis.cli research "Summarize recent AI papers"
```

## Built-in Agents

OpenJarvis comes with 12 pre-built agents:

1. **simple** - Single-turn chat, no tools
2. **orchestrator** - Multi-turn reasoning with tool selection
3. **native_react** - ReAct loop (Thought-Action-Observation)
4. **morning_digest** - Daily briefing from email, calendar, news
5. **deep_research** - Multi-hop research with citations
6. **monitor_operative** - Long-horizon monitoring with memory
7. **operative** - Persistent autonomous agent
8. **native_openhands** - Code generation and execution

## Available Tools (37 total)

- Web search and browsing
- File operations
- Code execution
- Email and calendar
- Memory and retrieval
- And more...

## Configuration Presets

Install pre-configured setups:

```bash
# Morning digest for Mac
python -m openjarvis.cli init --preset morning-digest-mac

# Deep research assistant
python -m openjarvis.cli init --preset deep-research

# Code assistant
python -m openjarvis.cli init --preset code-assistant

# Simple chat
python -m openjarvis.cli init --preset chat-simple
```

## Python SDK Usage

```python
from openjarvis import Jarvis

# Initialize
jarvis = Jarvis()

# Ask a question
response = jarvis.ask("What is machine learning?")
print(response)

# Multi-turn chat
jarvis.chat("Let's discuss AI")
```

## Starting the API Server

```bash
# Start OpenAI-compatible API server
python -m openjarvis.cli serve

# Server runs on http://localhost:8000
# Compatible with OpenAI SDK
```

## Connecting Data Sources

```bash
# Connect Gmail, Calendar, Tasks (one OAuth flow)
python -m openjarvis.cli connect gdrive

# Connect other services
python -m openjarvis.cli connect obsidian
python -m openjarvis.cli connect notion
```

## Next Steps

1. **Try the demo script**: `python demo_openjarvis.py`
2. **Explore examples**: Check the `examples/` folder for use cases
3. **Read the docs**: https://open-jarvis.github.io/OpenJarvis/
4. **Join Discord**: https://discord.gg/YZZRxCAhmm

## Troubleshooting

### Engines showing as "Unreachable"

This is normal if you haven't started the inference backend. To use Ollama:

```bash
# Start Ollama (if not running)
ollama serve

# Pull a model
ollama pull qwen2.5:latest

# Test it
python -m openjarvis.cli ask "Hello!"
```

### Need a different engine?

Edit `C:\Users\john\.openjarvis\config.toml` and change the `engine` setting.

## Architecture Overview

```
┌─────────────────────────────────────────┐
│           User Interface                │
│  (CLI, API, Channels, Desktop App)      │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│         OpenJarvis Core                 │
│  • Agents (reasoning loops)             │
│  • Tools (actions)                      │
│  • Memory (retrieval)                   │
│  • Skills (reusable patterns)           │
└─────────────────┬───────────────────────┘
                  │
┌─────────────────▼───────────────────────┐
│      Intelligence Layer                 │
│  • Engine (Ollama, vLLM, Cloud)         │
│  • Model Router (auto-select)           │
│  • Learning (distillation)              │
└─────────────────────────────────────────┘
```

## Key Features

- **Local-First**: Runs on your device, cloud optional
- **Multi-Backend**: Ollama, vLLM, SGLang, llama.cpp, cloud APIs
- **Agent Framework**: Pre-built agents + custom agent builder
- **Skills System**: Reusable tool patterns that improve over time
- **Memory**: Vector search, ColBERT, BM25 for retrieval
- **Channels**: Connect to Slack, Discord, Telegram, WhatsApp, etc.
- **Scheduler**: Run agents on a schedule
- **Learning**: Improve models from your usage data
- **Benchmarks**: Evaluate accuracy, latency, energy, cost

## Resources

- **Documentation**: https://open-jarvis.github.io/OpenJarvis/
- **GitHub**: https://github.com/open-jarvis/OpenJarvis
- **Project Site**: https://scalingintelligence.stanford.edu/blogs/openjarvis/
- **Leaderboard**: https://open-jarvis.github.io/OpenJarvis/leaderboard/
- **Discord**: https://discord.gg/YZZRxCAhmm

---

**Happy building with OpenJarvis! 🚀**
