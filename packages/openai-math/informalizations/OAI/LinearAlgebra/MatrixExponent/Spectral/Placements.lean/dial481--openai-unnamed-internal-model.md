---
{
  "module": "OAI/LinearAlgebra/MatrixExponent/Spectral/Placements.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectral/Placements.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/LinearAlgebra/MatrixExponent/Spectral/Placements.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Extending the coefficient field

A field homomorphism acts entrywise on both tensor factors and local
restriction matrices. It therefore induces a monotone semiring homomorphism.



# Descent of restriction along a finite field extension

One extra diagonal label records one basis index at every site. Its
dimension depends on the field and the sites, and stays fixed even as
the local dimensions grow under tensor powers.



# Specializing a tensor restriction

The equations in the local matrix entries have coefficients in the base
field. A maximal ideal containing the kernel of evaluation preserves all
the equations simultaneously. Its residue field is a finite extension by
Zariski's lemma.



# Extension of spectral points under extension of scalars

One restriction specializes to a single finite extension. All powers
then descend with the same overhead, so every spectral point respects
the new comparison. Compact spectral extension yields agreement on
every tensor over the base field simultaneously.



# Moving a single leg along a wire

The old and new sites both pin the wire label to the corresponding
leg coordinate. For each target assignment there is exactly one
source assignment satisfying these local conditions and the wire.



# Transporting a tensor between placements


### `move_all`

 Iterate a transport bound proved for one leg at a time. 

### `log_transport`

 Convert multiplicative wire bounds into an additive estimate on logs. 
