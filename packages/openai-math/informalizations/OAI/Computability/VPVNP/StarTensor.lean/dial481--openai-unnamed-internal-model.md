---
{
  "module": "OAI/Computability/VPVNP/StarTensor.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarTensor.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/StarTensor.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Adding a center to a tensor

In the star construction of Theorem 2.4, the added party holds one end of
every wire. Its product basis is indexed by the full tuple of leaf indices.
A covector at the center can therefore specify the entries of an arbitrary
old-party tensor independently.


### `withCenter`

 Extend an old tuple of indices by an index for the additional party. 

### `embedOld`

 Embed an old tensor by using a one-dimensional factor at the center. 

### `contractCenter`

 Evaluate a covector on the center leg while keeping all the old legs. 

### `starBasis`

 The basis of a star of wires. The center stores a tuple and leaf `j`
stores only its component at `j`. 

### `starTensor`

 Equality wires from the center to every old party, in their product basis. 

### `contractCenter_starTensor`

 A single unrestricted covector on the center of the star realizes any
coefficient array in the indicated local dimensions. 

### `tensorPowerFin`

 A tensor power with its copies indexed by `Fin n` and their local legs
grouped at each party. 

### `starTensor_wireNetwork`

 The tuple-indexed star is the wire network joining the center to each
leaf, up to invertible local changes of basis. 

### `starTensor_tensorProduct`

 Multiplying two stars independently combines their two sets of wire
indices at each leaf and at the center. 

### `starTensor_powerFin`

 The power of a star has one enlarged wire of dimension `|I j| ^ n` at
each leaf. This identifies its joint center, including the zeroth power. 

### `contractCenter_starPowerFin`

 Arbitrary leaf coefficients on a power of the star are realized by one
covector on its entire center leg. Its coordinates transpose the copy and
party indices. 
