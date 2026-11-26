---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapWidths.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapWidths.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapWidths.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native width sums for the inner selector sequence

After a selector is decoded, its width on each supply edge is a fixed table
entry. A private RAM scan over one edge's width cells gives either the field
offset before a copy or the full total checked against the term descriptor.
The scan preserves memory and has a fixed linear instruction count.


### `instruction`

 Registers hold cursor, exclusive end, running sum, the constant one and a
temporary width. Each successful iteration consists of four private instructions. 

### `Linked`

 The machine stores the four width-scan instructions at the addresses given by `pc`. 

### `accumulate`

 The loop scans the given resident widths, including an empty prefix.
Its register result is the machine-word sum and its instruction count is
independent of all widths and all other memory cells. 

### `widthPrefix_native`

 A zeroed accumulator returns the natural prefix total when it fits the
word. This is the offset or total computed by the abstract motif interpreter. 
