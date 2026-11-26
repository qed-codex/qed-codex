---
{
  "module": "OAI/Computability/VPVNP/RAMTapeInputParametersLog.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersLog.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RAMTapeInputParametersLog.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Reading the ceiling binary logarithm from a padded word

After reversing the bit stack, skip the leading zeros. For each bit below
the leading one emit one mark. A final extra mark is needed exactly when
one of those lower bits was set.


### `Port`

 Labels for the padded word, its reversed copy, and the unary ceiling-log output. 

### `State`

 States for reversing the word, skipping leading zeros, counting lower positions, and
rounding up if any lower bit is set. 

### `code`

 Emit one unary mark per position below the highest set bit and one more if a lower bit is
set, giving the ceiling binary logarithm. 

### `store`

 Place the word, its temporary reversal, and accumulated output on the logarithm scanner’s
ports. 

### `clog_leading_one`

 If the most significant bit is set, the ceiling logarithm counts the
bits below it and tests whether any of them is set. 

### `runs`

 Read every word, including zero and words with high padding, in linear time. 
