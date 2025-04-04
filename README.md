# 🤖 AI Multi-Agent Hands-on Project with PhiData + Groq + Tools  

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Kajaani-Balabavan/ai-multi-agent-hands-on/blob/main/agent_demo.ipynb)

This project was built by following this awesome YouTube tutorial:  
🎥 [Create an Agent App with Groq + Phi](https://www.youtube.com/watch?v=mDOqyIk_lLk&t=684s)

---

## 🎯 Purpose  
I built this project to get **hands-on experience** with AI agents using [phidata](https://pypi.org/project/phidata/) and [Groq](https://groq.com/), while also integrating real-world tools like YouTube summarization and Google search.

---

## 🛠️ What’s Inside  

✅ **Phi Agents**  
✅ **Groq model** (`deepseek-r1-distill-llama-70b`)  
✅ **YouTube Tools** – for summarizing videos and fetching latest uploads  
✅ **Google Search Agent** – fetches real-time info in English and Tamil  
✅ **Team Agent** – combines both for full video + channel insights  

---

## 🧪 Sample Usage

```python
team_Agents.print_response("Summarize this video https://www.youtube.com/watch?v=Lp0mT42kepg&list=PL0N0mLMfepi-olljfgwmypvkOq2xtGHZE&index=5 and provide latest information about Department of Computer Science & Engineering channel", markdown=True, stream= True)
```

---

## 🧠 Agents

### 🎥 YouTube Agent
- Summarizes a given video  
- Provides recent video uploads from the same channel

### 🌐 Web Agent
- Uses Google to find latest information about the channel  
- Supports English and Tamil  
- Filters top 4 unique news items

### 🤝 Team Agent
- Combines YouTube + Web agents  
- Provides a full report for any given video/channel combo

---

## 📦 Installation

```bash
pip install phidata
pip install groq
pip install python-dotenv
pip install -U youtube_transcript_api
pip install -U googlesearch-python pycountry
```

---

## 🔑 .env File

Create a `.env` file in your project root:
```env
GROQ_API_KEY = "your_groq_api_key_here"
```

---

## ⭐️ Credits  
Huge thanks to the video that helped me build this:  
📺 [YouTube Tutorial](https://www.youtube.com/watch?v=mDOqyIk_lLk&t=684s)  

