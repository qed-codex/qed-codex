---
{
  "module": "OAI/Computability/VPVNP/PairShrinkNodeLabelBudget.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkNodeLabelBudget.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairShrinkNodeLabelBudget.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Label counts of native shrinking and refresh rows

A successful motif invocation emits one label for each repetition, including
repeated labels. A shrinking row enumerates the six-party occurrences in its
published order. Its output on every input is bounded by the row capacity
times the repetition bound of the input state. A refresh has one invocation.


### `runEntry_length`

 A successful run on arbitrary bit inputs emits one base-matrix label
per copy, even if several copies select the same label. 

### `labels_length_ofFn`

 On a successful loop the list has exactly the sum of the copy counts.
A failing loop keeps the prefix already emitted, bounded by the same sum. 

### `row_label_lengths`

 On a passed row the degree equals the sum of the repetitions of its
actual entry calls. Every prefix of a rejecting row satisfies the upper bound. 

### `noncomputable local instance : DecidableEq Y.Base`

 Classical decidable equality on the compression state’s base vertices for counting labels
in the ordered resident row. 

### `row_label_budget`

 The resident row in the published directory has a linear label budget
in the input width, including inputs that fail at a later occurrence. 

### `noncomputable local instance : DecidableEq X.Base`

 Classical decidable equality on the compression state’s base vertices for bounding the
exponents of the selected shrink witness. 

### `selected_exponent_bound`

 Bound the increment of the actual selected kernel witness in the common
parameter alphabet, at the point where the frontier checks word headroom. 

### `eventually_row_constants`

 The input-length threshold for all shrinking stages is fixed before
choosing any state, layout, site or branch of the schedule. 

### `native_row_label_budget`

 Apply the width bound directly to the selected handler family on the
physical party jobs. Work and probe charges do not affect its emitted labels. 

### `emitted_length`

 The native refresh has one motif call after its diagonal checks. 
