---
{
  "module": "OAI/Computability/VPVNP/ParseOracleCircuit.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseOracleCircuit.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/ParseOracleCircuit.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# A polynomial-size Boolean checker for coefficient queries

The query contains the input word and a fixed-width binary exponent at each
label address. Guess bits select events. Static advice supplies the incidence
clauses and the terminal and label tags of each event. The circuit accepts
exactly those flags whose leaf and production tallies match the query.


### `Var`

 A paired input variable indexed by a word position and one of its two Boolean values. 

### `Label`

 A terminal or binary production label for the grammar on the paired input variables through
degree `D`. 

### `Row`

 A tally row indexed by either a paired input variable or a grammar production label. 

### `Input`

 The checker input addresses for the public word and packed label exponents, followed by a
separate address space for the guessed event flags. 

### `query`

 Public query layout, with the word first and little-endian label exponents next. 

### `mask`

 Test whether the candidate event at a flag address carries the terminal or production tag
counted by the given row. 

### `wanted`

 The queried count at each terminal and production. 

### `frame`

 The query evaluator is independent of all actual queried exponent and word values. 

### `frame_size_le`

 The frame size is polynomial in the static flag count, row count, exponent
word width, and length of the incidence formula. 

### `circuitSize_le`

 The circuit size is polynomial in the static flag count, row count, exponent
word width, and length of the incidence formula. 
