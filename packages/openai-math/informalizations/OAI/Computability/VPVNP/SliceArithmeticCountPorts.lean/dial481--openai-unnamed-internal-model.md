---
{
  "module": "OAI/Computability/VPVNP/SliceArithmeticCountPorts.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticCountPorts.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/SliceArithmeticCountPorts.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Register and stream interface for signed witness counts 

### `External`

 Caller ports for the two signed witness counts, the modulus and field width advice, and the
output coefficient. 

### `Private`

 Work ports for reducing both witness counts, subtracting their residues, and emitting the
packed field coefficient. 

### `Port`

 Stack interface for converting a signed witness count into a power-basis field element. 

### `external`

 Encode the two input counts, field parameters, and result suffix on the external
signed-count ports. 

### `frame`

 Install the current division input and the two saved residues alongside the caller's
stacks. 

### `clean`

 Signed-count workspace with empty division input and empty residue stacks for both signs. 

### `source`

 Select the negative count when `sign` is true and the positive count otherwise. 

### `divisionPorts`

 Route division through the advised prime and store its remainder on the port for the chosen
sign. 

### `reduceCount`

 A preserved count supplies the input of the division. Its quotient is
discarded, and the remainder remains on the selected arithmetic register. 

### `reduceCost`

 Step bound for copying an `n`-bit witness count and reducing it modulo a `w`-bit prime
word. 

### `arithmeticPorts`

 Map the subtraction registers to the prime and the two saved residues, using the caller's
zero word as width template. 
