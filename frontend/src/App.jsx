import { useState } from "react";

import RequirementInput from "./components/RequirementInput";
import AgentProgress from "./components/AgentProgress";
import CodeOutput from "./components/CodeOutput";
import ReviewResults from "./components/ReviewResults";
import TestResults from "./components/TestResults";

import "./App.css";


function App() {
  const [requirement, setRequirement] = useState("");

  const [plan, setPlan] = useState("");
  const [generatedCode, setGeneratedCode] = useState("");
  const [review, setReview] = useState("");
  const [testingReport, setTestingReport] = useState("");

  const [currentAgent, setCurrentAgent] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");


  const runAgentWorkflow = async () => {
    if (!requirement.trim()) {
      setError("Please enter a software requirement.");
      return;
    }

    setError("");
    setLoading(true);

    setPlan("");
    setGeneratedCode("");
    setReview("");
    setTestingReport("");


    try {
      // -----------------------------
      // 1. Planner Agent
      // -----------------------------

      setCurrentAgent("Planner Agent");

      const planResponse = await fetch(
        "http://127.0.0.1:8000/api/plan",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            requirement
          })
        }
      );

      const planData = await planResponse.json();

      if (!planResponse.ok) {
        throw new Error(
          planData.detail || "Planner Agent failed."
        );
      }

      const generatedPlan = planData.plan;

      setPlan(generatedPlan);


      // -----------------------------
      // 2. Coding Agent
      // -----------------------------

      setCurrentAgent("Coding Agent");

      const codeResponse = await fetch(
        "http://127.0.0.1:8000/api/code",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            requirement,
            plan: generatedPlan
          })
        }
      );

      const codeData = await codeResponse.json();

      if (!codeResponse.ok) {
        throw new Error(
          codeData.detail || "Coding Agent failed."
        );
      }

      const generatedProjectCode =
        codeData.generated_code;

      setGeneratedCode(generatedProjectCode);


      // -----------------------------
      // 3. Reviewer Agent
      // -----------------------------

      setCurrentAgent("Reviewer Agent");

      const reviewResponse = await fetch(
        "http://127.0.0.1:8000/api/review",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            requirement,
            generated_code: generatedProjectCode
          })
        }
      );

      const reviewData = await reviewResponse.json();

      if (!reviewResponse.ok) {
        throw new Error(
          reviewData.detail || "Reviewer Agent failed."
        );
      }

      setReview(reviewData.review);


      // -----------------------------
      // 4. Tester Agent
      // -----------------------------

      setCurrentAgent("Tester Agent");

      const testResponse = await fetch(
        "http://127.0.0.1:8000/api/test",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json"
          },
          body: JSON.stringify({
            requirement,
            generated_code: generatedProjectCode
          })
        }
      );

      const testData = await testResponse.json();

      if (!testResponse.ok) {
        throw new Error(
          testData.detail || "Tester Agent failed."
        );
      }

      setTestingReport(
        testData.testing_report
      );

      setCurrentAgent("Workflow Complete");

    } catch (err) {
      console.error(err);

      setError(
        err.message ||
        "Something went wrong while running the agents."
      );

      setCurrentAgent("Workflow Failed");

    } finally {
      setLoading(false);
    }
  };


  return (
    <div className="app">

      <header className="header">
        <div>
          <h1>AI Software Engineering Agent</h1>

          <p>
            Multi-Agent AI System for Software Development
          </p>
        </div>
      </header>


      <main className="container">

        <section className="hero">
          <h2>
            Build Software with AI Agents
          </h2>

          <p>
            Enter a software requirement and let
            multiple AI agents plan, code, review,
            and test the solution.
          </p>
        </section>


        <RequirementInput
          requirement={requirement}
          setRequirement={setRequirement}
          onRun={runAgentWorkflow}
          loading={loading}
        />


        {error && (
          <div className="error-box">
            {error}
          </div>
        )}


        {currentAgent && (
          <AgentProgress
            currentAgent={currentAgent}
          />
        )}


        {plan && (
          <section className="result-card">
            <h2>Development Plan</h2>

            <pre>
              {plan}
            </pre>
          </section>
        )}


        {generatedCode && (
          <CodeOutput
            code={generatedCode}
          />
        )}


        {review && (
          <ReviewResults
            review={review}
          />
        )}


        {testingReport && (
          <TestResults
            report={testingReport}
          />
        )}

      </main>


      <footer className="footer">
        <p>
          AI Software Engineering Agent
        </p>

        <span>
          Planning • Coding • Review • Testing
        </span>
      </footer>

    </div>
  );
}


export default App;
