---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorReindex.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorReindex.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorReindex.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Exponent coordinates on the physical evaluator input

The middle cut sends dense production rows followed by dense gadget rows.
The advised permutation identifies the corresponding formal coordinate of
the evaluator. Each low-endian row bit appears once in the raw input,
as the payload of a reversed tagged field. All remaining bytes of the
initial tape are identical to the raw input with zero exponent rows.


### `bitOrder`

 Lift the coordinate permutation, keeping every row's bit index fixed. 

### `payload`

 Address inside the tagged exponent field of the bit whose formal index
in the forward, low-endian array is `q`. 

### `rawSlot`

 Offset in the raw evaluator input, after the advised prefix and the
initial unary width field. 

### `raw_dense_at`

 The word read from dense row `q / Z` supplies exactly the payload
of the formal-coordinate evaluator field. 
