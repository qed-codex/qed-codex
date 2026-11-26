---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Network/Dense.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Network/Dense.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Network/Dense.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Trivalent realization of arbitrary tables

Give the table one enable bit. Splitting on the next address bit enables
exactly one of two subtables, while a disabled subtable contributes the
factor one. Copying the remaining bits costs their width at each split.


### `cup`

 A pair of identical bundles with no inputs. 

### `curry`

 Turn some inputs into outputs, paying for a pairwise equality test
on the corresponding bits. 

### `Enabled`

 The additive width term pays for copying the unprocessed address bits. 

### `dense`

 Any table on `r` exterior bits needs at most `8 * 2 ^ r` trivalent vertices. 
