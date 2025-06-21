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
        trigger=IntervalTrigger(hours=1),
        name="Publish deals every hour",
        replace_existing=True,
    )
    scheduler.start()
    logging.info("⏰ Scheduler started")