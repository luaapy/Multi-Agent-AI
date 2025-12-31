# 🤖 Multi-Agent AI Code Assistant

A powerful multi-agent AI system that leverages three different AI providers to collaboratively generate, review, and polish code. Each agent has a specialized role, creating a robust code generation pipeline with consensus-based quality assurance.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)
![AI Agents](https://img.shields.io/badge/AI%20Agents-3-purple)

## ✨ Features

- **🚀 Triple AI Architecture** - Combines Groq (Llama 3.3), Google Gemini, and GLM for comprehensive code generation
- **👥 Specialized Agent Roles**:
  - **SpeedCoder** (Groq) - Fast draft generation with creative solutions
  - **Reviewer** (Gemini) - Code quality analysis and optimization
  - **Polisher** (GLM) - Best practices and documentation expert
- **🗳️ Consensus System** - AIs vote on the best approach for higher quality output
- **⚡ Parallel Processing** - Simultaneous API calls for faster responses
- **💾 Conversation History** - Persistent conversation saving
- **🔧 Configurable** - Easy customization of models, temperatures, and features

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                        User Request                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                       Orchestrator                           │
│              (Coordinates all AI agents)                     │
└─────────────────────────────────────────────────────────────┘
                              │
           ┌──────────────────┼──────────────────┐
           ▼                  ▼                  ▼
   ┌───────────────┐  ┌───────────────┐  ┌───────────────┐
   │  SpeedCoder   │  │   Reviewer    │  │   Polisher    │
   │    (Groq)     │  │   (Gemini)    │  │    (GLM)      │
   │               │  │               │  │               │
   │ Fast Drafts   │  │ Quality Check │  │ Best Practice │
   └───────────────┘  └───────────────┘  └───────────────┘
           │                  │                  │
           └──────────────────┼──────────────────┘
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Code Synthesizer                          │
│            (Merges & produces final output)                  │
└─────────────────────────────────────────────────────────────┘
```

## 📦 Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/luaapy/Multi-Agent-AI.git
   cd Multi-Agent-AI
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys** (in `config.py`):
   ```python
   API_KEYS = {
       'glm': 'your-glm-api-key',
       'gemini': 'your-gemini-api-key',
       'groq': 'your-groq-api-key'
   }
   ```

## 🚀 Usage

Start the CLI interface:

```bash
python main.py
```

### Example Interaction

```
🤖 Multi-Agent AI Code Assistant
Enter your coding request:

> Write a function to calculate factorial

[SpeedCoder 🚀] Generating quick draft...
[Reviewer 📋] Analyzing code quality...
[Polisher ✨] Applying best practices...

Final Code:
───────────────────────────────────
# ... polished, production-ready code ...
───────────────────────────────────
```

## 📁 Project Structure

```
Multi-Agent AI/
├── main.py                 # Application entry point
├── config.py               # API configuration & settings
├── requirements.txt        # Python dependencies
├── core/
│   ├── agent_groq.py       # Groq/Llama agent (SpeedCoder)
│   ├── agent_gemini.py     # Gemini agent (Reviewer)
│   ├── agent_glm.py        # GLM agent (Polisher)
│   ├── orchestrator.py     # Agent coordination
│   ├── code_synthesizer.py # Output merging
│   └── conversation_manager.py
├── prompts/                # Agent-specific prompts
├── ui/                     # User interface (CLI)
└── utils/                  # Helper utilities
```

## ⚙️ Configuration

Key settings in `config.py`:

| Setting | Description | Default |
|---------|-------------|---------|
| `DEBUG_MODE` | Use mock responses for testing | `False` |
| `max_tokens` | Maximum response tokens | `4000` |
| `timeout` | API request timeout (seconds) | `60` |
| `enable_consensus` | Require 2+ AI agreement | `True` |
| `parallel_requests` | Simultaneous API calls | `True` |
| `save_history` | Persist conversations | `True` |

## 🔑 API Providers

| Provider | Model | Role | Strength |
|----------|-------|------|----------|
| **Groq** | Llama 3.3 70B | SpeedCoder | Fast, creative drafts |
| **Gemini** | Gemini 2.5 Flash | Reviewer | Code analysis, optimization |
| **GLM** | GLM-4.5 | Polisher | Documentation, best practices |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for lightning-fast Llama inference
- [Google Gemini](https://ai.google.dev/) for powerful analysis capabilities
- [GLM](https://zhipuai.com/) for excellent code polishing

---

<p align="center">
  Made by Nosan (Luaapy)
</p>
