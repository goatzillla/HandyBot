import json

def load_price_pages():
    with open("data/pricelist.json", "r", encoding="utf-8") as f:
        data = json.load(f)
        
    pages = []

    for key, content in data.items():
        title = f"🛠️ **{content['category_name']}**\n\n"
        items_text = ""
        
        # Собираем строчки товаров
        for item in content["items"]:
            unit = "hr" if item["unit"] == "hour" else "pc" if item["unit"] == "pc" else item["unit"]
            items_text += f"• {item['name']}: **${item['price']}** /{unit}\n"
            
        pages.append({
            "category_key": key,
            "text": title + items_text
        })
        
    return pages

PRICE_PAGES = load_price_pages()