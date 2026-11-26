---
{
  "module": "OAI/Computability/VPVNP/CompressorFormulaRow.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorFormulaRow.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/CompressorFormulaRow.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Native publication of a consecutive row of computed descriptor fields

The finite program evaluates the destination and all field expressions against
entry memory before performing any store. The program works at every word width
and its instruction and probe counts depend only on the expressions.


### `FormulaRow`

 A computed starting address and the consecutive words installed there. 

### `FormulaRow.dest`

 Expression computing the destination address of the first word of the published row. 

### `FormulaRow.fields`

 Expressions for the consecutive row words, evaluated against the entry memory before
  publication. 

### `carrier`

 Use the phase compiler's scratch allocation for exactly the requested
expressions. The extra phase prefix is omitted from the emitted assignments. 

### `recipe`

 Compile the row's destination and fields into a recipe that publishes the tag, interval,
and parameters. 

### `execute`

 Normal entry executes one burst, returns the next state, installs each
field at its natural address and preserves all words outside the row. 
