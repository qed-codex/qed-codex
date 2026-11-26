---
{
  "module": "OAI/Computability/VPVNP/JointScalarMachine.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarMachine.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/JointScalarMachine.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical signed coefficient read for the joint integer system

The same finite bit-stack control executes all original row reads. Its
gate-stream advice specifies the two verifier circuits and the fixed motif
tables. The public query is one sign bit, the binary equation address and
the array of formal exponents. The returned unsigned integer is the selected
positive or negative part of the formal coefficient.


### `sparseRows`

 Sparse integer coefficient tables of the fixed equations, indexed in their finite row
order. 

### `highWidth`

 Number of bits reserved above the low input word to address the fixed equations following
the grammar rows. 

### `motifWidth`

 Width of the witness word that counts each signed part of a coefficient in the fixed
equations. 

### `productionAddress`

 Formal variable index of a grammar production in the joint grammar and motif system. 

### `denseProduction`

 Translate a production number from the primed parser's order into its formal variable
index. 

### `denseLocal`

 Translate a finite motif-entry number into its formal variable index in the joint system. 

### `rootLayer`

 Final grammar layer `n - 1`, from which the coefficient verifier starts a parse. 

### `rootState`

 State zero at the root of the grammar used for the joint coefficient query. 

### `parseBlock`

 Grammar verifier frame rooted at the final layer and state zero, with label exponents
addressed in the joint system. 

### `rowFrame`

 The exact advised checker. Its input wiring uses the formal coordinate
number of each grammar and motif label. 

### `checker`

 Single-output Boolean circuit for counting the selected sign of a joint equation
coefficient. 

### `checker_grammar`

 Count the checker witnesses at a grammar row. 

### `checker_motif`

 Count the checker witnesses at a motif row. 

### `checker_count`

 One bit-stack count gives the selected part of the actual integer row. 

### `scalar_runs`

 Execution of the fixed finite routine from its concrete port bank. The
signed part of the formal coefficient appears as a little-endian word on
the `.total` stack. The circuit advice depends only on the dimensions and
the fixed equation family. 

### `scalar_part_lt`

 The count is at most the number of full witness strings. 

### `scalar_digits_value`

 Reading the returned count word retains the selected part in full. 
