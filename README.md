# AF IMPERIYA - Enterprise Boshqaruv Tizimi

🚀 **Professional enterprise management system with 13+ modules**

## 📋 Xususiyatlar

### 🎯 Asosiy Funksiyalar
- ✅ **4 xil panel**: Admin, Rahbar, Xodim, User
- ✅ **13 ta to'liq modul**: Topshriqlar, Transport, Binolar, Yashil makonlar va boshqalar
- ✅ **Role-based Access Control (RBAC)**: Har bir foydalanuvchi o'z roli bo'yicha kirish huquqiga ega
- ✅ **Telegram Bot integratsiyasi**: Real-time bildirishnomalar
- ✅ **PDF/Excel Export**: Har bir modulda hisobotlarni yuklab olish
- ✅ **Real-time notifications**: Vazifalar va o'zgarishlar haqida darhol xabardor bo'ling
- ✅ **File Upload**: Rasmlar, PDF, Excel, Word fayllarni yuklash
- ✅ **Dashboard with Charts**: Grafiklar bilan zamonaviy dashboard
- ✅ **Responsive Design**: Mobil va desktop qurilmalarda ishlaydi
- ✅ **O'zbekiston ranglari**: Milliy ranglar bilan dizayn

### 📦 13 ta Modul

1. **Topshriqlar** - Admin tomonidan berish, xodimlar bajarish, rahbar tasdiqlash
2. **Avto Transport** - Mashina ma'lumotlari, haydovchilar, remont tarixi
3. **Ijro** - Real-time chat, status tracking, Telegram push notifications
4. **Binolar** - Kategoriyalar, bino ma'lumotlari
5. **Yashil Makonlar** - O'simliklar, parvarish jadvali
6. **Quyosh Panellari** - Solar panel ma'lumotlari, monitoring
7. **Xodimlar** - Rezume, statistika, modul biriktirish
8. **Tasks (Kanban)** - Kanban board stil
9. **Outsorsing** - Xizmatlar, shartnomalar
10. **Tashkilotlar** - Kompaniya ma'lumotlari
11. **Mehmonlar** - Mehmon registratsiyasi, xarajatlar
12. **Tabriknomalar** - Tug'ilgan kunlar, sovg'alar
13. **Shartnomalar** - PDF/Excel yuklash, holat tracking

## 🚀 Tezkor Boshlash

### Lokal Ishga Tushirish

```bash
# 1. Repository'ni clone qiling
git clone <repository_url>
cd af_imperiya_full

# 2. Virtual environment yarating
python -m venv venv
source venv/bin/activate  # Linux/Mac
# yoki
venv\Scripts\activate  # Windows

# 3. Dependencies o'rnating
pip install -r requirements.txt

# 4. Database yarating
python app.py

# 5. Serverni ishga tushiring
python app.py
```

Server http://localhost:5000 da ishga tushadi

### Default Login Ma'lumotlari

```
Email: admin@afimperiya.uz
Parol: admin123
```

## 🌐 Render.com ga Deploy Qilish

### 1-usul: GitHub orqali (Tavsiya etiladi)

