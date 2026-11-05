import time
import requests
import pandas as pd
import yfinance as yf

# আপনার টেলিগ্রাম টোকেন এবং চ্যাট আইডি
TOKEN = "9249300034:AAHI1qc2pUlo2G-6FVuyg"
CHAT_ID = "7490703095"

# এক সাথে একাধিক জনপ্রিয় পেয়ার ট্র্যাক করার লিস্ট
SYMBOLS = ["EURUSD=X", "GBPUSD=X", "USDJPY=X"]

def send_telegram_signal(message):
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
    payload = {"chat_id": CHAT_ID, "text": message, "parse_mode": "Markdown"}
    try:
        requests.post(url, json=payload)
    except Exception as e:
        print(f"Telegram Error: {e}")

def get_market_data(symbol):
    try:
        df = yf.download(symbol, period="5d", interval="1m", progress=False)
        if isinstance(df.columns, pd.MultiIndex):
            df.columns = df.columns.get_level_values(0)
        return df
    except Exception as e:
        print(f"Data Error for {symbol}: {e}")
        return None

# বট চালু হওয়ার মেসেজ পাঠানো
send_telegram_signal("🚀 *Multi-Market Pro Trader Bot is running...*")

last_signals = {}
last_signal_times = {}

while True:
    for symbol in SYMBOLS:
        try:
            df = get_market_data(symbol)
            if df is not None and len(df) > 15:
                # 간단한 RSI ক্যালকুলেশন লজিক
                delta = df['Close'].diff()
                gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
                loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
                rs = gain / loss
                df['RSI'] = 100 - (100 / (1 + rs))
                
                current_rsi = df['RSI'].iloc[-1]
                current_time = time.time()
                
                # সিগন্যাল কন্ডিশন (যেমন RSI < 30 হলে Buy, > 70 হলে Sell)
                current_signal = None
                if current_rsi < 30:
                    current_signal = "BUY"
                elif current_rsi > 70:
                    current_signal = "SELL"
                
                if current_signal:
                    last_state = last_signals.get(symbol)
                    if current_signal != last_state:
                        signal_msg = f"🟢 *STRONG BUY SIGNAL*\nPair: `{symbol}`\nRSI: `{current_rsi:.2f}`" if current_signal == "BUY" else f"🔴 *STRONG SELL SIGNAL*\nPair: `{symbol}`\nRSI: `{current_rsi:.2f}`"
                        send_telegram_signal(signal_msg)
                        last_signals[symbol] = current_signal
                else:
                    last_signals[symbol] = None
                    
            time.sleep(10) # পেয়ারগুলোর মাঝে সামান্য বিরতি
        except Exception as e:
            print(f"Error analyzing {symbol}: {e}")
            
    time.sleep(60) # পুরো সাইকেল শেষ হওয়ার পর ১ মিনিট অপেক্ষা
