---
{
  "module": "OAI/Computability/VPVNP/PairTreeFrontierBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreeFrontierBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairTreeFrontierBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Word headroom for every pending vertex

Each remaining vertex can add at most `nodeCap` to any one label counter.
The total allowance decreases by exactly one vertex when a row exposes its
children, including a leaf with no children. This bounds every intermediate
counter on arbitrary accepting prefixes, before the native word addition.


### `remaining`

 Count the unvisited vertices, including descendants of pending roots. 

### `Budgeted`

 The bound applies to each label separately, also when a later node
reads a field that was not reached on a successful whole-site path. 

### `Budgeted.headRoom`

 A nonempty frontier always has room for the local update, before its
value is represented modulo the machine's word size. 
