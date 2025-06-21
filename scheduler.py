# scheduler.py

import asyncio
import logging
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.triggers.interval import IntervalTrigger
from publisher import publish_deals

def start_scheduler():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(
        publish_deals,
        "cron",
        minute=0,  # каждый час в 00 минут
        id="publish_deals_hourly",
        replace_existing=True
    )
    scheduler.start()
    logging.info("📅 Scheduler started (every hour on the hour)")
