from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
import numpy as np
import json

app = FastAPI()

# Enable CORS for POST from any origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

@app.options("/api/latency")
async def options_handler():
    return Response(status_code=200)

TELEMETRY_DATA = json.loads("""
[
  {
    "region": "apac",
    "service": "catalog",
    "latency_ms": 116.38,
    "uptime_pct": 98.811,
    "timestamp": 20250301
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 154.14,
    "uptime_pct": 98.438,
    "timestamp": 20250302
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 119.67,
    "uptime_pct": 99.436,
    "timestamp": 20250303
  },
  {
    "region": "apac",
    "service": "checkout",
    "latency_ms": 185.5,
    "uptime_pct": 99.459,
    "timestamp": 20250304
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 198.1,
    "uptime_pct": 98.725,
    "timestamp": 20250305
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 153.4,
    "uptime_pct": 99.204,
    "timestamp": 20250306
  },
  {
    "region": "apac",
    "service": "analytics",
    "latency_ms": 153.91,
    "uptime_pct": 97.638,
    "timestamp": 20250307
  },
  {
    "region": "apac",
    "service": "recommendations",
    "latency_ms": 119.95,
    "uptime_pct": 99.033,
    "timestamp": 20250308
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 132.01,
    "uptime_pct": 98.873,
    "timestamp": 20250309
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 190.41,
    "uptime_pct": 98.52,
    "timestamp": 20250310
  },
  {
    "region": "apac",
    "service": "support",
    "latency_ms": 139.61,
    "uptime_pct": 99.109,
    "timestamp": 20250311
  },
  {
    "region": "apac",
    "service": "payments",
    "latency_ms": 133.11,
    "uptime_pct": 99.066,
    "timestamp": 20250312
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 166.7,
    "uptime_pct": 98.406,
    "timestamp": 20250301
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 229.16,
    "uptime_pct": 97.302,
    "timestamp": 20250302
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 122.68,
    "uptime_pct": 98.053,
    "timestamp": 20250303
  },
  {
    "region": "emea",
    "service": "recommendations",
    "latency_ms": 202.35,
    "uptime_pct": 98.391,
    "timestamp": 20250304
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 201.34,
    "uptime_pct": 97.329,
    "timestamp": 20250305
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 187.14,
    "uptime_pct": 99.351,
    "timestamp": 20250306
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 157.29,
    "uptime_pct": 99.003,
    "timestamp": 20250307
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 153.56,
    "uptime_pct": 97.963,
    "timestamp": 20250308
  },
  {
    "region": "emea",
    "service": "support",
    "latency_ms": 204.21,
    "uptime_pct": 98.691,
    "timestamp": 20250309
  },
  {
    "region": "emea",
    "service": "checkout",
    "latency_ms": 226.66,
    "uptime_pct": 97.246,
    "timestamp": 20250310
  },
  {
    "region": "emea",
    "service": "catalog",
    "latency_ms": 181.49,
    "uptime_pct": 98.453,
    "timestamp": 20250311
  },
  {
    "region": "emea",
    "service": "payments",
    "latency_ms": 118.99,
    "uptime_pct": 99.18,
    "timestamp": 20250312
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 168.46,
    "uptime_pct": 98.499,
    "timestamp": 20250301
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 107.93,
    "uptime_pct": 97.314,
    "timestamp": 20250302
  },
  {
    "region": "amer",
    "service": "recommendations",
    "latency_ms": 127.64,
    "uptime_pct": 97.342,
    "timestamp": 20250303
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 197.28,
    "uptime_pct": 98.943,
    "timestamp": 20250304
  },
  {
    "region": "amer",
    "service": "support",
    "latency_ms": 221.19,
    "uptime_pct": 97.157,
    "timestamp": 20250305
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 207.06,
    "uptime_pct": 97.949,
    "timestamp": 20250306
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 183.15,
    "uptime_pct": 99.241,
    "timestamp": 20250307
  },
  {
    "region": "amer",
    "service": "analytics",
    "latency_ms": 119.18,
    "uptime_pct": 97.8,
    "timestamp": 20250308
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 199.75,
    "uptime_pct": 99.085,
    "timestamp": 20250309
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 127.89,
    "uptime_pct": 98.524,
    "timestamp": 20250310
  },
  {
    "region": "amer",
    "service": "catalog",
    "latency_ms": 131.59,
    "uptime_pct": 97.41,
    "timestamp": 20250311
  },
  {
    "region": "amer",
    "service": "payments",
    "latency_ms": 214.24,
    "uptime_pct": 99.324,
    "timestamp": 20250312
  }
]
""")

@app.post("/api/latency")
async def latency_analytics(request: Request):
    body = await request.json()
    regions = body.get("regions", [])
    threshold_ms = body.get("threshold_ms", 180)

    results = []
    for region in regions:
        records   = [r for r in TELEMETRY_DATA if r["region"] == region]
        latencies = [r["latency_ms"] for r in records]
        uptimes   = [r["uptime_pct"]  for r in records]
        results.append({
            "region":      region,
            "avg_latency": round(float(np.mean(latencies)), 2),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime":  round(float(np.mean(uptimes)), 3),
            "breaches":    int(sum(1 for l in latencies if l > threshold_ms))
        })

    return {"regions": results}
