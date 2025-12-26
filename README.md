# 🚀 Hackathon II: The Evolution of Todo

**Mastering Spec-Driven Development & Cloud-Native AI**

[![Python 3.13+](https://img.shields.io/badge/python-3.13+-blue.svg)](https://www.python.org/downloads/)
[![Next.js](https://img.shields.io/badge/Next.js-15+-black.svg)](https://nextjs.org/)
[![Kubernetes](https://img.shields.io/badge/kubernetes-ready-326ce5.svg)](https://kubernetes.io/)
[![Spec-Driven](https://img.shields.io/badge/methodology-spec--driven-green.svg)](https://github.com/panaversity/spec-kit-plus)

> *"From Console to Cloud: Building AI-Powered Systems Through Progressive Evolution"*

---

## 📋 Overview

**The Evolution of Todo** is a 5-phase hackathon teaching spec-driven development from a simple console app to a cloud-native AI chatbot on Kubernetes.

### 🌟 The Journey

```
Phase I  →  Phase II  →  Phase III  →  Phase IV  →  Phase V
Console     Web App     AI Chatbot    Local K8s    Cloud Prod
Python      Next.js     MCP+Agents    Minikube     Kafka+Dapr
```

### 🏆 Competition

- **Duration**: Dec 1, 2025 → Jan 18, 2026
- **Total Points**: 1,000 + 600 bonus
- **Prize**: Top performers interview for Panaversity core team

---

## ✅ Current Status: Phase I Complete

**Phase I**: In-Memory Console App ✅  
**Location**: `phase1-cli/`  
**Status**: Fully implemented with interactive interface

### Quick Start

```bash
cd phase1-cli
pip install -e .
python -m todo_app.interactive
```

See [Phase I README](phase1-cli/README.md) for details.

---

## 📊 All Phases

| Phase | Description | Tech | Points | Due |
|-------|-------------|------|--------|-----|
| I ✅ | Console App | Python | 100 | Dec 7 |
| II 🔄 | Web App | Next.js+FastAPI | 150 | Dec 14 |
| III 📅 | AI Chatbot | OpenAI+MCP | 200 | Dec 21 |
| IV 📅 | Local K8s | Docker+Helm | 250 | Jan 4 |
| V 📅 | Cloud | Kafka+Dapr | 300 | Jan 18 |

---

## 🎯 Features

### Basic (Phase I) ✅
- Add/Delete/Update tasks
- View task list
- Mark as complete

### Intermediate (Phase II)
- Due dates & priorities
- Tags & categories
- Search & filter

### Advanced (Phase III-V)
- AI chatbot interface
- Natural language
- Recurring tasks
- Cloud deployment

---

## 🛠️ Tech Stack Evolution

**Phase I**: Python + Rich + Click  
**Phase II**: Next.js + FastAPI + PostgreSQL  
**Phase III**: OpenAI Agents + MCP SDK  
**Phase IV**: Docker + Kubernetes + Helm  
**Phase V**: Kafka + Dapr + Cloud (DO/GKE/AKS)

---

## 📚 Documentation

- **[Phase I Guide](phase1-cli/README.md)** - Complete console app docs
- **[Quick Start](phase1-cli/QUICKSTART.md)** - Interactive mode tutorial
- **[Hackathon Details](#)** - Full requirements (see below)

---

## 📤 Submission

**Form**: https://forms.gle/KMKEKaFUD6ZX4UtY8

**Required**:
1. Public GitHub repo
2. Deployed app link (Phase II+)
3. Demo video (90 sec max)
4. WhatsApp number

---

## 🎓 What You'll Learn

- Spec-Driven Development
- Full-stack with Next.js + FastAPI
- AI agents with OpenAI SDK
- Kubernetes orchestration
- Event-driven architecture (Kafka)
- AIOps (kubectl-ai, kagent, Docker AI)

---

## 📅 Timeline

| Date | Milestone |
|------|-----------|
| Dec 7 | Phase I Due |
| Dec 14 | Phase II Due |
| Dec 21 | Phase III Due |
| Jan 4 | Phase IV Due |
| Jan 18 | Phase V Due + Final |

**Live Presentations**: Sundays 8 PM PKT  
**Zoom**: https://us06web.zoom.us/j/84976847088?pwd=Z7t7NaeXwVmmR5fysCv7NiMbfbhIda.1

---

## 🏅 Scoring

| Phase | Base | Bonus | Total |
|-------|------|-------|-------|
| I | 100 | - | 100 |
| II | 150 | - | 150 |
| III | 200 | +200 | 400 |
| IV | 250 | +200 | 450 |
| V | 300 | +300 | 600 |
| **TOTAL** | **1,000** | **+600** | **1,600** |

**Bonus Opportunities**:
- Reusable Intelligence (+200)
- Cloud Blueprints (+200)
- Urdu Support (+100)
- Voice Commands (+200)

---

## 🚀 Getting Started

### Phase I (Current)

```bash
# Clone repo
git clone <your-repo>
cd ToDo-app/phase1-cli

# Install
pip install -e .

# Run interactive mode
python -m todo_app.interactive
```

### Phase II (Next)

Coming soon - Web application with Next.js frontend and FastAPI backend.

---

## 📖 Full Hackathon Details

### Phase I: Console App ✅

**Objective**: Build CLI todo app with in-memory storage

**Features**:
- Interactive menu interface
- Add, delete, update, view tasks
- Mark as complete/incomplete
- Beautiful console UI with Rich

**Tech**: Python 3.13+, Click, Rich, Pydantic

**Deliverables**:
- Constitution & specs
- Source code with clean architecture
- Tests
- Documentation (README, CLAUDE.md)

**Status**: ✅ Complete - See [phase1-cli/](phase1-cli/)

---

### Phase II: Web Application 🔄

**Objective**: Multi-user web app with database

**Features**:
- User authentication (Better Auth)
- RESTful API (FastAPI)
- Responsive frontend (Next.js)
- PostgreSQL database (Neon)
- JWT security

**API Endpoints**:
```
GET    /api/{user_id}/tasks          - List tasks
POST   /api/{user_id}/tasks          - Create task
PUT    /api/{user_id}/tasks/{id}     - Update task
DELETE /api/{user_id}/tasks/{id}     - Delete task
PATCH  /api/{user_id}/tasks/{id}/complete - Toggle
```

**Architecture**:
```
Next.js (Vercel) ←→ FastAPI ←→ Neon PostgreSQL
       ↓
  Better Auth (JWT)
```

**Due**: December 14, 2025

---

### Phase III: AI Chatbot 📅

**Objective**: Conversational AI interface with MCP

**Features**:
- OpenAI ChatKit UI
- OpenAI Agents SDK logic
- MCP server with task tools
- Natural language commands
- Stateless architecture

**MCP Tools**:
- `add_task(user_id, title, description)`
- `list_tasks(user_id, status)`
- `complete_task(user_id, task_id)`
- `update_task(user_id, task_id, ...)`
- `delete_task(user_id, task_id)`

**Examples**:
- "Add a task to buy groceries"
- "Show my pending tasks"
- "Mark task 3 as done"
- "Reschedule my morning meetings to 2 PM"

**Due**: December 21, 2025

---

### Phase IV: Local Kubernetes 📅

**Objective**: Containerize and deploy on Minikube

**Features**:
- Docker containerization (with Docker AI - Gordon)
- Helm charts for deployment
- Minikube local cluster
- kubectl-ai for AI operations
- kagent for optimization

**AIOps Examples**:
```bash
# Docker AI (Gordon)
docker ai "Build and run my app"

# kubectl-ai
kubectl-ai "deploy frontend with 2 replicas"
kubectl-ai "check why pods are failing"

# kagent
kagent "analyze cluster health"
```

**Due**: January 4, 2026

---

### Phase V: Cloud Production 📅

**Objective**: Full cloud deployment with advanced features

**Part A - Advanced Features**:
- Recurring tasks
- Due dates & reminders
- Priorities & tags
- Search, filter, sort

**Part B - Event-Driven**:
- Kafka for pub/sub (Redpanda Cloud)
- Dapr for distributed runtime
- Event-driven microservices

**Part C - Cloud Deployment**:
- DigitalOcean Kubernetes (or GKE/AKS)
- CI/CD with GitHub Actions
- Production monitoring
- Auto-scaling

**Kafka Use Cases**:
```
Task Events → Kafka → Notification Service → Reminders
           → Kafka → Recurring Task Service → New Tasks
           → Kafka → Audit Service → History
```

**Dapr Building Blocks**:
- Pub/Sub (Kafka abstraction)
- State Management
- Service Invocation
- Bindings (cron)
- Secrets Management

**Due**: January 18, 2026

---

## 🎯 Development Approach

### Spec-Driven Development Loop

```
1. Specify  → Write requirements (spec.md)
2. Plan     → Design architecture (plan.md)
3. Tasks    → Break into steps (tasks.md)
4. Implement → Code with Claude Code
5. Test     → Validate & iterate
6. Document → Update README & PHR
```

### The Agentic Dev Stack

**AGENTS.md** (Constitution) → Defines behavior  
**Spec-Kit Plus** (Architect) → Manages specs  
**Claude Code** (Builder) → Executes via MCP

**CRITICAL**: You cannot write code manually! You must:
1. Write specifications first
2. Use Claude Code to generate code
3. Refine specs until output is correct

---

## 📚 Resources

### Tools

- **Claude Code**: https://claude.com/product/claude-code
- **Spec-Kit Plus**: https://github.com/panaversity/spec-kit-plus
- **OpenAI ChatKit**: https://platform.openai.com/docs/guides/chatkit
- **MCP SDK**: https://github.com/modelcontextprotocol/python-sdk

### Cloud Services

- **Neon DB**: https://neon.tech (Free tier)
- **Vercel**: https://vercel.com (Free hosting)
- **DigitalOcean**: https://digitalocean.com ($200 credit)
- **Oracle Cloud**: https://oracle.com/cloud/free (Always free)
- **Redpanda**: https://redpanda.com/cloud (Free serverless)

### Learning

- **Minikube**: https://minikube.sigs.k8s.io
- **Helm**: https://helm.sh
- **Dapr**: https://dapr.io
- **kubectl-ai**: https://github.com/sozercan/kubectl-ai
- **kagent**: https://github.com/k8sgpt-ai/k8sgpt

---

## ❓ FAQ

**Q: Can I skip phases?**  
A: No, complete in order. Each builds on previous.

**Q: Can I use different tech?**  
A: Core stack must stay. You can add extras.

**Q: Team or individual?**  
A: Individual. Submit separately.

**Q: What if incomplete?**  
A: Submit what you have. Partial credit given.

**Q: WSL 2 required?**  
A: Phase IV+ (Docker/K8s). Phase I-III work on Windows.

---

## 👥 Organized By

**Panaversity** (panaversity.org)  
**PIAIC** - Presidential Initiative for AI & Computing  
**GIAIC** - Governor's Initiative for AI & Computing

**Led by**: Zia Khan, Rehan, Junaid, Wania

**🌟 Top performers** may be invited to join Panaversity core team as startup founders.

---

## 🎉 Let's Build!

Ready to evolve from console to cloud? Start with Phase I!

**📖 [Phase I Complete Guide](phase1-cli/README.md)**

**Good luck, and may your specs be clear and your code be clean!** 🚀

---

*Hackathon II: The Evolution of Todo*  
*December 1, 2025 - January 18, 2026*