from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import numpy as np
import json
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"status": "ok"}

# Load JSON file
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "q-vercel-latency.json"), "r") as f:
    TELEMETRY_DATA = json.load(f)

@app.post("/api/latency")
async def latency_analytics(payload: dict):

    regions = payload.get("regions", [])
    threshold_ms = payload.get("threshold_ms", 180)

    results = []

    for region in regions:
        records = [r for r in TELEMETRY_DATA if r["region"] == region]

        latencies = [r["latency_ms"] for r in records]
        uptimes = [r["uptime_pct"] for r in records]

        results.append({
            "region": region,
            "avg_latency": round(sum(latencies) / len(latencies), 1),
            "p95_latency": round(float(np.percentile(latencies, 95)), 2),
            "avg_uptime": round(sum(uptimes) / len(uptimes), 3),
            "breaches": sum(
                1 for r in records
                if r["latency_ms"] > threshold_ms
            )
        })

    return results