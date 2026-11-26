---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpNormalizationProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNormalizationProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpNormalizationProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

+# Fixed-control encoded CNF normalization

The common boundary uses stack 13 for the formula and empty work stacks.
Literal cleanup and tautology removal are lifted into that boundary here;
clause deduplication and strict-subset deletion use the same boundary.


### `absorbCommand`

 This subroutine is also used after constructing a sparsifier child. 

### `command`

 The complete program contains only the three checked fixed-control stages. 

### `raw_input_runsIn`

 The raw input is the encoded clause-list body; the variable-count header
is handled by the separate frontend initializer. 

### `typed_program_runsIn`

 Exact ordered refinement to the typed worklist's input, including its
redundant final literal-cleanup pass. No finite-set-only equality is used. 
