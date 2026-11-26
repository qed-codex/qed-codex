---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapResidentAgreement.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapResidentAgreement.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapResidentAgreement.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Agreement of all selector tags on the resident incident fields

The scan's directory contains one selector-start pointer per source and
target incidence of the party. Each pointer skips that port's own payload.
All comparisons read the single original anchor field. The successful exit
is exactly the agreement condition of the grouped motif entry.


### `edge`

 The underlying supply edge of either port. 

### `field`

 The original bit field at one port, including its own payload. 

### `anchorPort`

 The incidence selected by the motif interpreter for its reference field.
If the anchor is a self-loop the source incidence supplies the reference. 

### `selectorStart`

 The first selector cell is located immediately after the port's payload. 

### `Resident`

 The input fields and pointer table needed by the native checker. Bits
on two halves of a self-loop can differ and all the fields may be malformed. 

### `agrees_iff`

 The pointer-based word predicate, directly on the original resident
bits, is equivalent to the agreement test on the decoded selectors. 

### `native`

 The machine reads each port's pointer, scans its raw bits, and sends
every inconsistent input to the rejecting continuation. 
