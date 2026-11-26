---
{
  "module": "OAI/Computability/VPVNP/CompressionDegreeCoverage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionDegreeCoverage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressionDegreeCoverage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Degrees of map witnesses throughout a compressor execution

The witnesses and records are indexed by the same pass and selected term.
The sum of the recorded map degrees at a site therefore bounds every local
choice there. This property is preserved by joining procedures, assembling
a scheduled block, and repeating it.


### `StatePass.DegreeCovered`

 The joint degree of a chosen kernel monomial is bounded by the degrees
of all map occurrences at its output site. 

### `StateExecution.DegreeCovered`

 Degree coverage at every site in every branch-dependent substep. 

### `DegreeCovered`

 The same degree bound for every admissible input state of a procedure. 

### `assemble_degreeCovered`

 Every shrinking step and the final refresh retain their own degree records
when the block is run on an arbitrary state. 
