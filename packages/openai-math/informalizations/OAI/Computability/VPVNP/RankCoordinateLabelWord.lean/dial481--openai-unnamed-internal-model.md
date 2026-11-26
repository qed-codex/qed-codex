---
{
  "module": "OAI/Computability/VPVNP/RankCoordinateLabelWord.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateLabelWord.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/RankCoordinateLabelWord.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Encoding the one-based label in a Cramer target row

The evaluator's label port stores its zero-based ordinal in unary. The powered
monomial reader takes a fixed-width binary mark with value one greater. The
original unary stream survives the conversion and can be reused on return.


### `machine`

 Convert a zero-based unary label ordinal to its one-based binary mark, preserving the
source stream. 

### `clock`

 Step count for copying the unary label, appending one marker, and counting into a
fixed-width word. 
