# mcp-server-with-semantic-kernel
Building Semantic Kernel Agents with Model Context Protocol (MCP) Plugins in Python

[Using MCP Servers with Semantic Kernel in Python](https://developers.onwardplatforms.com/blog/2025/04/14/using-mcp-servers-with-semantic-kernel-in-python)

## What is Semantic Kernel?

Semantic Kernel (SK) is an open-source toolkit created by Microsoft that helps developers build powerful AI agents and apps that can talk, think, and act.

### Think of it like this:

Imagine you're building a robot assistant. This assistant can:
1. Talk using ChatGPT or other AI models (like asking questions or answering)
2. Do tasks like checking your calendar, sending emails, or summarizing documents
3. Remember things it has done or seen before
4. Learn and follow workflows you teach it

SK is the brain behind this assistant. It connects the language part (like ChatGPT) with the tools and memory part (your calendar, files, APIs, etc.).

---

## Key Building Blocks of SK

| Concept | Beginner Explanation |
|---------|---------------------|
| Kernel | The central piece that connects everything. It talks to the AI model and runs your instructions. |
| Plugins / Skills | These are like apps for your assistant. For example: a calendar plugin, or an email plugin. |
| Prompt Templates | Prewritten instructions that tell the AI how to behave. You give it some variables, it fills in the rest. Like: "Summarize this: {{text}}." |
| Memory | It lets your assistant "remember" past things—like past conversations, or data. |
| Planner / Orchestrator | If your assistant has to do 5 steps to finish something (e.g. plan a trip), this part figures out the steps. |

### Example in Simple Terms

Let's say you're building a "Meeting Assistant" using Semantic Kernel:
- You give it a plugin called CalendarSkill that knows how to read and create calendar events
- You write a prompt: "Schedule a 30-minute meeting with John sometime next week."
- The Semantic Kernel takes your prompt, sends it to the AI (like ChatGPT), figures out the intent ("create event"), and then runs the plugin to do it

So SK = AI (understands language) + Tools (do actions) + Memory (remembers stuff)

## Semantic Kernel (SK) vs Model Context Protocol (MCP)

| Feature | Semantic Kernel (SK) | Model Context Protocol (MCP) |
|---------|---------------------|----------------------------|
| What it is | A toolkit/framework to build intelligent AI agents | A standard/protocol for exposing tools to LLMs |
| Who created it | Microsoft | Open standard (inspired by tools like OpenAI tool calling, Claude tool use) |
| Main Job | Let you connect an AI model with memory, tools, and prompts | Let AI agents talk to tools via a common format |
| Think of it as | The brain + logic + app store of an AI agent | The interface/plug for tools to work with any AI agent |
| Does it have memory? | Yes, SK can store and recall things (e.g. vector memory) | No, it doesn't handle memory itself |
| Tool usage | You define and load "skills" (functions/tools) in code | Tools are exposed as MCP Servers, any agent can connect |
| Language focus | Python / C# SDKs | Language-agnostic (focuses on the format, not the implementation) |
| Complexity | Higher-level abstraction (like a full toolkit) | Lower-level protocol (like a wire format or spec) |

## Communication Methods

### 1. Server-Sent Events (SSE)

**TL;DR:** SSE is a way for a server to send real-time updates to your app over the web.

**Think of it like:**
You're at a coffee shop. You give the barista your order (a request), and instead of checking back constantly, you just sit and relax. When your drink is ready, they call your name.

**How it works:**
- The client makes a one-time request
- The server keeps that connection open
- Whenever there's data, the server sends it as a stream
- The client gets updates in real time

**In MCP or AI apps:**
When an AI tool talks to a tool server (via MCP), the server may stream results gradually — like partial answers, tokens, or logs.

### 2. Standard Input/Output (stdio)

**TL;DR:** stdio is how your computer's command-line tools read input and write output.

**How it works:**
- stdin: You type or send data into a program
- stdout: The program prints the result
- stderr: Errors go here (so they don't mix with normal output)

**In MCP:**
MCP Servers can be run as command-line programs. The agent talks to them by:
- Writing JSON input into stdin
- Reading the tool's response from stdout

## Communication Methods Comparison

| Feature | SSE | stdio |
|---------|-----|-------|
| Type | Web protocol | Local program communication |
| Used for | Streaming real-time data from servers | Talking to command-line tools or subprocesses |
| Agent use | When MCP tool is running as a web server | When MCP tool is a local process |
| Connection | Client keeps a live HTTP connection open | Input/output pipes (like running a script) |
| Example | Live chat, streaming tokens from LLM | Shell script reading a prompt and printing answer |

### In AI Tooling (like MCP):
- If a tool is deployed on a web server → use SSE to stream responses
- If a tool is a local binary/script → use stdio to send/receive data