1. Loyihani GitHub'ga yuklang
2. [Render.com](https://render.com) ga kiring
3. "New +" > "Web Service" tanlang
4. GitHub repository'ni tanlang
5. Quyidagi sozlamalarni kiriting:
   - **Name**: af-imperiya
   - **Environment**: Python
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
   - **Plan**: Free yoki Professional
6. **Environment Variables** qo'shing:
   ```
   SECRET_KEY=<random_secret_key>
   DATABASE_URL=<postgresql_url>
   TELEGRAM_BOT_TOKEN=<your_bot_token>
   ```
7. "Create Web Service" tugmasini bosing

### 2-usul: render.yaml bilan

`render.yaml` fayli allaqachon tayyor. Faqat quyidagilarni bajaring:

1. GitHub'ga push qiling
2. Render.com'da "New +" > "Blueprint" tanlang
3. Repository'ni tanlang
4. Render avtomatik tarzda barcha servicelarni yaratadi

### Database (PostgreSQL)

Render avtomatik PostgreSQL database yaratadi. Agar manual yaratmoqchi bo'lsangiz:

1. Render.com'da "New +" > "PostgreSQL" tanlang
2. Database nomini kiriting
3. Create tugmasini bosing
4. DATABASE_URL'ni Web Service'ga environment variable sifatida qo'shing

## 🤖 Telegram Bot Sozlash

1. [@BotFather](https://t.me/botfather) orqali bot yarating
2. Bot token olasiz
3. Environment variable sifatida qo'shing:
   ```
   TELEGRAM_BOT_TOKEN=your_bot_token_here
   ```
4. Webhook sozlang (Render deploy bo'lgandan keyin):
   ```bash
   curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://your-app.onrender.com/telegram-webhook"
   ```

## 📱 Foydalanish

### Admin Panel
- Barcha foydalanuvchilarni boshqaring
- Rollarni o'zgartiring
- Tizim statistikasini ko'ring
- Modullarni biriktiring

### Rahbar Paneli
- Barcha modullarga kirish
- Xodimlarni nazorat qilish
- Topshiriqlarni tasdiqlash
- Hisobotlarni ko'rish

### Xodim Paneli
- Biriktirilgan modullarda ishlash
- Topshiriqlarni bajarish
- Hisobotlar yaratish

### User Panel
- So'rovnoma yuborish
- Umumiy ma'lumotlarni ko'rish

## 🔒 Xavfsizlik

- ✅ Password hashing (Werkzeug)
- ✅ Session management (Flask-Login)
- ✅ CSRF protection
- ✅ SQL injection himoyasi (SQLAlchemy ORM)
- ✅ Role-based access control
- ✅ File upload validation

## 📊 Texnologiyalar

### Backend
- **Flask 3.0** - Web framework
- **SQLAlchemy** - ORM
- **PostgreSQL** - Production database
- **SQLite** - Development database

### Frontend
- **HTML5 / CSS3**
- **JavaScript (Vanilla)**
- **Font Awesome** - Icons
- **Google Fonts** - Inter & Poppins

### Deployment
- **Gunicorn** - WSGI server
- **Render.com** - Cloud platform

### Kutubxonalar
- **openpyxl** - Excel generation
- **reportlab** - PDF generation
- **Pillow** - Image processing
- **requests** - HTTP requests

## 📁 Loyiha Strukturasi

```
af_imperiya_full/
├── app.py                 # Asosiy Flask app
├── models.py              # Database models
├── config.py              # Konfiguratsiya
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment config
├── render.yaml           # Render.com config
├── uploads/              # Yuklangan fayllar
│   ├── vehicles/
│   ├── buildings/
│   ├── tasks/
│   └── ...
├── templates/            # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── tasks/
│   ├── vehicles/
│   ├── admin/
│   └── ...
└── README.md
```

## 🎨 Dizayn Xususiyatlari

- **O'zbekiston milliy ranglari**: Ko'k (#0084d4), Yashil (#1eb53a), Qizil (#e31e25)
- **Zamonaviy UI/UX**: Clean, professional dizayn
- **Responsive**: Mobile-first approach
- **Dark sidebar**: Professional ko'rinish
- **Animated elements**: Smooth transitions
- **Color-coded status**: Vizual feedback

## 🔄 Database Migrations

Agar database strukturasini o'zgartirsangiz:

```python
# Python shell'da
from app import app, db
with app.app_context():
    db.create_all()
```

## 🐛 Troubleshooting

### Database xatosi
```bash
# Database'ni reset qilish
rm af_imperiya.db
python app.py
```

### Permission xatosi
```bash
# Uploadsdirectory'ga ruxsat berish
chmod 755 uploads/
```

### Telegram bot ishlamayapti
- Bot token to'g'ri ekanligini tekshiring
- Webhook URL to'g'ri sozlanganligini tekshiring
- Internet ulanishini tekshiring

## 📞 Yordam va Support

Muammolar yoki savollar bo'lsa:
1. GitHub Issues ochish
2. Email: support@afimperiya.uz
3. Telegram: @afimperiya_support

## 📄 Litsenziya

MIT License - Batafsil ma'lumot uchun LICENSE faylini ko'ring

## 🙏 Minnatdorchilik

- Flask community
- Render.com
- All contributors

## 📈 Kelajakdagi Yangilanishlar

- [ ] Mobile app (React Native)
- [ ] Advanced analytics
- [ ] Multi-language support
- [ ] Calendar integration
- [ ] Email notifications
- [ ] Advanced reporting
- [ ] API documentation
- [ ] Docker support

---

**Built with ❤️ in Uzbekistan** 🇺🇿

**Version**: 1.0.0  
**Last Updated**: November 2024
