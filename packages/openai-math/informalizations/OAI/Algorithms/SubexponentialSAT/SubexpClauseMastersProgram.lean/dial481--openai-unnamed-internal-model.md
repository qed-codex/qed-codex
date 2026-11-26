---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SubexpClauseMastersProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpClauseMastersProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SubexpClauseMastersProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Physical preparation of the shared clause-factor masters

Four preserved binary input words supply the declared variable count, chunk
width, field modulus, and chunk count. Copies of the three counts are converted
by the checked binary-to-unary program. The checked full-shape capture then
builds the padded-array shape. No desired shape is an input assumption.

The modulus-width shape is a physical copy of the modulus word: its consumers
use its length, not its bits. The other two copies supply the binary chunk
width and field modulus at the clause-family's own persistent ports.


### `initialState`

 Inputs 0--3, six outputs 4--9, and four initially empty work ports 10--13. 

### `outputState`

 Outputs: n-shape 4, ell-shape 5, full-shape 6, modulus-width 7,
binary ell 8, and modulus 9. All four original binary words are preserved. 

### `unaryCopy_eval`

 A preserving binary-to-unary call using fixed work ports 11--13. 

### `command_eval`

 All six requested masters are produced by actual instructions from four
binary words; the original words and all scratch-clear postconditions remain. 
