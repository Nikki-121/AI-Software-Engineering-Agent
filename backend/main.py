from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents.planner_agent import create_plan
from agents.coder_agent import generate_code
from agents.reviewer_agent import review_code
from agents.tester_agent import test_code


app = FastAPI(
    title="AI Software Engineering Agent",
    description="Multi-agent AI system for software development",
    version="1.0.0"
)


# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class RequirementRequest(BaseModel):
    requirement: str


class DevelopmentRequest(BaseModel):
    requirement: str
    plan: str


class ReviewRequest(BaseModel):
    requirement: str
    generated_code: str


class TestRequest(BaseModel):
    requirement: str
    generated_code: str


@app.get("/")
def home():
    return {
        "message": "AI Software Engineering Agent API is running",
        "status": "success"
    }


@app.post("/api/plan")
def create_development_plan(request: RequirementRequest):

    if not request.requirement.strip():
        raise HTTPException(
            status_code=400,
            detail="Software requirement cannot be empty."
        )

    try:
        plan = create_plan(request.requirement)

        return {
            "status": "success",
            "agent": "planner",
            "plan": plan
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.post("/api/code")
def create_project_code(request: DevelopmentRequest):

    if not request.requirement.strip():
        raise HTTPException(
            status_code=400,
            detail="Software requirement cannot be empty."
        )

    if not request.plan.strip():
        raise HTTPException(
            status_code=400,
            detail="Development plan cannot be empty."
        )

    try:
        generated_code = generate_code(
            request.requirement,
            request.plan
        )

        return {
            "status": "success",
            "agent": "coder",
            "generated_code": generated_code
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.post("/api/review")
def review_project_code(request: ReviewRequest):

    if not request.requirement.strip():
        raise HTTPException(
            status_code=400,
            detail="Software requirement cannot be empty."
        )

    if not request.generated_code.strip():
        raise HTTPException(
            status_code=400,
            detail="Generated code cannot be empty."
        )

    try:
        review = review_code(
            request.requirement,
            request.generated_code
        )

        return {
            "status": "success",
            "agent": "reviewer",
            "review": review
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


@app.post("/api/test")
def test_project_code(request: TestRequest):

    if not request.requirement.strip():
        raise HTTPException(
            status_code=400,
            detail="Software requirement cannot be empty."
        )

    if not request.generated_code.strip():
        raise HTTPException(
            status_code=400,
            detail="Generated code cannot be empty."
        )

    try:
        testing_report = test_code(
            request.requirement,
            request.generated_code
        )

        return {
            "status": "success",
            "agent": "tester",
            "testing_report": testing_report
        }

    except Exception as error:
        raise HTTPException(
            status_code=500,
            detail=str(error)
        )


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
