---
{
  "module": "OAI/Computability/VPVNP/CompressorCanonicalWorkerRows.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCanonicalWorkerRows.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorCanonicalWorkerRows.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A fixed dense representation of the demand rows of a semantic pass

The representation uses the exact demand vector of every motif of the
shrinking or refresh pass. The native verifier on this memory has the same
successful tapes as on any physical level directory representing those
vectors, including on an empty set of demand coordinates.


### `memory`

 Row-major initial memory for the demand scan, storing motif demands in the specified
coordinate order and zero outside the table. 

### `layout`

 Disjoint strided demand and term tables, with the first term record immediately after the
final demand row. 

### `input`

 The fixed dense encoding runs the real native term program and uses
its uniform clock. It only depends on the old graph and the pass origin. 
