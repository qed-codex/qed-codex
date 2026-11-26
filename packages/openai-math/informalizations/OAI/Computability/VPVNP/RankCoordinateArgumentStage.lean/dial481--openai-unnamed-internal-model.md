---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateArgumentStage.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateArgumentStage.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateArgumentStage.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Installing the live Cramer query into its paired root banks

The four copied words are the replacement ordinal, the original monomial
index, the one-based label mark, and the target power scale. The first two
come from the greedy selector's binary register bank. Every write is to a
scalar-reader port of the numerator. Both roots, the arithmetic field advice,
and the entire denominator reader retain their initialized contents.


### `Field`

 The four live Cramer arguments consist of a replacement-row index and three target-row
words. 

### `Num`

 The numerator workspace compares the row index and then reads either the original submatrix
or the replacement row. 

### `numSlot`

 The comparison register and the three independent inputs of the target reader. 

### `destination`

 Actual physical destination of each word in the paired roots. 

### `workPort`

 Place a working stack on the auxiliary side of the coordinate callback's bus. 

### `sources`

 Offsets five and seven are the two outputs of `Dynamic.machine`. The mark
and scale may have independent advice or runtime source ports. 

### `source_words_at`

 Only two dynamic registers are read during transport, so other registers
can be aliased to the enclosing evaluator's public ports. 

### `machine`

 Clear the four template words and copy their replacements with one shared
scratch stack. The control is independent of the values and address width. 

### `clock`

 Bound the steps to clear and copy all four argument words of the given width. 

### `install_comp`

 Install a smaller bank through a larger port embedding. This characterizes
the returned bank both on and off the four written stacks. 

### `num_bank_after`

 The four updates change precisely the replacement ordinal and the target
reader's own raw-bank slots, leaving the two submatrix index stacks empty. 

### `host_after`

 If the template has already been loaded, the entire paired host now sees
the correct updated root banks. Static denominator inputs survive unchanged. 

### `root_ready`

 Readiness of the updated numerator and denominator after the exact word
copies. Only the raw reader's own ready predicate is needed here. 

### `target_bank_after`

 Mount the concrete three target words inside any containing raw workspace.
Every unmounted raw-reader port retains the old value. 
