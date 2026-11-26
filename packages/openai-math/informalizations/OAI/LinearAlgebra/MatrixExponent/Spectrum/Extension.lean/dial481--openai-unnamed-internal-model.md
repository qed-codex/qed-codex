---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Spectrum/Extension.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectrum/Extension.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectrum/Extension.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Simultaneous extension of spectral points

Strict comparison transfers inequalities from the spectrum of the target.
A point outside its image can be separated by one such inequality: round
its finitely many coordinates, then clear denominators in the squared
distance and move negative terms to the other side.


### `separate_by_elements`

 A single ordered pair of semiring elements distinguishes a finite
strictly positive squared-distance gap. 

### `extension`

 It suffices that the given character respects comparisons made in the
target semiring. The extension agrees at every element simultaneously. 
