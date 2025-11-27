# AF IMPERIYA - Tezkor Boshlash (O'zbekcha)

## 🎯 Bu nima?

**AF IMPERIYA** - bu to'liq professional enterprise boshqaruv tizimi bo'lib, 13 ta modul, Telegram bot integratsiyasi, PDF/Excel export va zamonaviy dizaynga ega.

## ⚡ Tezkor Boshlash (3 daqiqa)

### Windows'da

1. Fayllarni yuklab oling
2. `start.bat` faylini ikki marta bosing
3. Brauzerda `http://localhost:5000` ga o'ting
4. Login qiling:
   - **Email**: `admin@afimperiya.uz`
   - **Parol**: `admin123`

### Mac/Linux'da

```bash
./start.sh
```

Yoki:

```bash
# 1. Virtual environment yarating
python3 -m venv venv
source venv/bin/activate

# 2. Dependencies o'rnating
pip install -r requirements.txt

# 3. Database yarating
python init_db.py

# 4. Serverni ishga tushiring
python app.py
```

## 🌐 Internet'ga Chiqarish (Render.com)

### 1-qadam: GitHub'ga yuklash

```bash
# Proyektni GitHub'ga yuklang
git init
git add .
git commit -m "AF IMPERIYA system"
git remote add origin https://github.com/USERNAME/af-imperiya.git
git push -u origin main
```

### 2-qadam: Render.com'da deploy qilish

