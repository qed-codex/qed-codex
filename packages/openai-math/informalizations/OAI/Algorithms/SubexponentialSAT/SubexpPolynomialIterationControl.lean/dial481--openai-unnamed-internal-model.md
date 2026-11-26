---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpPolynomialIterationControl.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPolynomialIterationControl.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpPolynomialIterationControl.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Reusing the polynomial multiplication workspace in a runtime-counted
loop. The output on 244 is moved back to accumulator 240, with all temporary
bits erased. The loop itself is the verified unary controller. 

### `repeat_visits`

 Exact observations of every invocation of the fixed iteration command.
The only component premise is its actual instruction trace and cost. 
