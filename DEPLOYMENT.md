# AF IMPERIYA - Deployment Guide

Bu qo'llanma sizga AF IMPERIYA tizimini turli platformalarga deploy qilishda yordam beradi.

## 🚀 Render.com ga Deploy (Tavsiya etiladi)

### Tayyor bo'lish

1. **GitHub Repository yarating**
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   git remote add origin <your-github-repo-url>
   git push -u origin main
   ```

2. **Render.com'ga kiring**
   - [render.com](https://render.com) saytiga o'ting
   - GitHub akkauntingiz bilan kiring

### Web Service yaratish

1. **New Web Service**
   - Dashboard > "New +" > "Web Service"
   - GitHub repository'ni tanlang
   - Branch: `main` (yoki sizning branchingiz)

2. **Sozlamalar**
   ```
   Name: af-imperiya
   Region: Frankfurt (yoki Singapore)
   Branch: main
   Runtime: Python 3
   Build Command: pip install -r requirements.txt
   Start Command: gunicorn app:app
   ```

3. **Plan tanlash**
   - Free (test uchun)
   - Starter ($7/month - production uchun)
   - Professional ($25/month - katta proyekt uchun)

4. **Environment Variables**
   
   Advanced > Environment Variables > "Add Environment Variable"
   
   ```env
   SECRET_KEY=your-secret-key-here-make-it-long-and-random
   TELEGRAM_BOT_TOKEN=1234567890:ABCdefGHIjklMNOpqrsTUVwxyz
   ```

5. **Deploy**
   - "Create Web Service" tugmasini bosing
   - Deploy jarayoni 5-10 daqiqa davom etadi
   - Log'larni kuzating

### PostgreSQL Database yaratish

1. **New PostgreSQL**
   - Dashboard > "New +" > "PostgreSQL"
   - Name: `af-imperiya-db`
   - Region: Web service bilan bir xil
   - Plan: Free (test) yoki Starter (production)

2. **Connection**
   - Database yaratilgandan keyin "Internal Database URL"ni ko'chirib oling
   - Web Service > Environment > Add Environment Variable
   ```
   DATABASE_URL=<internal-database-url>
   ```

3. **Database Migration**
   Deploy tugagach, Render Shell'da:
   ```bash
   python
   >>> from app import app, db
   >>> with app.app_context():
   ...     db.create_all()
   >>> exit()
   ```

### Telegram Bot Webhook sozlash

Deploy tugagach:

```bash
curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://your-app.onrender.com/telegram-webhook"
```

Yoki Python'da:
```python
import requests
bot_token = "YOUR_BOT_TOKEN"
webhook_url = "https://your-app.onrender.com/telegram-webhook"
requests.post(f"https://api.telegram.org/bot{bot_token}/setWebhook", 
              data={"url": webhook_url})
```

## 🐳 Docker bilan Deploy

### Dockerfile yaratish

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN mkdir -p uploads

ENV FLASK_APP=app.py
ENV PORT=8000

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "--workers", "4", "app:app"]
```

### Docker Compose

```yaml
version: '3.8'

services:
  web:
    build: .
    ports:
      - "8000:8000"
    environment:
      - DATABASE_URL=postgresql://user:password@db:5432/afimperiya
      - SECRET_KEY=your-secret-key
    depends_on:
      - db
    volumes:
      - ./uploads:/app/uploads

  db:
    image: postgres:15
    environment:
      - POSTGRES_USER=user
      - POSTGRES_PASSWORD=password
      - POSTGRES_DB=afimperiya
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

### Ishga tushirish

```bash
docker-compose up -d
docker-compose exec web python -c "from app import app, db; db.create_all()"
```

## ☁️ Heroku ga Deploy

### Tayyor bo'lish

```bash
# Heroku CLI o'rnatish
brew install heroku/brew/heroku  # Mac
# yoki
curl https://cli-assets.heroku.com/install.sh | sh  # Linux

# Login
heroku login
```

### App yaratish

```bash
heroku create af-imperiya

# PostgreSQL qo'shish
heroku addons:create heroku-postgresql:mini

# Environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set TELEGRAM_BOT_TOKEN=your-token

# Deploy
git push heroku main

# Database migration
heroku run python
>>> from app import app, db
>>> with app.app_context():
...     db.create_all()
```

## 🌐 Railway.app ga Deploy

### Web UI orqali

1. [railway.app](https://railway.app) ga kiring
2. "New Project" > "Deploy from GitHub repo"
3. Repository tanlang
4. Avtomatik deploy boshlanadi
5. Environment variables qo'shing
6. PostgreSQL plugin qo'shing

### CLI orqali

```bash
# Railway CLI o'rnatish
npm install -g @railway/cli

