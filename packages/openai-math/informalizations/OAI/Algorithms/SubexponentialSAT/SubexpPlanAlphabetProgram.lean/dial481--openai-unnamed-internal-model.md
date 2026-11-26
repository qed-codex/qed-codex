---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPlanAlphabetProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPlanAlphabetProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPlanAlphabetProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed work bank for the all-vertex plan producer

The protected masters are the encoded scope list, D and Delta. A callback
copies them into the already checked per-vertex machine, emits a double-framed
plan record, and physically clears the work bank before the next vertex.


### `data`

 Masters: 16 scopes, 17 D, 18 Delta. The vertex stream is on 21,
its current payload on 23, and the plan alphabet accumulator on 24. 

 A closed callback for producing one framed forward vertex plan. 

 A physical record iterator invokes the closed plan-producing callback. 


# Actual all-vertices forward-plan alphabet

The machine generates the vertex indices itself from unary D, in descending
order. The checked callback prepends its output, so the final alphabet is in
ascending vertex order. Every alphabet payload is a framed forward read plan.


### `command_eval`

 No vertex list or slot assignment is an input. The only structural premise
is the degree bound on the runtime scope list. 
