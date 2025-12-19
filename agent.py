from dotenv import load_dotenv
load_dotenv()

import os
import json
import requests
from tools import getOrderStatus


def read_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()


def velocity_chat(messages):
    base_url = os.getenv("VELOCITY_BASE_URL")
    api_key = os.getenv("VELOCITY_API_KEY")
    model = os.getenv("VELOCITY_MODEL")

    if not base_url or not api_key or not model:
        raise RuntimeError("Missing Velocity environment variables")

    url = base_url.rstrip("/") + "/chat/completions"

    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": model,
        "messages": messages,
        "temperature": float(os.getenv("VELOCITY_TEMPERATURE", "0.2"))
    }

    r = requests.post(url, headers=headers, json=payload, timeout=60)
    r.raise_for_status()

    return r.json()["choices"][0]["message"]["content"]


def run():
    products = read_json("products.json")
    system_prompt = read_text("prompt.txt")

    messages = [
        {"role": "system", "content": system_prompt},
        {
            "role": "system",
            "content": "PRODUCT CATALOG:\n" + json.dumps(products, indent=2)
        }
    ]

    print("\nNovaTech Agent (Production-Style Lab)")
    print("Type 'exit' to quit\n")

    while True:
        user = input("User: ").strip()
        if user.lower() == "exit":
            break

        messages.append({"role": "user", "content": user})

        raw = velocity_chat(messages)

        try:
            decision = json.loads(raw)
        except json.JSONDecodeError:
            print("Agent:", raw)
            messages.append({"role": "assistant", "content": raw})
            continue

        if decision.get("action") == "tool":
            tool_result = getOrderStatus(decision["order_id"])

            messages.append({
                "role": "system",
                "content": f"TOOL_RESULT: {json.dumps(tool_result)}"
            })

            final = velocity_chat(messages)
            final_json = json.loads(final)

            print("Agent:", final_json["message"])
            messages.append({"role": "assistant", "content": final_json["message"]})

        else:
            print("Agent:", decision["message"])
            messages.append({"role": "assistant", "content": decision["message"]})


if __name__ == "__main__":
    run()
