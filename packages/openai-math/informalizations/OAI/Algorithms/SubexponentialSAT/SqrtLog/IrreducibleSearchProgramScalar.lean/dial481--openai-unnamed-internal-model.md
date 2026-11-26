---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchProgramScalar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchProgramScalar.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/IrreducibleSearchProgramScalar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fixed truth-table arithmetic for the irreducible search over F₃

The six input bits select one of 64 *static* leaves. No parameter of the
polynomial search occurs in this instruction table. The two output bits
encode the multiply-add `s + a*b` in the same two-bit scalar format as the
audited tuple generator.


### `truthTable`

 Finite synthesis from a fixed list of input registers. Only register
branches and constant bit assignments occur in the resulting command. 
