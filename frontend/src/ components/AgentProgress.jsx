function AgentProgress({ currentAgent }) {
  const agents = [
    "Planner Agent",
    "Coding Agent",
    "Reviewer Agent",
    "Tester Agent"
  ];

  const currentIndex = agents.indexOf(currentAgent);

  return (
    <section className="progress-card">

      <h2>AI Engineering Workflow</h2>

      <div className="agent-list">

        {agents.map((agent, index) => {

          const isCompleted =
            currentIndex > index ||
            currentAgent === "Workflow Complete";

          const isActive =
            currentAgent === agent;

          return (
            <div
              key={agent}
              className={`agent-item ${
                isActive ? "active" : ""
              } ${
                isCompleted ? "completed" : ""
              }`}
            >

              <div className="agent-number">
                {isCompleted ? "✓" : index + 1}
              </div>

              <div className="agent-info">
                <strong>{agent}</strong>

                <span>
                  {isCompleted
                    ? "Completed"
                    : isActive
                    ? "Working..."
                    : "Waiting"}
                </span>
              </div>

            </div>
          );
        })}

      </div>

    </section>
  );
}

export default AgentProgress;
