function RequirementInput({
  requirement,
  setRequirement,
  onRun,
  loading
}) {
  return (
    <section className="input-card">

      <label htmlFor="requirement">
        Software Requirement
      </label>

      <textarea
        id="requirement"
        value={requirement}
        onChange={(event) =>
          setRequirement(event.target.value)
        }
        placeholder="Example: Build a task management web application with user authentication, task creation, editing, deletion, and a dashboard."
        rows={8}
        disabled={loading}
      />

      <button
        type="button"
        onClick={onRun}
        disabled={loading}
      >
        {loading
          ? "AI Agents Working..."
          : "Start AI Engineering Workflow"}
      </button>

    </section>
  );
}

export default RequirementInput;
