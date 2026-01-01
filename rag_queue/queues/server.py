from fastapi import FastAPI, Query, HTTPException

from client.rq_client import queue
from .worker import process_query

app = FastAPI()

@app.get("/")
def root():
    return {"status": "Server is up and running"}

@app.get("/chat")
def chat(query: str = Query(..., description="The chat query of the user")):
    job = queue.enqueue(process_query, query)
    return {
        "message": "Query submitted",
        "job_id": job.id
    }

@app.get("/result")
def get_result(job_id: str = Query(..., description="Job ID")):
    job = queue.fetch_job(job_id)

    if job is None:
        raise HTTPException(status_code=404, detail="Job not found")

    if not job.is_finished:
        return {
            "status": job.get_status(),
            "result": None
        }

    return {
        "status": job.get_status(),
        "result": job.return_value
    }
