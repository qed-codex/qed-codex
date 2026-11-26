---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/HashSelectProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 A fixed deterministic hash selector. Its input carries a unary round
counter and a saved candidate queue. Every round copies that queue, pays
for every mass evaluation, takes a binary argmin, and appends the winner.
The only computational premise is the explicit trace specification of the
mass subprogram; no semantic SAT or mass instruction occurs in the code. 

### `ControllerReady`

 The untouched input banks retain their initial values between rounds. 

### `controller_roundSpec`

 The concrete round establishes the loop specification. All calls,
including failed candidates and the initial candidate, are charged. 

### `controllerBudget_callback`

 This displays the contribution of every paid mass evaluation over K
rounds. Candidate enumeration is a separate, also traced preprocessing cost. 
