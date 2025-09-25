# Login-Credentials - Projet Playwright avec POM

Projet d’automatisation de tests en Python avec [Playwright](https://playwright.dev/python/), organisé selon le modèle **Page Object Model (POM)**.


## Installation

### 1. Cloner le projet

git clone https://github.com/Vianney97/Login-Credentials.git
cd Login-Credentials


### 2. Créer et activer un environnement virtuel
python -m venv venv
# Windows PowerShell
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

### 3. Créer et activer un environnement virtuel
pip install playwright python-dotenv
playwright install

### 4. Configuration
Créer un fichier .env à la racine

LOGIN_URL=https://ton-site.fr/login](https://www.demarches-simplifiees.fr/users/sign_in
LOGIN_EMAIL=mon.email@example.com
LOGIN_PASSWORD=monMotDePasse

### 5. Lancer un test
python main.py
