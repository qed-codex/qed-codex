---
{
  "module": "OAI/Computability/VPVNP/LiveHeaderAdvice.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderAdvice.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveHeaderAdvice.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Copying the distributed live advice

Processor `j` holds advice bit `j` in slot one of its physical header. The
native scan reads each occupied header and writes its bit as a separate word
in the public advice array. The scratch array starts beyond the processor
sites, so later stages can still read all four fields at every site.


### `adviceTable`

 The native table for the advice stage. 

### `AdviceImage`

 Advice readback, preservation of the packed site headers, and the frame
for every word outside the allocated advice array. 

### `physical_advice_scan_native`

 Execute all occupied advice cells starting with any memory that retains
the physical headers. Zero-length advice gives an empty scan. 

### `physical_advice_bounded_native`

 The bounded advice table executes one active call per bit and closes
with a zero-probe accepting call. Its final memory contains the same advice
image, including when the advice array is empty. 
