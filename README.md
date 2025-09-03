
---

# 🍲 ChakulaHub – Recipe Hackathon Project

> *Discover recipes, share the taste. AI-powered culinary exploration.*

---

HOW IT WORKS 
 [ User Browser ]  
       |  
       v  
 [ Recipe Website Frontend ]  
 (Search bar, UI, Download button)  
       |  
       v  
 [ AI Engine / Backend ]  
 (Processes request, generates recipe + diagram)  
       |  
       v  
 [ Recipe Results + Summary ]  
       |  
       v  
 [ Download as PDF / Text ]  


## 👨‍👩‍👧‍👦 Team Members – Coders Cave Crew

| Name  | Role                             | Contributions                                                                                                          |
| ----- | -------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
|  Samson Mbugua | **Team Lead & Backend Engineer** | Managed team workflow, handled API endpoints. 
            |
|  Festus Daudi | **Frontend Developer**           | Built responsive UI (HTML/CSS/JS), designed hero/search interface, styled result cards, implemented responsive footer. |

| Lukoye Jackson | **AI/ML Engineer**               | Integrated Hugging Face GPT-2 for recipe summarization, fine-tuned model prompts, ensured AI-powered descriptions.     |
                   **Security & Testing Engineer**  | Implemented input validation, secured API keys, wrote unit & integration tests, tested M-Pesa sandbox payments.  

| Samuel Musili | **API Integration Specialist**   | Connected with TheMealDB API, handled search/filtering of recipes, managed error handling and data formatting.         |

| Ivy Liz Nyawira | **Documentation & Deployment**   | Authored README, managed GitHub repo, wrote API usage guide, deployed project on Netlify/Render.                       |

---

# Contributors  
Here are the contributors to this project:  

| Name               | Email                         |
|--------------------|-------------------------------|
| Lukoye Jackson     | lukoyejackson77@gmail.com     |
| Samson Mbugua      | officialson03@gmail.com       |
| Samuel Musili      | musilisam20@gmail.com         |
| Ivy Liz Nyawira    | kish.liz10349@gmail.com       |
| Festus Daudi       | daudifestus@gmail.com         |

---

© 2025 THE CODERS CAVE  

## 🏆 Judging Criteria Breakdown

### 1. **Code Quality (20%)** 💻

* Clean, modular, and well-documented code.
* Followed **best practices** for naming conventions, reusable functions, and separation of concerns.

### 2. **Algorithm Efficiency (20%)** 

* Optimized recipe search & filtering using asynchronous JavaScript.
* Efficient handling of API responses with minimal resource consumption.

### 3. **Utilization of Technology Stack (14%)** 🌐

* **Frontend:** HTML, CSS, JS
* **Backend:** Python, MySQL
Python, Mysql
* **AI:** Hugging Face GPT-2 for recipe descriptions
* **Deployment:** Vercel (frontend) + Render (backend)

### 4. **Security & Fault Tolerance (12%)** 🔒

* API keys stored in `.env` file (never exposed).
* Error handling for API requests
* Validation of user inputs to prevent injection attacks.

### 5. **Performance (16%)** 🚀

* Fast recipe search (debounced API calls).
* Optimized images & assets for faster load times.
* Backend caching for frequently searched recipes.

### 6. **Development Process (10%)** 

* Used **GitHub Projects** for task tracking.
* Team collaboration via Git & pull requests.
* Clear division of roles across all 5 members.

### 7. **Documentation & Testing (8%)** 📖

* Comprehensive **README.md** (this file).
* Unit & integration tests for search and payment workflows.
* Manual + automated testing ( recipe API).

---

## ⚙️ Features

✅ Recipe Search by ingredient or keyword
✅ AI-powered recipe descriptions (Hugging Face GPT-2)
✅ Secure & optimized backend
✅ Fully responsive UI

---

## 🚀 Installation

1. Clone repo:

   ```bash
   git clone https://github.com/CodersCave/ChakulaHub.git
   cd ChakulaHub
   ```

2. Install dependencies:

   ```bash
   npm install
   ```

3. Create `.env` file:

   ```
   HF_API_KEY=your_huggingface_key
   
   ```
4. Run locally:

   ```bash
   npm start
   ```

---

## 📡 API References

* **TheMealDB API** → Recipe search & data
* **Hugging Face GPT-2** → AI text generation

---

## 👨‍⚖️ License

© 2025 THE CODERS CAVE – All rights reserved.

---

