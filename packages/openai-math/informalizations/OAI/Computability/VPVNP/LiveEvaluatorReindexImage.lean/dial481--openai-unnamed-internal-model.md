---
{
  "module": "OAI/Computability/VPVNP/LiveEvaluatorReindexImage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorReindexImage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveEvaluatorReindexImage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Memory invariant for the evaluator's exponent scatter

Each dense exponent bit has a distinct destination in the first tape. The
invariant describes exactly the visited payload slots and preserves every
other address. At completion the initial zero-exponent bank has become the
bank for the actual evaluator input in formal-coordinate order.


### `symbolAddress`

 Physical word address of an exponent payload symbol. 

### `Image`

 Dense source `q` has been read if its position precedes the cursor. 

### `stores_formal`

 The completed scatter gives every word of the initialized evaluator on
the real exponent vector, including all unchanged advice, width tags, padding,
state and second-tape words. 
