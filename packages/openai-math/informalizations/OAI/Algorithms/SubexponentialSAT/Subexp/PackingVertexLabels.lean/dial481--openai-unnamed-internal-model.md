---
{
  "module": "OAI/Algorithms/SubexponentialSAT/Subexp/PackingVertexLabels.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingVertexLabels.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/Subexp/PackingVertexLabels.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Gathering the actual assignment type at every vertex before packing. 

### `gatherCall_eval`

 Lift the checked gather machine into the first ten work ports. 

### `callback_eval`

 Each callback consumes the actual framed plan, performs the persistent
array reads, and prepends one raw `(type, vertex)` record. 

### `iterationCost`

 The sum of actual callback bounds and actual outer-reader overheads.
The runtime counter increases, so its current value is included explicitly. 

### `command_eval`

 Execute every supplied forward plan in order. The packed assignment and
row width are preserved; the raw bucket records are prepended in reverse order. 

### `traceCost_le`

 A polynomial in the number of plans, maximum serialized plan size,
row width, and initial unary index. It also covers zero-width arrays. 

### `alphabet_eq_planPayload`

 The all-vertex producer's payloads are precisely this routine's inputs. 
