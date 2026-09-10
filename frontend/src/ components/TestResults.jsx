function TestResults({ report }) {
  return (
    <section className="result-card">

      <div className="result-header">
        <h2>Testing Report</h2>

        <span className="agent-badge">
          Tester Agent
        </span>
      </div>

      <pre className="test-output">
        {report}
      </pre>

    </section>
  );
}

export default TestResults;
