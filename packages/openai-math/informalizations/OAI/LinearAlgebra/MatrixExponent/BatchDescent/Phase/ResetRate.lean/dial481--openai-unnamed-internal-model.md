---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/BatchDescent/Phase/ResetRate.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Phase/ResetRate.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/BatchDescent/Phase/ResetRate.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Quantitative contract for one encoded contraction or reset

A phase reduces block height by exactly `r`. Its constants are
independent of the number of hosts and blocks. Only the charge on
long addresses can involve a polynomial of the global width `w`.


### `degreeBound`

 Choose an artificially large full degree so noncore marks cannot
propagate. Only the small core graph needs to be stored. 

### `Input`

 Preconditions shared by all encoded inputs at a phase boundary. 

 # A common domain for bounds uniform in the host and block counts 


# Charges on host addresses and short block records

Multiplication by a short quantity is allowed in both terms of the
budget. Multiplication by the world size is confined to the first.


 # Polynomial cost of the new table controls after a host reset 

 # Controlling widths after an expansion of hosts 

 # The cost of retaining exterior labels after an expansion 

 # Gathering neighboring records without duplicating long addresses per block 
