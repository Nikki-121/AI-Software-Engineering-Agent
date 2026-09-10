function ReviewResults({ review }) {
  return (
    <section className="result-card">

      <div className="result-header">
        <h2>Code Review</h2>

        <span className="agent-badge">
          Reviewer Agent
        </span>
      </div>

      <pre className="review-output">
        {review}
      </pre>

    </section>
  );
}

export default ReviewResults;
