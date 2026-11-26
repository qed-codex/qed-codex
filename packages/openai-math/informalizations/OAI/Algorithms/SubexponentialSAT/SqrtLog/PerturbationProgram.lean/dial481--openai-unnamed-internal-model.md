---
{
  "module": "OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgram.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgram.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Algorithms/SubexponentialSAT/SqrtLog/PerturbationProgram.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 Explicit coefficient preparation for incidence perturbations.
The coefficient arrays are ordered from degree zero upwards. Every shift and
node evaluation is the existing finite represented-ring loop, not an oracle.
Counters here charge coefficient callbacks and list visits; primitive execution
is a separate interface and is not asserted by these counter theorems. 

### `coordinateRun`

 An explicit Horner evaluation and an explicit translated coefficient array. 

### `positiveRun`

 Removing the constant coefficient creates the actual positive-Z row delta. 

### `positiveRun_correct`

 This is the same polynomial as Moments.rowDelta, with no constant term. 

### `selected`

 The local head chooses the current assignment; other heads use the fixed
bucket representative. This selection is executable Boolean data. 

### `betaRun`

 A dot product against a Boolean vector: rejected entries perform no
multiplication, and selected entries use the explicit ring addition callback. 

### `singletonKey`

 One physical output key. Only the origin and positive-Z singleton keys
are emitted by the incidence preparer. 

### `emitPositive`

 Explicit row emission loop. The input is the tail of the translated array;
position j stores the coefficient of Z^(j+1), never the node value. 
