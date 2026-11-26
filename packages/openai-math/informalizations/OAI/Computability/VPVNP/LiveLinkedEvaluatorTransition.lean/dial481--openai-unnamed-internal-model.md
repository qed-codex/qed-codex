---
{
  "module": "OAI/Computability/VPVNP/LiveLinkedEvaluatorTransition.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorTransition.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLinkedEvaluatorTransition.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The terminal transition of the linked live evaluator

The initial call changes five scratch words. Each subsequent cell call
preserves external memory. The outer stage tag therefore persists throughout
the terminal scan, on arbitrary input words. The cap on its linked reports
retains one dispatcher probe per call and the full cost of any preceding
reports. Malformed raw cut fields contribute zero.


### `transitionPub`

 The four evaluated operands of the native transition check in this physical group. 

### `transition_frame`

 A terminal evaluator entry retains the stage tag on every returning
native call, including arbitrary scratch contents and malformed cut fields. 

### `transitionEquiv`

 The entire outer accepting suffix at the transition tag is precisely
the standalone evaluator segment, with the cap applied to every mapped
dispatcher report. It accepts the same individual branch streams. 

### `terminal_cost`

 A terminal transition adds exactly one dispatcher probe per native report. 

### `linked_transition_resources`

 The linked terminal stage charges one dispatch read per native call,
keeps the returned call count, and uses at most 47 additional instructions. 

### `linkedTransitionFits`

 Global and per-call transcript caps after prefixing the exact linked
transition reports by the already executed calls. 

### `linkedTailCount`

 Under the accumulated transcript budget the linked terminal suffix has
the paper's exact local tail multiplicity on raw boundary fields. This also
covers an invalid decoder output on either boundary. 
