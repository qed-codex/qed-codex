---
{
  "module": "OAI/Computability/VPVNP/PairSimulationMapTagBits.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapTagBits.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PairSimulationMapTagBits.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Comparing selector suffixes in their original private bit fields

The payload lengths at two incident ports can differ. Starting each cursor
above its own payload, a private scan compares every bit in their selectors.
This checks the same condition as comparing the decoded selector words.


### `readTag_eq_iff_suffix`

 Flattening the copy and bit indices enumerates exactly the suffix above
the payload. This equivalence also covers zero-bit tags and zero copies. 

### `compareResidentTags`

 The native loop starts at the two payload boundaries and compares the
resident bits directly. It takes seven ticks per selector bit and one final
test. Its mask can feed the next port's comparison. 
