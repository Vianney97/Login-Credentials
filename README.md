# Login-Credentials — Automatisation de tests avec Playwright (POM)

Projet d'automatisation de tests de connexion en Python avec [Playwright](https://playwright.dev/python/), organisé selon le modèle **Page Object Model (POM)**.

## Prérequis

- Python 3.8+
- pip

## Structure du projet

```
Login-Credentials/
├── pages/
│   └── login_page.py   # Page Object : page de connexion
├── tests/
│   └── test_login.py   # Scénario de test de connexion
├── main.py             # Point d'entrée
├── .env                # Variables d'environnement (non versionné)
└── README.md
```

## Installation

### 1. Cloner le projet

```bash
git clone https://github.com/Vianney97/Login-Credentials.git
cd Login-Credentials
```

### 2. Créer et activer un environnement virtuel

```bash
python -m venv venv
```

- **Windows (PowerShell) :**

```powershell
.\venv\Scripts\activate
```

- **Linux / macOS :**

```bash
source venv/bin/activate
```

### 3. Installer les dépendances

```bash
pip install playwright python-dotenv
playwright install
```

## Configuration

Créer un fichier `.env` à la racine du projet avec les variables suivantes :

```env
LOGIN_URL=https://www.demarches-simplifiees.fr/users/sign_in
LOGIN_EMAIL=mon.email@example.com
LOGIN_PASSWORD=monMotDePasse
```

> ⚠️ Le fichier `.env` est ignoré par Git (voir `.gitignore`). Ne le commitez jamais.

## Lancer les tests

```bash
python main.py
```

En cas de succès, le message suivant s'affiche dans le terminal :

```
✅ Message 'Connecté(e).' trouvé
```
