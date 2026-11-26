---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafIncidentBank.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafIncidentBank.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafIncidentBank.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Representing the full stack bank after loading the incident bits

The descending native copy stores the head of the logical list at its highest
address. Updating the incident stack's exclusive top therefore installs the
list with exactly the stack representation used by the interpreter.


### `placed_contents`

 Install one physical field in its own disjoint stack interval. 

### `represents`

 Only the incident top pointer needs a new value. Scratch register
contents may change freely; the other base and top pointers keep their values. 

### `placed_memory`

 The exact private memory is determined by the old workspace and the
full bank. Outside both the scalar data and the new incident bits, stale
private cells keep their previous values. 

### `fullBank`

 Specialize the physical installation to the actual site-port layout.
The incident vector is precisely the field omitted by the scalar startup. 
