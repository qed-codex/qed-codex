---
{
  "module": "OAI/Computability/VPVNP/CompressorMatrixReader.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorMatrixReader.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorMatrixReader.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The augmented matrix reader for the compressor's actual finite model

The entry routine is a single finite bit-stack program. On every queried row
and column, including all original grammar and fixed compressor equations,
it returns the encoded scalar in the determinant algorithm's matrix. Its
reusable advice and workspace have a separate stack-height bound, independent
of the exponentially longer clock.


### `compressorMatrixReader`

 All coefficients of the actual encoded augmented Macaulay matrix are
computed on the physical scalar-entry ABI required by the rank engine. 
