# scraper.py

import logging

def scrape_deals():
    """
    Заглушка парсера скидок. Позже будет заменена реальной логикой.
    """
    logging.info("🔍 Scraping deals...")

    # Пример списка акций
    deals = [
        {"brand": "Nike", "offer": "Up to 50% Off"},
        {"brand": "Uniqlo", "offer": "Extra 20% Clearance"},
        {"brand": "Macy’s", "offer": "Buy One Get One Free"}
    ]

    # Формируем красиво отформатированный текст
    message_lines = ["🔥 <b>New Deals Available!</b> 🔥"]
    for deal in deals:
        message_lines.append(f"👕 <b>{deal['brand']}</b> — {deal['offer']}")
    message_lines.append("\n#buyersclub #usa #deals")

    return "\n".join(message_lines)