---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpMachineNodeOrder.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpMachineNodeOrder.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpMachineNodeOrder.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Selected-field nodes in the tuple machine's actual output order

The raw tuples use the fixed tuple program's order. The nonzero filter prepends
retained records, so its output is the reverse of the filtered raw list. The
node equivalence below uses exactly that order.


### `rawWords`

 Source-level output of the fixed tuple generator at depth four. 

### `nodeWords`

 The exact order produced by a prepend-emitting nonzero-record filter. 

### `nodeEquiv`

 No semantic node order is substituted: the equivalence follows the
actual tuple and filter output word for word. 

### `lifted_node_value`

 The coefficientwise word lift denotes the section value in the actual
machine node order as well. 
