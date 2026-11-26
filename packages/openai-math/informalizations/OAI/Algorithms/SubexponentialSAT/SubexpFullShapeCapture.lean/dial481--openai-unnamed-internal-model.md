---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpFullShapeCapture.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFullShapeCapture.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpFullShapeCapture.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preserving capture of the padded-array shape

The actual unary chunk count is copied before the shape constructor consumes
its working counter. The width and count masters are preserved, as is every
caller stack except the initially empty output. All three work stacks are
restored empty. Port maps are fixed parts of the finite program.


### `shapeIndices`

 Local ports: width 0, output 1, shape scratch 2, count master 3,
working count 4, and copy scratch 5. 

### `output`

 Only the output stack changes; the three selected Boolean registers end
false, while all other caller registers are preserved. 

### `command_eval`

 Actual execution from an arbitrary caller state. The unary count comes
from a physical master stack; it is copied and is not consumed. 
