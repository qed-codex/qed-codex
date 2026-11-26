---
{
  "module": "OAI/Computability/VPVNP/RAMTapeSuccessorChecks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorChecks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeSuccessorChecks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# The stack successor guard recognizes the shared-bit validator's fields

On an arbitrary local vector the finite stack program accepts exactly the
canonical present fields and the zero clamps. When the vector comes from a
shared-bit assignment, these tests are the successor parts of the local RAM
validator. A malformed field has zero accepting continuation count.


### `GoodField`

 A present successor field decodes to a canonical message, and an absent field consists
entirely of zero bits. 

### `finish_good_iff`

 The machine's two validity bits, evaluated on an arbitrary fixed-size
incident vector, test the full format including every padding bit. 

### `shared_fields_iff`

 At shared-bit inputs the missing end vectors are clamped by construction,
and the two remaining tests are exactly the sender and receiver predicates. 

### `checked_shared_count`

 The actual table spends the declared budget on valid fields and calls its
continuation once. On malformed fields its accepting multiplicity is zero. 