# Login
railway login

# Init
railway init

# Deploy
railway up

# Environment variables
railway variables set SECRET_KEY=your-key
railway variables set TELEGRAM_BOT_TOKEN=your-token

# Database qo'shish
railway add postgres
```

## 🖥️ VPS (DigitalOcean, AWS, etc.) ga Deploy

### Server sozlash (Ubuntu 22.04)

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Python va dependencies
sudo apt install python3-pip python3-venv nginx -y

# PostgreSQL
sudo apt install postgresql postgresql-contrib -y

# Setup database
sudo -u postgres psql
CREATE DATABASE afimperiya;
CREATE USER afimperiya_user WITH PASSWORD 'strong_password';
GRANT ALL PRIVILEGES ON DATABASE afimperiya TO afimperiya_user;
\q
```

### Application setup

```bash
# Clone repository
cd /var/www
sudo git clone <your-repo> af-imperiya
cd af-imperiya

# Virtual environment
sudo python3 -m venv venv
sudo venv/bin/pip install -r requirements.txt

# Environment file
sudo nano .env
```

`.env` fayli:
```env
DATABASE_URL=postgresql://afimperiya_user:strong_password@localhost/afimperiya
SECRET_KEY=your-secret-key
TELEGRAM_BOT_TOKEN=your-token
```

### Gunicorn service

```bash
sudo nano /etc/systemd/system/afimperiya.service
```

```ini
[Unit]
Description=AF IMPERIYA Web Application
After=network.target

[Service]
User=www-data
WorkingDirectory=/var/www/af-imperiya
Environment="PATH=/var/www/af-imperiya/venv/bin"
ExecStart=/var/www/af-imperiya/venv/bin/gunicorn --workers 4 --bind 127.0.0.1:8000 app:app

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl start afimperiya
sudo systemctl enable afimperiya
```

### Nginx sozlash

```bash
sudo nano /etc/nginx/sites-available/afimperiya
```

```nginx
server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://127.0.0.1:8000;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
    }

    location /uploads {
        alias /var/www/af-imperiya/uploads;
    }
}
```

```bash
sudo ln -s /etc/nginx/sites-available/afimperiya /etc/nginx/sites-enabled/
sudo nginx -t
sudo systemctl restart nginx
```

### SSL (Let's Encrypt)

```bash
sudo apt install certbot python3-certbot-nginx -y
sudo certbot --nginx -d your-domain.com
```

## 🔒 Production Checklist

- [ ] SECRET_KEY o'zgartirildi va xavfsiz
- [ ] PostgreSQL parol kuchli va maxfiy
- [ ] DEBUG=False
- [ ] HTTPS (SSL) sozlandi
- [ ] Database backup sozlandi
- [ ] Firewall sozlandi
- [ ] Monitoring qo'shildi (Sentry, etc.)
- [ ] Log rotation sozlandi
- [ ] Environment variables xavfsiz
- [ ] Static fayllar CDN orqali serve qilinadi
- [ ] Database indexlar qo'shildi
- [ ] Rate limiting qo'shildi

## 📊 Monitoring va Logging

### Sentry (Error tracking)

```python
# requirements.txt ga qo'shing
sentry-sdk[flask]==1.38.0
```

```python
# app.py ga qo'shing
import sentry_sdk
from sentry_sdk.integrations.flask import FlaskIntegration

sentry_sdk.init(
    dsn="your-sentry-dsn",
    integrations=[FlaskIntegration()],
    traces_sample_rate=1.0
)
```

### Logging

```python
# app.py da
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('app.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
```

## 🔄 Auto-deployment (CI/CD)

### GitHub Actions

`.github/workflows/deploy.yml`:

```yaml
name: Deploy to Render

on:
  push:
    branches: [main]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Render
        run: |
          curl -X POST ${{ secrets.RENDER_DEPLOY_HOOK }}
```

## 🆘 Troubleshooting

### Database connection issues
```bash
# Check DATABASE_URL
echo $DATABASE_URL

# Test connection
psql $DATABASE_URL

# Reset migrations
rm -rf migrations/
flask db init
flask db migrate
flask db upgrade
```

### Application won't start
```bash
# Check logs
heroku logs --tail  # Heroku
railway logs  # Railway
journalctl -u afimperiya -f  # VPS

# Check process
ps aux | grep gunicorn
```

### Static files not loading
```bash
# Collect static files
flask collect-static

# Check permissions
chmod -R 755 uploads/
```

## 📞 Support

Muammolar yuzaga kelsa:
- GitHub Issues
- Email: support@afimperiya.uz
- Telegram: @afimperiya_support

---

**Good luck with your deployment!** 🚀
