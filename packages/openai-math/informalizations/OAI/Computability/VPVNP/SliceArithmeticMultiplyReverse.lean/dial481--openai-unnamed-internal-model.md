---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticMultiplyReverse.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticMultiplyReverse.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticMultiplyReverse.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Preparing the digit and accumulator streams for Horner multiplication

A marker for each coefficient controls one load of the next input word,
followed by an order-preserving store onto the digit stack and a store of
one zero word onto the accumulator. Thus the highest-degree coefficient is
the first Horner digit, while each limb retains its little-endian encoding.


### `Port`

 Operand, digit, accumulator, marker, and word-copy ports for preparing the Horner input
order. 

### `prepare`

 The final store and load use the unconsumed query suffix to reset the
staging register. Both operations leave this suffix in its original place. 

### `pack`

 Concatenate the little-endian bit encodings of a list of equal-width words in list order. 

### `frame`

 State of the digit-order conversion with the remaining query, prepared digits, zero
accumulator, marker count, and staging word. 

### `prepare_runs`

 Exact bit-stack execution for the query preparation. The three streams can
have arbitrary suffixes, and the staging register returns to the zero word. 
