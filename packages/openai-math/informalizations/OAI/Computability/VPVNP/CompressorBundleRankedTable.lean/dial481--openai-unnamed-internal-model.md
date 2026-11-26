---
{
  "module": "OAI/Computability/VPVNP/CompressorBundleRankedTable.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleRankedTable.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorBundleRankedTable.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Ranking all old ports from the completed bundle lists

The native gather schedule runs on the append pass's memory. The rank
scan starts in the resulting memory, uses the same owner and count cells,
and writes the sorted bundle number for every original arc. No input about
the contents of the unused tail of a thick-wire row is required.


### `Ranked`

 Readback of both classes from the one rank column indexed by the original ports. 

### `ranked_table`

 Build the rectangular key table from actual bounded ID rows, then execute
one rank call per original port in the resulting physical memory. 

### `fixed_ranked_table`

 Execute both whole-table scans using one fixed bank each. 
