---
{
  "module": "OAI/Computability/VPVNP/LiveLocalCountConditions.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLocalCountConditions.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/LiveLocalCountConditions.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Numeric bounds for the native local group count

Section 9 chooses the cut, evaluator-space and advice powers before the
processor exponent. The same choice made by `paper_parameters` supplies all
word, header and cost bounds needed for `LocalCount.group`.


### `conditions_of_majorant`

 Direct adapter for any choice of the public powers and processor exponent
satisfying the size bounds of `paper_parameters`. 

### `eventually_conditions_adapter`

 The fixed instruction clock and live bucket meet the two constant lower
bounds simultaneously at every sufficiently large length. 

### `eventually_paper_conditions`

 Select all length powers before the processor exponent and obtain the
actual local-count conditions at all sufficiently large lengths. 
