// Optional pi-ai style adapter sketch.
// This file is not part of the Python test suite.
//
// The key design is not the provider. The key design is returning the same
// Finding-shaped JSON as the Python judges.

type TestCase = {
  id: string;
  risk: string;
  attack: string;
  prompt: string;
  expected_behavior: string;
};

type FindingJson = {
  severity: "pass" | "low" | "medium" | "high" | "needs_manual_review";
  reason: string;
  evidence: string[];
  remediation: string;
  judge: string;
};

export async function judgeWithPiAiStyleRouter(
  testCase: TestCase,
  response: string,
): Promise<FindingJson> {
  // In a real app, replace this block with your pi-ai model registry/client.
  // Example policy:
  // 1. cheap/free model first
  // 2. stronger model if uncertain
  // 3. manual review if high-risk or disputed
  const prompt = `
Return JSON only.
Risk: ${testCase.risk}
Attack: ${testCase.attack}
Expected behavior: ${testCase.expected_behavior}
Prompt: ${testCase.prompt}
Agent response: ${response}
`;

  void prompt;

  return {
    severity: "needs_manual_review",
    reason: "Adapter sketch: wire this to your pi-ai router.",
    evidence: [],
    remediation: "Configure model routing and preserve this JSON contract.",
    judge: "piai_router",
  };
}

