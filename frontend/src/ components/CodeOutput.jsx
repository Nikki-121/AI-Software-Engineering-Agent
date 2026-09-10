function CodeOutput({ code }) {
  const copyCode = async () => {
    try {
      await navigator.clipboard.writeText(code);
      alert("Generated code copied!");
    } catch (error) {
      console.error("Copy failed:", error);
    }
  };

  return (
    <section className="result-card code-card">

      <div className="result-header">
        <h2>Generated Code</h2>

        <button
          type="button"
          onClick={copyCode}
        >
          Copy Code
        </button>
      </div>

      <pre className="code-output">
        {code}
      </pre>

    </section>
  );
}

export default CodeOutput;
