import json
import re

with open("raw.txt", "r", encoding="utf-8") as file:
    content = file.read()

prices = re.findall(r"\b\d+(?:[\s,]\d+)*(?:\,\d{2})?\b", content)


item_pattern = re.compile(
    r"(\d+)\.\n(.+?)\n([\d\s,]+?)\s*x\s*([\d\s,]+?)\n([\d\s,]+?)\nСтоимость\n([\d\s,]+?)(?=\n\d+\.|\nБанковская карта|\nИТОГО)",
    re.DOTALL,
)

products = []
for match in item_pattern.finditer(content):
    idx, name, qty, unit_price, line_total, _ = match.groups()
    products.append(
        {
            "id": int(idx),
            "name": name.strip(),
            "quantity": qty.strip(),
            "unit_price": unit_price.strip(),
            "total": line_total.strip(),
        }
    )


total_match = re.search(r"ИТОГО:\s*\n?\s*([\d\s,]+)", content)
total_amount = total_match.group(1).strip() if total_match else None

datetime_match = re.search(
    r"Время:\s*(\d{2}\.\d{2}\.\d{4}\s+\d{2}:\d{2}:\d{2})", content
)
datetime_info = datetime_match.group(1) if datetime_match else None


payment_match = re.search(
    r"^(Банковская карта|Наличные):", content, re.MULTILINE
)
payment_method = payment_match.group(1) if payment_match else None


result = {
    "store": "EUROPHARMA",
    "date_time": datetime_info,
    "payment_method": payment_method,
    "total_amount": total_amount,
    "products_count": len(products),
    "products": products,
}


print(json.dumps(result, ensure_ascii=False, indent=4))