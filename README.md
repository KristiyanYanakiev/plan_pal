# PlanPal

PlanPal is a Django-based social planning platform designed for groups of friends to organize events, propose activities, vote on participation, and manage social coordination in a structured and transparent way.

The system replaces informal group chat planning with a centralized application where users can create proposals, invite participants, vote, and comment in real time.

---

## ✨ Features

### 👥 User & Friends System
- User registration, login, logout
- Extended Django User model (custom user system)
- Friend request system:
  - Send friend requests
  - Accept / reject requests
  - View friends list

---

### 📅 Proposal System
- Create, edit, and delete event proposals
- Assign participants to proposals (friends only)
- Add notes and event details
- Date validation (no past events allowed)
- Filtered proposal access per user (participants + owner only)

---

### 🗳 Voting System
- Vote YES / NO for each proposal
- Users can change their vote (update_or_create logic)
- Live vote tracking:
  - Yes votes
  - No votes
  - Users who have not voted yet
- Owner cannot vote on their own proposal

---

### 💬 Comments System
- Add comments to proposals
- Delete own comments
- Comment access restricted to participants and owner

---

### 🔎 Search & Filtering
- Search proposals by title
- Filter proposals by user participation

---

### 🌐 REST API (Django REST Framework)
- Proposal API endpoints implemented using DRF
- Serializer-based architecture
- Authentication-protected endpoints
- Structured JSON responses for proposals

---

### 📊 Dashboard Features
- Upcoming vs past events (computed dynamically)
- Proposal participation overview
- Voting status overview per user

---

### 🎨 UI / UX
- Responsive design using Bootstrap 5
- Reusable base template with navigation and footer
- Clean and consistent layout across all pages
- Conditional navigation based on authentication status

---

### ⚠️ Error Handling
- Custom 404 page
- Custom 500 page
- User-friendly validation error messages

---

## 🧠 Concept

PlanPal is designed to simplify group coordination for friends.

Instead of managing plans in chat applications, users create structured event proposals:

> “Bowling Friday at 19:00?”

Friends are added as participants, vote on attendance, and leave comments for clarification.

The system ensures:
- Transparency
- Organization
- Easy decision-making

---

## 🏗 Data Model

Main entities:

- **CustomUser** — extended Django user model
- **FriendRequest** — manages friendships between users
- **Proposal** — event/activity proposal
- **Vote** — YES/NO response per user per proposal
- **Comment** — user discussion on proposals

### Relationships:
- User ↔ User (friend system)
- User → Proposal (owner)
- Proposal ↔ Users (participants M2M)
- User → Vote (FK)
- Proposal → Vote (FK)
- User → Comment (FK)
- Proposal → Comment (FK)

---

## 🛠 Tech Stack

- Python 3.11+
- Django 4+
- Django REST Framework
- PostgreSQL
- Bootstrap 5

---

## ⚙️ Requirements

- Python 3.10+
- PostgreSQL
- pip / virtualenv

---

## ▶ Run Locally

### 1. Clone the repository
git clone https://github.com/KristiyanYanakiev/plan_pal.git
cd plan_pal

### 2. Create a virtual environment
python3 -m venv venv
source venv/bin/activate      # Linux / Mac \
venv\Scripts\activate         # Windows

### 3. Install dependencies
pip install -r requirements.txt

### 4. Setup environment variables
cp .env.example .env
### Then edit .env to configure your PostgreSQL credentials

### 5. Create PostgreSQL database matching DB_NAME
Example: create a database named 'plan_pal'

### 6. Apply migrations
python3 manage.py migrate

### 7. Create admin user
python3 manage.py createsuperuser

### 8. Run the development server
python3 manage.py runserver

### Open in your browser:
http://127.0.0.1:8000/

