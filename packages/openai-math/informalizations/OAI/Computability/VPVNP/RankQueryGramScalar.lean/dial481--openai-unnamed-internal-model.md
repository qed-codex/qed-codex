---
{
  "module": "OAI/Computability/VPVNP/RankQueryGramScalar.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryGramScalar.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankQueryGramScalar.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # The signed Gram-entry call of the physical Schur interpreter

The binary program first computes the Gram column from the degree. It tests
the emitted tag, writes zero or invokes the two Macaulay reads, and applies
packed-field negation when the enclosing Schur factor supplies a minus sign.


### `Small`

 Word-machine ports for Gram dispatch, with `14 + Dispatch.capacity` registers and zero
public input words. 

### `Registers`

 The width-`w` register file for Gram dispatch, holding the eight inputs, six descriptor
outputs and compiler scratch registers. 

### `Port`

 Stack addresses for Gram descriptor words, multiplication, negation, literal-writing
scratch and the supplied matrix-entry reader. 

### `outWord`

 Word-stack address of the `i`th Gram descriptor output register. 

### `reads`

 Wire the two row inputs and common column of a Gram read to output words one, two and
three, and route its multiplier and reader ports to their banks. 

### `negPorts`

 Wire field negation to its own row-arithmetic workspace and the multiplier's shared
external field stacks, including the accumulator. 

### `literalPorts`

 Wire the literal writer to the packed coefficient advice and product accumulator, using
`extra` and `tmp` for its work stacks. 

### `branch`

 For descriptor tag one, read and multiply the two entries in the designated column. For
every other tag, write the packed zero scalar. 

### `sign`

 Negate the field accumulator when the Schur descriptor requests a minus sign and return it
as supplied otherwise. 

### `machine`

 Decode the column for a weighted Gram coefficient, compute its two-entry product or zero
according to the tag, and apply the requested sign. 

### `bank`

 Assemble the signed coefficient call's word, multiplication and reader banks with empty
negation and literal-writing work stacks. 

### `wordBank`

 Initialize the Gram dispatch word stacks from the persistent word and registers, with an
empty write log and zero public inputs. 

### `clock`

 Time bound for Gram index dispatch, two entry reads of at most `B` steps each, the product
or zero branch and the optional field negation. 
