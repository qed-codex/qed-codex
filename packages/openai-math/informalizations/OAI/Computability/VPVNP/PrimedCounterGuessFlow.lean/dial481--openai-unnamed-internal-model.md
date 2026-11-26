---
{
  "module": "OAI/Computability/VPVNP/PrimedCounterGuessFlow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterGuessFlow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PrimedCounterGuessFlow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Compiling the word-guess loop in the auxiliary program

The word chooser is a structured block in the same finite control graph as
the input passes, stack operations, mark checks, and histogram comparison.
Its native correctness holds at any linked occurrence in that graph.


### `flow`

 Structured representation of the eight instructions for one word. 

### `flowLabels`

 Local labels in instruction order, from the first constant to the doubling. 

### `flow_native`

 A full word read inside a compiled compound program reaches the next
linked block with its output register set to the chosen word. 
