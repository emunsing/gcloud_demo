from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sql import get_db
from sqlalchemy import text

app = FastAPI(title="Cloud SQL Demo API")

@app.get("/db-test")
async def test_db(db: Session = Depends(get_db)):
    try:
        result = db.execute(text("SELECT version();"))
        version = result.fetchone()[0]
        return {
            "status": "success",
            "database_version": version
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }