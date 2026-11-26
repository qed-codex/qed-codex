---
{
  "module": "OAI/Computability/VPVNP/PairSimulationLeafStartup.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafStartup.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationLeafStartup.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Input stacks of an auxiliary RAM validator in a compression history

The auxiliary RAM has an entire word of header data at each address, including
the nomination words. Each input of the successor reader is taken from the
four half-wire buffers at the current vertex. Only the selected local incident
vector is used. The sender array extending it serves in the correctness proof.


### `expr`

 The constant-zero expression at each public index used to fix the type of the auxiliary
site processor's ports. 

### `Port`

 The private stack ports of a site processor with `r` machine registers and `k` public
operand positions. 

### `Field`

 Names of the finite collection of public fields copied into a leaf's
private stacks. A blank port gets length zero. 

### `field`

 Port assignments are fixed by the two linked stack machines. 

### `choiceBound`

 Number of choice bits reserved for the site validator, twice its bucket size times the sum
of its fuel and word width. 

### `fieldBits`

 Encode one input field as its stack bits, using binary words, unary counts, the site's
incident vector or the selected public operand. 

### `bank`

 Assign each processor port the stack encoding of its input field for the specified site and
public operands. 

### `sends`

 Local sender arrays from independently supplied half-wires. End clamps
come from the decoder at the two chain endpoints. 

### `auxiliary`

 The auxiliary call graph receives its complete header word and the exact
private cutoff of the finite coefficient counter. 
