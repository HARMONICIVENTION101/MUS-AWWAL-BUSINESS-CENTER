from flask import Flask, render_template_string
app = Flask(__name__)
WHATSAPP = "2348069730375"
services = [
    {"name":"Photocopy", "desc":"A4 Black & White & Colour"},
    {"name":"Lamination", "desc":"ID Card, Certificate"},
    {"name":"Passport Photo", "desc":"Instant 8 copies"},
    {"name":"Printing", "desc":"All types printing"},
    {"name":"Scanning", "desc":"Scan to Phone & PDF"},
    {"name":"Typing", "desc":"CV, Letter, Project"},
    {"name":"Graphic Design", "desc":"Business Card, Banner"},
    {"name":"Online Registration", "desc":"JAMB, NIN, CAC, NYSC"},
    {"name":"Binding", "desc":"Spiral Binding"},
    {"name":"Plastic ID Card", "desc":"Original Plastic ID"},
]
HTML = """<!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1"><title>MUS AWWAL</title><style>body{margin:0;font-family:Arial;background:#f2f4f7}.head{background:#0b2a4a;color:white;padding:30px 20px;text-align:center}.grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;padding:15px}.card{background:white;padding:16px;border-radius:14px;box-shadow:0 2px 8px #0001;text-align:center}.btn{background:#25D366;color:white;border:0;width:100%;padding:12px;border-radius:8px;margin-top:10px;font-weight:bold}</style></head><body><div class="head"><h1>MUS AWWAL BUSINESS CENTER</h1><p>Photocopy | Lamination | Passport | Printing</p><p>Opposite Central Mosque, Okene</p><p>08069730375</p></div><div class="grid">{% for s in services %}<div class="card"><h3>{{s.name}}</h3><p>{{s.desc}}</p><button class="btn" onclick="order('{{s.name}}')">WhatsApp Us</button></div>{% endfor %}</div><script>function order(s){let m='Hello MUS AWWAL,%0AI need: '+s;window.open('https://wa.me/{{wa}}?text='+m,'_blank');}</script></body></html>"""
@app.route('/')
def home():
    return render_template_string(HTML, services=services, wa=WHATSAPP)
app.run(host='0.0.0.0', port=10000)
