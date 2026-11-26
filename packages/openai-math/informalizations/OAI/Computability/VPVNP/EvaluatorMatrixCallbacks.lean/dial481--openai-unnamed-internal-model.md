---
{
  "module": "OAI/Computability/VPVNP/EvaluatorMatrixCallbacks.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorMatrixCallbacks.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/EvaluatorMatrixCallbacks.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Mounting the coordinate query in the monomial scheduler

A query sees the unary label number on one port and the weighted-step payload
on all other ports. The Frobenius and label entry readers use the same numeric
row and column representation. The remaining digit scheduler counters are
framed around the callbacks, so their sizes do not enter the query clock.


### `ReadPort`

 The query's label-index port together with the weighted-step ports for matrix indices,
field arithmetic and callback data. 

### `Host`

 The surrounding digit-fetch bank with a weighted matrix-step register bank mounted as its
work payload. 

### `mount`

 Only the label index of the outer schedule is shared with its entry reader. 

### `queryBank`

 The read ABI, with the label ordinal in unary. 

### `machine`

 Fixed outer callback for either the Frobenius or the label multiplication
query. The differing query controls are installed in the same ports. 

### `count_callback`

 From an actual deterministic entry reader, the complete callback
satisfies the bounded-delay law of the digit scheduler, with its label counter
and other outer registers preserved. 

### `outputPort`

 Identify the fixed ports from which the final routine reads. 

### `output_data`

 On the compatible polynomial-basis advice, the real arithmetic bank meets
the terminal reader's exact low-limb and endpoint-index specifications. 
