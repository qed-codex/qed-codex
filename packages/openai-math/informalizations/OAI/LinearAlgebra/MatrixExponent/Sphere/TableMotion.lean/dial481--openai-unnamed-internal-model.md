---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Sphere/TableMotion.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/TableMotion.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Sphere/TableMotion.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Fusion of simultaneous collisions

Groups are in cluster order. Their offsets determine the independent
fusion coefficients, leaving a Wick sum at the cluster centers.


### `multifusion`

 The normalized generator pairing sums agree over every nilpotent
extension. Taking the parameter modulo its Nth power recovers any desired
finite precision of the expansion. 


# Sphere forms on fixed-energy legs

Permuting the marked sites contributes a sign independent of the
chosen basis words because each word's parity equals its energy parity.



# Passing an insertion through a seam

After fusing on the near side, sum the old seam state against the far
sphere. The transposed fusion map can be recovered there by regular
evaluations. The interpolation weights are independent of all states.


### `lowering`

 A fixed lowering map for the whole construction. 

### `cross_seam`

 Transpose the near-side fusion coefficient through the old seam.
One choice of lowering operator works for every position and energy.
The regular evaluation weights depend only on energies and marks. 


# A single seam crossing

The near sphere has the first coordinate, its private sphere the second.
At a seam the private sphere is regular. Negative Laurent orders therefore
force a drop on the shared seam. Only regular evaluations of the private
sphere and the far sphere are needed to reconstruct the crossing.


### `fusedEnergy`

 New doubled energy after an order-`i` collision. 

### `seam_drop`

 Multiply the weighted energies by `2P` to use integral units.
The loss covers the insertion and its reserve. 

### `coeff_at_seam`

 At a seam the second coordinate has no principal part. 

### `sew`

 Contract two spheres by equality on the indicated level. Negative
levels carry no states. 

### `transported`

 Value on the far sphere with the transformed insertion. 

### `seam_step`

 Reconstruct a seam coefficient by regular evaluations on the far
and private spheres, sewing at the lower level. The near and far spectator
energies are `u,w`. The private sphere has total doubled energy `n+v`,
including `n` from the mover. All weights are uniform in the basis entries. 


# Motion on paired spheres

In the shared coordinate, the powers in the first sphere's denominator
are multiplied by the characteristic power. Reconstruct from the
prescribed Laurent orders and fuse each insertion coefficient.


### `paired_reconstruction`

 The interpolation weights are independent of every basis mode.
The private sphere may omit stationary marks, including the seams. 

### `insertion_energy`

 The weighted energy after fusion is the sum of the two incident
energies plus the Laurent order, in units of `2P`. 

### `fusedAt`

 Fusion through one specified level, or zero at a negative level. 

### `insertion_step`

 At an insertion mark each term fuses both incident legs. 


# Fixed-energy tables in paired motion

The order of the exterior arguments is fixed before interpolating. A
collision can take place at any stationary mark. Bringing that mark
and the moving site to the front contributes a scalar depending only
on the energy labels and the mark.


### `table_seam`

 Sum an arbitrary joint table on the two movers and all spectators.
Its entries are independent of the internal seam index. 

### `table_insertion`

 Simultaneous fusion at an insertion for any joint table of inputs. 
