---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/Private/Install.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Private/Install.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/Private/Install.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.

 # Splitting a homogeneous state into consecutive groups of species 

 # Splitting a sphere into smaller spheres at prescribed chunk energies 

### `wick_chunks`

 The sign is determined by the outer index of chunk energies. 

 # Binary widths of a homogeneous leg and its chunks 


# Private spheres as universal tensors

Give each leg twice the target width. A spectral point can transmit
the target from the same auxiliary position used in the sphere lower
bound. The cost of transmitting a binary common label shows that the
extra width supplies a strict margin, uniform in the spectral point.


### `cap`

 The largest doubled energy of a leg at the given width cap. 

### `universalSphere`

 The direct sum over the allowed energy profiles. 

 # Local matrices implementing a private state on each chosen profile 

### `local_matrices`

 The common selector is internal. Once it is fixed, each map can
read only the state at its own site across the selected blocks. 

 # Uniform comparison with the direct sum of bounded sphere levels 

### `universal`

 Under shared-parameter pricing over an infinite extension, all the
restrictions are over the original field. Their multiplicative overhead
can depend on the target, but not on the tensor power. 

### `binary_matrices`

 The same width at every mark suffices for a block of binary rows. 

 # A private sphere on the packed species 

### `local_push`

 Push independent finite sums forward along site maps. Different
preimages of one local label contribute additively. 

### `local_packed`

 Pack the product of selected one-species spaces into prescribed
levels of a single private sphere. The order sign is fixed by the selector. 


# Realizing the signed joint state

The signature exchanging blocks depends only on their occupancy counts
at each mark. Include these counts in the common selector and check
them locally. The signature within a block is part of its input table.


### `signed`

 The coefficient across all species after ordering by marks. 

### `private_joint`

 The only coupling between distinct marks, beyond the private sphere
itself, is the common selection. Both energies are known from it. 

 # Energy and selector costs of the private sphere 

### `energyConstant`

 Absolute constant for the private energy bound. 

### `selector_small`

 Any prescribed selector rate is available by choosing the block
size first and then the number of blocks. 

 # Both spheres have prescribed total energies at every auxiliary mark 

### `push_level`

 Push the supported occupancy assignments onto the prescribed energy
level. The equality check is on the full ordered wedge. 

### `Coupling`

 One local coupling matrix per auxiliary mark. 


# Public energies and a private selector

The outer index records just the total energy at each auxiliary mark
of each sphere. Its size is polynomial in the number of species.
The short private selector is summed internally.


### `Shape`

 The two total doubled energies at each auxiliary mark. 

### `Program`

 One selector and one family of local tables per public shape.
The scalar weight can enforce consistency of the private choice. 


# Implanting a wiring table using two spheres

The original marks carry fixed-energy codes, independently for each
species. This includes seam labels. Only the total energy is checked
there, so the rule applies to an arbitrary summation over seam states.


### `install`

 The thresholds for the block size and number of blocks are uniform
in all three sets of positions, the individual widths and the wiring table. 
