---
{
  "module": "OAI/Computability/VPVNP/CompressorFormulaFootprint.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorFormulaFootprint.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorFormulaFootprint.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# External addresses accessed by a compiled formula row

A load first evaluates its address in entry memory. The compiler's scratch
register then contains exactly that address when the read executes. After
the destination and field expressions finish, the row writer stores one
word at each consecutive machine address.


### `Expr.ReadsFrom`

 Every external address read while evaluating an expression belongs to
the specified region, including reads needed to compute another address. 

### `report_reads`

 Every external read of the actual formula-row report is justified by
a load in the destination expression or in one of the field expressions. 

### `report_writes`

 Stores use machine-word addition, even when a row wraps at the end of
the address space. 

### `report_writes_nat`

 A physically allocated row uses ordinary natural offsets for all stores. 
