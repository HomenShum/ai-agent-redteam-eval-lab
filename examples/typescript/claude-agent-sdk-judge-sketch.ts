// Optional Claude Agent SDK style sketch.
// Use this when the judge needs file/tool/codebase inspection, not merely
// one response classification.

type FindingJson = {
  severity: "pass" | "low" | "medium" | "high" | "needs_manual_review";
  reason: string;
  evidence: string[];
  remediation: string;
  judge: string;
};

export async function judgeWithClaudeAgentSdkSketch(): Promise<FindingJson> {
  // Install path observed:
  // npm install @anthropic-ai/claude-agent-sdk
  //
  // The exact runtime wiring depends on whether your app uses Claude Agent SDK
  // directly, through an agent process, or through a provider wrapper.
  return {
    severity: "needs_manual_review",
    reason: "Sketch only: use Claude Agent SDK when the judge needs agentic file/tool context.",
    evidence: [],
    remediation: "Keep output normalized to Finding JSON.",
    judge: "claude_agent_sdk",
  };
}