1. [render.com](https://render.com) ga kiring (GitHub bilan)
2. "New +" tugmasini bosing
3. "Web Service" ni tanlang
4. GitHub repository'ni tanlang
5. Quyidagi ma'lumotlarni kiriting:
   - **Name**: `af-imperiya`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app`
6. Environment Variables qo'shing:
   ```
   SECRET_KEY = <random_secret_key>
   ```
7. "Create Web Service" tugmasini bosing
8. 5-10 daqiqa kutib turing

### 3-qadam: Database sozlash

1. Render.com'da "New +" > "PostgreSQL"
2. Database yarating
3. "Internal Database URL" ni ko'chiring
4. Web Service > Environment ga qo'shing:
   ```
   DATABASE_URL = <internal-database-url>
   ```

### 4-qadam: Database yaratish

Deploy tugagandan keyin, Render Shell'da:

```bash
python init_db.py
```

## 🤖 Telegram Bot

### Bot yaratish

1. Telegram'da [@BotFather](https://t.me/botfather) ga o'ting
2. `/newbot` buyrug'ini yuboring
3. Bot nomini kiriting: `AF IMPERIYA Bot`
4. Username kiriting: `afimperiya_bot`
5. Token olasiz (masalan: `1234567890:ABCdefGHI...`)

### Bot'ni ulash

1. Render.com'da Environment Variables'ga qo'shing:
   ```
   TELEGRAM_BOT_TOKEN = <your_bot_token>
   ```

2. Webhook sozlang:
   ```bash
   curl -X POST "https://api.telegram.org/bot<YOUR_BOT_TOKEN>/setWebhook?url=https://your-app.onrender.com/telegram-webhook"
   ```

### Foydalanish

1. Bot'ga `/start` yuboring
2. Sizning email adresingizni qo'shing (tizimda ro'yxatdan o'tgan bo'lishi kerak)
3. Endi yangi topshiriqlar va bildirishnomalarni Telegram orqali olasiz!

## 📱 Xususiyatlar

### ✅ 4 Xil Panel

1. **Admin Panel**
   - Barcha foydalanuvchilarni boshqarish
   - Rollarni o'zgartirish
   - Tizim statistikasi

2. **Rahbar Paneli**
   - Barcha modullarga kirish
   - Xodimlarni nazorat qilish
   - Topshiriqlarni tasdiqlash

3. **Xodim Paneli**
   - Biriktirilgan modullarda ishlash
   - Topshiriqlarni bajarish

4. **User Panel**
   - So'rovnoma yuborish
   - Ma'lumotlarni ko'rish

### 📦 13 ta Modul

1. **Topshriqlar** - Vazifalarni boshqarish
2. **Avto Transport** - Mashinalar ma'lumotlari
3. **Ijro** - Real-time chat
4. **Binolar** - Bino ma'lumotlari
5. **Yashil Makonlar** - O'simliklar
6. **Quyosh Panellari** - Solar panellar
7. **Xodimlar** - Xodimlar bazasi
8. **Tasks (Kanban)** - Kanban board
9. **Outsorsing** - Xizmatlar
10. **Tashkilotlar** - Kompaniyalar
11. **Mehmonlar** - Mehmon registratsiyasi
12. **Tabriknomalar** - Tug'ilgan kunlar
13. **Shartnomalar** - Shartnomalar bazasi

## 🔐 Default Login Ma'lumotlari

Birinchi kirish uchun:

```
Email: admin@afimperiya.uz
Parol: admin123
```

⚠️ **Muhim**: Tizimga kirgandan keyin parolni o'zgartiring!

## 📊 Export Funksiyalari

Har bir modulda:
- **PDF Export** - Hisobotlarni PDF'da yuklab oling
- **Excel Export** - Ma'lumotlarni Excel'da oling
- **Word Upload** - Hujjatlarni yuklang

## 🎨 Dizayn

- O'zbekiston milliy ranglari (Ko'k, Yashil, Qizil)
- Zamonaviy, professional ko'rinish
- Mobile-friendly (telefonda ham ishlaydi)
- Dark sidebar
- Animated elements

## ❓ Tez-tez so'raladigan savollar

### Database xatosi chiqqanda?

```bash
# Database'ni qaytadan yarating
rm af_imperiya.db  # Agar mavjud bo'lsa
python init_db.py
```

### Parolni unutdim?

```python
# Python shell'da
from app import app, db
from models import User
with app.app_context():
    user = User.query.filter_by(email='admin@afimperiya.uz').first()
    user.set_password('yangi_parol')
    db.session.commit()
```

### Telegram bot ishlamayapti?

1. Bot token to'g'ri ekanligini tekshiring
2. Webhook sozlanganligini tekshiring
3. Deploy tugaganligini kutib turing

### Render.com bepul emasmi?

Render.com **750 soat/oylik bepul** tarif beradi. Bu taxminan 31 kun. Lekin:
- Sayt 15 daqiqa ishlatilmasa, "uxlab qoladi"
- Birinchi kirish 30-60 soniya vaqt olishi mumkin
- Production uchun Starter plan ($7/oy) tavsiya etiladi

### Rasm yuklash ishlamayapti?

```bash
# Permissions tekshiring
chmod -R 755 uploads/
```

## 📞 Yordam

Muammolar bo'lsa:
- GitHub'da Issue oching
- Email: support@afimperiya.uz
- Telegram: @afimperiya_support

## 📚 Batafsil Ma'lumot

- **README.md** - To'liq ingliz tilidagi qo'llanma
- **DEPLOYMENT.md** - Batafsil deploy qo'llanmasi
- **LICENSE** - MIT License

## 🚀 Keyingi Qadamlar

1. ✅ Tizimni lokal ishga tushiring
2. ✅ Admin panel bilan tanishing
3. ✅ Yangi xodimlar qo'shing
4. ✅ Modullarni biriktiring
5. ✅ Telegram bot'ni ulang
6. ✅ Render.com'ga deploy qiling
7. ✅ Production uchun tayyorlang

## 🎓 Video Darsliklar (Coming Soon)

- [ ] Tizimni o'rnatish
- [ ] Modullar bilan ishlash
- [ ] Telegram bot sozlash
- [ ] Render.com'ga deploy
- [ ] Customization

## 🌟 Afzalliklar

- ✅ **Bepul va Open Source**
- ✅ **To'liq O'zbekcha**
- ✅ **Professional dizayn**
- ✅ **Telegram integratsiyasi**
- ✅ **PDF/Excel export**
- ✅ **Mobile-friendly**
- ✅ **Oson o'rnatish**
- ✅ **Deploy qilish uchun tayyor**

## 💡 Maslahatlar

1. **Production uchun**:
   - PostgreSQL ishlatiladi (Render avtomatik)
   - SECRET_KEY o'zgartiring
   - HTTPS automatic (Render'da)
   - Backup qiling

2. **Xavfsizlik**:
   - Default parolni o'zgartiring
   - SECRET_KEY maxfiy saqlang
   - Environment variables ishlatiladi
   - CSRF protection bor

3. **Performance**:
   - Database indexlar bor
   - Gunicorn 4 worker bilan
   - Static files optimized

---

**Made with ❤️ in Uzbekistan** 🇺🇿

**Muvaffaqiyatlar!** 🚀

Version 1.0.0 | November 2024
