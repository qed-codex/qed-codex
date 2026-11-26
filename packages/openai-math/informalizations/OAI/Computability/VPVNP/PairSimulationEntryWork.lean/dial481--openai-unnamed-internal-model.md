---
{
  "module": "OAI/Computability/VPVNP/PairSimulationEntryWork.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationEntryWork.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationEntryWork.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Work of a recorded map occurrence

At a shrink or refresh site, the descriptor records the number of repeated
base lookups as the map's degree. The fixed selector and base-entry tables
therefore give a bound in terms of that individual degree on every input,
including a syntactic zero. Successful lists additionally cost seven native
counter instructions per label and the loop's final test.


### `EntryInput`

 Complete arguments of a recorded template lookup, including arbitrary
incident coordinates in their declared half-wire widths. 

### `EntryInput.demand`

 Number of input bits requested on each demand edge. 

### `EntryInput.payload`

 Number of payload bits requested on each supply edge. 

### `EntryInput.party`

 Party at which the interpreter looks up the local tensor entry. 

### `EntryInput.demandBits`

 Input coordinates on the demand half-wires incident to the party. 

### `EntryInput.supplyBits`

 Input coordinates on the supply half-wires at the template's computed widths. 

### `EntryInput.work`

 The actual metered template interpreter and the length of the native
label-counter prefix when the input is accepted. 

### `entry_work_le_degree`

 The constant depends only on the fixed template and precedes the input
widths, outer index, party and every supplied bit. 

### `MapInvocation`

 The two actual map interpreters at a block schedule's sites. The recorded
degree of a map bounds its base copies. A diagonal test can emit no labels. 

### `MapInvocation.work`

 Interpreter and label-counter work of the selected lookup, or zero when no lookup runs. 

### `mapInvocation_bound`

 One constant controls both template tables at every level. 
