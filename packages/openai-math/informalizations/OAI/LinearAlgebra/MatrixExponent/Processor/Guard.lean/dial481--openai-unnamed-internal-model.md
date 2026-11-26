---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Processor/Guard.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/Guard.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Processor/Guard.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Padding finite tables and private bit assignments 

### `unused`

 An unused position must contain zero. 

### `sum_padded`

 Each assignment on the active bits has exactly one extension with
nonzero padding weight, even in characteristic two. 

 # Summing private bits in a scalar network 

### `sum_right`

 Trace the named private bits against unary tables of weight one.
Every assignment contributes once, with no division by the alphabet size. 

 # Class counts as linear combinations of broadcast bits 

 # Scalar checks of bounded linear inequalities 

### `checks_net`

 Each input count field has `w` bits. The register width `v` is
chosen to rule out overflow even on malformed inputs. 

 # Masked sums of bounded registers 


# Programming a vertex by a constant-size truth table

The fourth address is spare for trivalent vertices. Reading four
addresses per instruction makes the parallel reader a binary tree.


### `vertex_rule`

 The addresses of a gate may coincide, even across its two sides. 

 # Trivalent diagrams as lists of local instructions 

### `compile`

 One half of the instructions represents vertices. The other half
pins private bits beyond the last internal edge. Both sets of external
slots may refer to any visible data positions. 


# Feasibility of reported selector counts

A class can realize prescribed multiplicities exactly when their sum
equals the size of the class. Combining the classes and checking the
choice of cut then characterizes the reports of actual assignments.



# Checking a public report from its binary counts

Check the class sizes and the minimizing coordinate. These checks force
the counts into range and identify an actual report, so the budget
follows from the bound for genuine assignments.



# A programmable product of local weights

A common array stores the data bits. Each row supplies a descriptor and
four addresses in the array. Four batches of indirect reads deliver
the arguments to independent copies of the local table.



# A binary program for a finite-field table network

For each of the sixteen possible argument strings a descriptor has one
bit per field element. A valid program sets just the bit corresponding
to the desired weight. Even arbitrary descriptor bits have a well-defined
interpretation, the sum of the selected field elements.



# Repeated programmable contractions

The two halves of a data array hold exterior and private bits. Each
copy sums its private bits independently. The script is shared.



# Programming a network template

One script records the wiring and coefficients of a trivalent network.
The script is independent of the values at all visible positions.


### `weight_program`

 In particular any bounded weighted circuit on named input bits can
be evaluated repeatedly without duplicating its program input. 
