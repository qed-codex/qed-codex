---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputParametersBucket.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersBucket.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersBucket.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Computing a unary bucket size from the rounded binary exponent

The denominator is fixed in the finite control. For each nonempty block of at
most `q` input bits the machine doubles its unary output, using a third stack
temporarily. Every instruction reads or writes a single stack bit.


### `Port`

 Stack labels for the logarithm marks, unary bucket, and temporary doubling stack. 

### `State`

 States that double the unary bucket once per block and count the remaining skips within a
block of size at most the fixed denominator. 

### `code`

 Start with one bucket mark and double its unary value once for every nonempty block of at
most the denominator’s number of input marks. 

### `store`

 Represent the input, output, and scratch tallies of the bucket routine as stacks of true
bits. 

### `bucket_run`

 From initially empty work stacks, compute the unary bucket size and clear the input. 
