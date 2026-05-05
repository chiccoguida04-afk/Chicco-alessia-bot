import os
import random
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes
from apscheduler.schedulers.asyncio import AsyncIOScheduler

# ======================
# CONFIGURAZIONE
# ======================
TOKEN = os.getenv("TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

DATA_INIZIO = datetime(2025, 12, 4)

# ======================
# FIGLIOLETTI 🧸
# ======================
figlioletti = [
    "NasNas", "Ossolini", "Wikky", "Pato", "Piero",
    "Franca", "Tino", "Lily", "Poppy", "Westie"
]

# ======================
# MESSAGGI DOLCI ❤️
# ======================
messaggi = [
    "Archivio emotivo: Alessia occupa una posizione stabile nei pensieri di Chicco ❤️",
    "Segnalazione dai figlioletti: oggi livello affetto molto alto 🧸",
    "Promemoria gentile: questa storia è tra le più belle registrate.",
    "Chicco risulta affezionato ad Alessia in modo costante ❤️",
    "Sistema relazione: amore in corso, nessuna anomalia rilevata 💌"
]

# ======================
# CANZONI ROMANTICHE 🎵
# ======================
canzoni = [
    "Ed Sheeran - Perfect",
    "Ed Sheeran - Thinking Out Loud",
    "John Legend - All of Me",
    "Lewis Capaldi - Someone You Loved",
    "Calcutta - Pesto",
    "Calcutta - Paracetamolo",
    "Franco126 - Brioschi",
    "Franco126 - Blue Jeans",
    "Tommaso Paradiso - Ricordami",
    "Tommaso Paradiso - Comunque",
    "Frah Quintale - Hai visto mai",
    "Frah Quintale - Colpa del vino",
    "Ultimo - Piccola Stella",
    "Ultimo - Alba",
    "Ultimo - Tutto questo sei tu",
    "Marracash - Crazy Love",
    "Annalisa - Mon amour",
    "Annalisa - Bellissima",
    "Elodie - Vertigine",
    "Irama - Ovunque sarai",
    "Thegiornalisti - Questa nostra stupida canzone d’amore"
]

# ======================
# RICORDI 📖
# ======================
ricordi = [
    "Halloween 2025 🎃",
    "La Locanda del 24 ottobre 🍽️",
    "Nascita ufficiale dei figlioletti 🧸"
]

# ======================
# FUNZIONI BASE
# ======================
def mesi():
    now = datetime.now()
    return (now.year - DATA_INIZIO.year) * 12 + now.month - DATA_INIZIO.month

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📂 Archivio Chicco & Alessia attivo ❤️"
    )

async def messaggio(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(random.choice(messaggi))

async def ricordo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📖 Memoria: " + random.choice(ricordi))

async def canzone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎵 " + random.choice(canzoni))

async def figlioletti_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🧸 Figlioletti: " + ", ".join(figlioletti))

async def quanto(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"❤️ Chicco e Alessia insieme da {mesi()} mesi"
    )

# ======================
# MESIVERSARIO AUTOMATICO ❤️
# ======================
async def mesiversario(app):
    text = f"""
💌 MESIVERSARIO CHICCO & ALESSIA 💌

Insieme da {mesi()} mesi ❤️

Dal 4 dicembre 2025 questa storia continua a crescere.

🧸 Figlioletti presenti: {random.choice(figlioletti)} oggi è in festa.

Sistema relazione: amore stabile e in evoluzione 💖
"""
    await app.bot.send_message(chat_id=CHAT_ID, text=text)

# ======================
# APP
# ======================
app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("messaggio", messaggio))
app.add_handler(CommandHandler("ricordo", ricordo))
app.add_handler(CommandHandler("canzone", canzone))
app.add_handler(CommandHandler("figlioletti", figlioletti_cmd))
app.add_handler(CommandHandler("quanto", quanto))

scheduler = AsyncIOScheduler()
scheduler.add_job(lambda: app.create_task(mesiversario(app)), "cron", day=4, hour=0, minute=0)
scheduler.start()

app.run_polling()
