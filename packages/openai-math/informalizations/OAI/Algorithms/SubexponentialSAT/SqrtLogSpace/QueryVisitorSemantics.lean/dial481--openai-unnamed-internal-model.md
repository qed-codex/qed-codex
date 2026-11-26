---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorSemantics.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorSemantics.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLogSpace/QueryVisitorSemantics.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Concrete execution of the two representative passes. The saved frame
stack is traversed in place, and every semantic dictionary is the one written
by the actual arithmetic command. 

### `mask`

 The mask produced by the actual addressed head loader. 

### `baseline_head`

 One first-pass visit reloads the real head, then installs its parsed
representative in the ambient baseline. No head-mask producer is assumed. 

### `baseline_pass`

 The whole first pass runs only the concrete addressed loader and overlay.
The list indexes the already emitted polynomial frame stack; no executable
assignment list or callback service occurs in this statement. 

### `frame_word_mass`

 The stored representative frames already pay for the parser's payload
mass; the proof does not construct any assignment enumeration. 

### `initialize_baseline`

 The actual initialization and whole first pass construct the full
ambient representative assignment. Its head masks and representative bits
are tied to the concrete loaded source, rather than supplied by an evaluator. 

### `headPrefix`

 Proof-level product of the heads that the decreasing replay has not yet
visited. This indexes only the already emitted tuple. 

### `headPrefix_step`

 Multiplying the visited head removes exactly its factor from the
unvisited product, without taking any quotient or applying readout early. 

### `evaluation_pass`

 The fixed second replay multiplies the actual normalized head sums in
reverse head order. The proof tracks the remaining product without division;
readout is still deferred to the completed tuple tail. 

### `facts_mask`

 The literal source certificate identifies the actual mask emitted at each
address with the original free head fiber. 

### `representativeWord_selected`

 The same physical representative word used by the key evaluator is the
selected ambient extension used by the first pass. 

### `visitor_run`

 The actual fixed visitor first reconstructs every representative, then
multiplies every restricted head sum, and finally adds one completed readout.
All execution witnesses are produced by the concrete commands in this proof. 
