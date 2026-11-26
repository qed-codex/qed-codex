---
{
  "module": "OAI/Computability/VPVNP/PerronRelation.lean",
  "declarations": [],
  "author": "dial481",
  "writer": "OpenAI (unnamed internal model)",
  "origin": "other-author",
  "entry_type": "source-documentation",
  "license": "Apache-2.0",
  "copyright_status": "absent",
  "source": "https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PerronRelation.lean",
  "source_commit": "3344da59991ed94f9ba711217b29c1d760badfa6",
  "kind": "ai"
}
---

Documentation comments extracted from this file at [3344da5](https://github.com/openai/math/blob/3344da59991ed94f9ba711217b29c1d760badfa6/lean/OAI/Computability/VPVNP/PerronRelation.lean). Any heading that names a declaration was added by QED Codex. The text is otherwise unchanged.


# Perron's quantitative algebraic-dependence argument

Substitute the given polynomials into a finite family of distinct monomials.
If the coefficient vectors of the images have fewer coordinates than the family
has elements, their linear dependence gives a nonzero polynomial relation.


### `perron_relation`

 Any `m + 1` polynomials of degree at most `D` in `m` variables satisfy a
nonzero formal polynomial relation of total degree at most `2 * (2 * (D + 1)) ^ m`. 
